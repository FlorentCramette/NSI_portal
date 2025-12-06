#!/usr/bin/env python
import os
import sys
import subprocess

def run_command(cmd):
    """Run a command and exit if it fails"""
    print(f"\n{'='*60}")
    print(f"Running: {cmd}")
    print('='*60)
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"ERROR: Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)
    return result

if __name__ == "__main__":
    # Run migrations
    run_command("python manage.py migrate --noinput")

    # Create superuser if it doesn't exist
    if os.environ.get('DJANGO_SUPERUSER_USERNAME'):
        print("\nCreating/updating superuser...")
        # Use Django management command with proper environment
        result = subprocess.run(
            [
                "python", "manage.py", "shell", "-c",
                """
from accounts.models import User
username = '{username}'
email = '{email}'
password = '{password}'

user, created = User.objects.get_or_create(
    username=username,
    defaults={{'email': email, 'is_student': False, 'is_teacher': True}}
)
if created:
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    print('✅ Superuser created successfully')
else:
    # Update existing user to ensure it's a superuser
    user.is_superuser = True
    user.is_staff = True
    user.is_student = False
    user.is_teacher = True
    user.set_password(password)
    user.save()
    print('✅ Superuser updated successfully')
                """.format(
                    username=os.environ.get('DJANGO_SUPERUSER_USERNAME'),
                    email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
                    password=os.environ.get('DJANGO_SUPERUSER_PASSWORD')
                )
            ],
            capture_output=True,
            text=True
        )
        if result.stdout:
            print(result.stdout)
        if result.returncode != 0 and result.stderr:
            print(f"⚠️ Superuser creation warning: {result.stderr}")

    # Create initial course content
    print("\nCreating course content...")
    result = subprocess.run(
        ["python", "manage.py", "create_snt_content"],
        capture_output=True,
        text=True
    )
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0 and result.stderr:
        print(f"⚠️ Course creation warning: {result.stderr}")

    # Collect static files
    print("\nCollecting static files...")
    run_command("python manage.py collectstatic --noinput --clear")

    # Start Gunicorn
    port = os.environ.get('PORT', '8000')
    workers = os.environ.get('WEB_CONCURRENCY', '3')

    print(f"\nStarting Gunicorn on port {port} with {workers} workers...")
    gunicorn_cmd = [
        "gunicorn",
        "nsi_project.wsgi:application",
        "--bind", f"0.0.0.0:{port}",
        "--workers", workers,
        "--timeout", "120",
        "--access-logfile", "-",
        "--error-logfile", "-",
        "--log-level", "info"
    ]
    os.execvp("gunicorn", gunicorn_cmd)
