from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from django.db.models import Prefetch
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Course, Chapter, ContentBlock, ChapterAssignment
import markdown
import bleach
import json
from datetime import datetime


class CourseListView(LoginRequiredMixin, ListView):
    """List all published courses"""
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    
    def get_queryset(self):
        return Course.objects.filter(is_published=True).prefetch_related('chapters')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Add completion stats for each chapter
        if user.is_student:
            for course in context['courses']:
                for chapter in course.chapters.all():
                    chapter.completion = chapter.get_completion_for_user(user)
        
        return context


class CourseDetailView(LoginRequiredMixin, DetailView):
    """View a course with its chapters"""
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Course.objects.filter(is_published=True).prefetch_related('chapters')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        course = self.object

        # Add completion stats for each chapter
        if user.is_student:
            for chapter in course.chapters.all():
                chapter.completion = chapter.get_completion_for_user(user)

        return context


class ChapterDetailView(LoginRequiredMixin, DetailView):
    """View a chapter with its content blocks and exercises"""
    model = Chapter
    template_name = 'courses/chapter_detail.html'
    context_object_name = 'chapter'
    
    def get_object(self, queryset=None):
        """Get chapter by course_slug and chapter_slug"""
        if queryset is None:
            queryset = self.get_queryset()
        
        course_slug = self.kwargs.get('course_slug')
        chapter_slug = self.kwargs.get('chapter_slug')
        
        return queryset.filter(
            course__slug=course_slug,
            slug=chapter_slug
        ).first()

    def get_queryset(self):
        return Chapter.objects.filter(is_published=True).select_related('course')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chapter = self.object
        
        # Get content blocks with rendered markdown
        content_blocks = []
        for block in chapter.content_blocks.all():
            # Convert markdown to HTML
            html_content = markdown.markdown(
                block.content_markdown,
                extensions=['fenced_code', 'codehilite', 'tables']
            )
            # Sanitize HTML
            safe_html = bleach.clean(
                html_content,
                tags=['p', 'br', 'strong', 'em', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                      'ul', 'ol', 'li', 'a', 'code', 'pre', 'blockquote', 'table', 'thead',
                      'tbody', 'tr', 'th', 'td', 'div', 'span'],
                attributes={'a': ['href', 'title'], 'code': ['class'], 'pre': ['class'], 
                           'div': ['class'], 'span': ['class']}
            )
            content_blocks.append({
                'block': block,
                'html_content': safe_html
            })
        
        context['content_blocks'] = content_blocks
        context['exercises'] = chapter.exercises.filter(is_published=True)
        
        if self.request.user.is_student:
            context['completion'] = chapter.get_completion_for_user(self.request.user)
        
        return context


class AssignChapterView(LoginRequiredMixin, View):
    """Teacher assigns a chapter to their classroom"""
    
    def post(self, request, pk):
        if not request.user.is_teacher:
            messages.error(request, 'Seuls les professeurs peuvent attribuer des chapitres.')
            return redirect('courses:course_list')
        
        chapter = get_object_or_404(Chapter, pk=pk)
        classroom_id = request.POST.get('classroom_id')
        classroom = get_object_or_404(Classroom, pk=classroom_id, teacher=request.user)
        
        # Create or get assignment
        assignment, created = ChapterAssignment.objects.get_or_create(
            classroom=classroom,
            chapter=chapter
        )
        
        if created:
            messages.success(request, f'Chapitre "{chapter.title}" attribué à la classe {classroom.name}.')
        else:
            messages.info(request, 'Ce chapitre est déjà attribué à cette classe.')
        
        return redirect('courses:chapter_detail', slug=chapter.slug)


class ExportChapterNotebookView(LoginRequiredMixin, View):
    """Export chapter as Jupyter Notebook (.ipynb)"""
    
    def get(self, request, course_slug, chapter_slug):
        chapter = get_object_or_404(Chapter, slug=chapter_slug, course__slug=course_slug)
        course = chapter.course
        
        # Build Jupyter Notebook structure
        notebook = {
            "cells": [],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.12.0"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 5
        }
        
        # Add title cell
        notebook["cells"].append({
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# {course.title}\n",
                f"## {chapter.title}\n\n",
                f"{chapter.description}\n\n",
                f"---\n",
                f"*Généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}*"
            ]
        })
        
        # Add content blocks
        for block in chapter.content_blocks.all():
            if block.type == 'TEXT':
                # Text block as markdown
                notebook["cells"].append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": self._clean_html_for_markdown(block.content_markdown, block.title)
                })
                
            elif block.type == 'CODE_SAMPLE':
                # Add title if exists
                if block.title:
                    notebook["cells"].append({
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [f"### {block.title}\n"]
                    })
                
                # Code block as executable Python
                notebook["cells"].append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": block.content_markdown.split('\n')
                })
                
            elif block.type == 'QUIZ':
                # Quiz as markdown with special formatting
                notebook["cells"].append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"### 🎯 {block.title or 'Quiz'}\n\n",
                        *self._clean_html_for_markdown(block.content_markdown)
                    ]
                })
                
            elif block.type == 'EXERCISE':
                # Exercise as markdown
                notebook["cells"].append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"### ✏️ {block.title or 'Exercice'}\n\n",
                        *self._clean_html_for_markdown(block.content_markdown)
                    ]
                })
                
                # Add empty code cell for solution
                notebook["cells"].append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": ["# Écrivez votre solution ici\n"]
                })
        
        # Create response
        response = HttpResponse(
            json.dumps(notebook, indent=2, ensure_ascii=False),
            content_type='application/x-ipynb+json'
        )
        filename = f"{course.slug}_{chapter.slug}.ipynb"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        return response
    
    def _clean_html_for_markdown(self, html_content, title=None):
        """Convert HTML to markdown-friendly format"""
        import re
        lines = []
        if title:
            lines.append(f"### {title}\n\n")
        
        # Basic HTML to markdown conversion
        content = html_content.replace('<p>', '').replace('</p>', '\n\n')
        content = content.replace('<strong>', '**').replace('</strong>', '**')
        content = content.replace('<em>', '*').replace('</em>', '*')
        content = content.replace('<code>', '`').replace('</code>', '`')
        content = content.replace('<li>', '- ').replace('</li>', '\n')
        content = content.replace('<ul>', '\n').replace('</ul>', '\n')
        content = content.replace('</h2>', '\n').replace('</h3>', '\n')
        content = content.replace('<h2>', '## ').replace('<h3>', '### ')
        
        # Remove remaining HTML tags
        content = re.sub(r'<[^>]+>', '', content)
        
        lines.extend(content.split('\n'))
        return lines


class ExportChapterPDFView(LoginRequiredMixin, View):
    """Export chapter as printable PDF"""
    
    def get(self, request, course_slug, chapter_slug):
        chapter = get_object_or_404(Chapter, slug=chapter_slug, course__slug=course_slug)
        course = chapter.course
        
        # Render HTML template for printing
        context = {
            'chapter': chapter,
            'course': course,
            'content_blocks': chapter.content_blocks.all(),
            'generated_date': datetime.now().strftime('%d/%m/%Y à %H:%M')
        }
        
        html = render_to_string('courses/chapter_print.html', context)
        
        # Return HTML that can be printed to PDF by browser
        response = HttpResponse(html, content_type='text/html')
        return response
