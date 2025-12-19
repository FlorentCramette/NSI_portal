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
    workers = int(os.environ.get('WEB_CONCURRENCY', '4'))  # 2*CPU+1 recommandé
    threads = int(os.environ.get('GUNICORN_THREADS', '2'))
    worker_connections = 1000
    max_requests = 1000
    max_requests_jitter = 50
    keepalive = 5
    
    print(f"\nStarting Gunicorn on port {port}")
    print(f"Workers: {workers}, Threads: {threads}, Worker connections: {worker_connections}")
    
    os.execvp("gunicorn", [
        "gunicorn",
        "nsi_project.wsgi:application",
        "--bind", f"0.0.0.0:{port}",
        "--workers", str(workers),
        "--worker-class", "gthread",
        "--threads", str(threads),
        "--worker-connections", str(worker_connections),
        "--max-requests", str(max_requests),
        "--max-requests-jitter", str(max_requests_jitter),
        "--keepalive", str(keepalive),
        "--timeout", "120",
        "--graceful-timeout", "30",
        "--access-logfile", "/dev/null",  # Disable access logs to avoid Railway rate limit
        "--error-logfile", "-",
        "--log-level", "warning"  # Only log warnings and errors
    ])

