#!/usr/bin/env python
import os
import sys
import subprocess

def run_command(cmd):
    print(f"\n{'='*60}")
    print(f"Running: {cmd}")
    print('='*60)
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"ERROR: Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)
    return result

if __name__ == "__main__":
    run_command("python manage.py migrate --noinput")

    if os.environ.get('DJANGO_SUPERUSER_USERNAME'):
        print("\nCreating/updating superuser...")
        result = subprocess.run(
            ["python", "manage.py", "shell", "-c",
             "from accounts.models import User; username = '{}'; email = '{}'; password = '{}'; user, created = User.objects.get_or_create(username=username, defaults={{'email': email, 'is_student': False, 'is_teacher': True}}); user.set_password(password); user.is_superuser = True; user.is_staff = True; user.is_student = False; user.is_teacher = True; user.save(); print('Superuser ready')".format(
                 os.environ.get('DJANGO_SUPERUSER_USERNAME'),
                 os.environ.get('DJANGO_SUPERUSER_EMAIL'),
                 os.environ.get('DJANGO_SUPERUSER_PASSWORD'))],
            capture_output=True, text=True)
        if result.stdout: print(result.stdout)

    print("\nCreating course content...")
    subprocess.run(["python", "manage.py", "create_snt_content", "--clean"], capture_output=True, text=True)

    print("\nPopulating Python content...")
    subprocess.run(["python", "manage.py", "populate_python_content"], capture_output=True, text=True)
    print("\nInitializing gamification...")
    subprocess.run(["python", "manage.py", "init_gamification"], capture_output=True, text=True)

    snt_commands = ["populate_snt_internet", "populate_snt_web", "populate_snt_donnees", "populate_snt_reseaux_sociaux", "populate_snt_photo", "populate_snt_localisation"]
    for cmd in snt_commands:
        print(f"\nPopulating {cmd}...")
        subprocess.run(["python", "manage.py", cmd], capture_output=True, text=True)

    nsi_commands = ["populate_nsi_python", "populate_nsi_algorithmique", "populate_nsi_representation", "populate_nsi_web", "populate_nsi_traitement_donnees", "populate_nsi_architecture", "populate_nsi_reseaux"]
    for cmd in nsi_commands:
        print(f"\nPopulating {cmd}...")
        subprocess.run(["python", "manage.py", cmd], capture_output=True, text=True)

    run_command("python manage.py collectstatic --noinput --clear")

    port = os.environ.get('PORT', '8000')
    workers = os.environ.get('WEB_CONCURRENCY', '3')
    print(f"\nStarting Gunicorn on port {port} with {workers} workers...")
    os.execvp("gunicorn", ["gunicorn", "nsi_project.wsgi:application", "--bind", f"0.0.0.0:{port}", "--workers", workers, "--timeout", "120", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info"])

