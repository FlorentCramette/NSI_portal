from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Enrollment, Classroom


class StudentRegistrationForm(UserCreationForm):
    """Registration form for students"""
    
    pseudo = forms.CharField(
        max_length=50,
        required=True,
        label='Pseudo',
        widget=forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'})
    )
    join_code = forms.CharField(
        max_length=6,
        required=False,
        label='Code de classe (optionnel)',
        widget=forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 uppercase'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'pseudo', 'password1', 'password2', 'join_code']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].widget.attrs['class'] = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.STUDENT
        user.pseudo = self.cleaned_data['pseudo']
        
        if commit:
            user.save()
            
            # Join classroom if code provided
            join_code = self.cleaned_data.get('join_code')
            if join_code:
                try:
                    classroom = Classroom.objects.get(join_code=join_code.upper())
                    Enrollment.objects.create(user=user, classroom=classroom)
                except Classroom.DoesNotExist:
                    pass
        
        return user


class TeacherRegistrationForm(UserCreationForm):
    """Registration form for teachers"""
    
    email = forms.EmailField(
        required=True,
        label='Email professionnel',
        widget=forms.EmailInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'})
    )
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label='Prénom',
        widget=forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'})
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label='Nom',
        widget=forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].widget.attrs['class'] = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = User.Role.TEACHER
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
        
        return user


class JoinClassroomForm(forms.Form):
    """Form for students to join a classroom"""
    
    join_code = forms.CharField(
        max_length=6,
        required=True,
        label='Code de classe',
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 uppercase',
            'placeholder': 'ABC123'
        })
    )
    
    def clean_join_code(self):
        code = self.cleaned_data['join_code'].upper()
        if not Classroom.objects.filter(join_code=code).exists():
            raise forms.ValidationError('Code de classe invalide.')
        return code


class ClassroomCreateForm(forms.ModelForm):
    """Form for teachers to create a classroom"""
    
    class Meta:
        model = Classroom
        fields = ['name', 'school_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
            'school_name': forms.TextInput(attrs={'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
        }
        labels = {
            'name': 'Nom de la classe',
            'school_name': 'Établissement',
        }
