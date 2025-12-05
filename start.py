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
    
    # Collect static files
    print("\nCollecting static files...")
    run_command("python manage.py collectstatic --noinput --clear")
    
    # Start Gunicorn
    port = os.environ.get('PORT', '8000')
    workers = os.environ.get('WEB_CONCURRENCY', '3')
    
    print(f"\nStarting Gunicorn on port {port} with {workers} workers...")
    gunicorn_cmd = (
        f"gunicorn nsi_project.wsgi:application "
        f"--bind 0.0.0.0:{port} "
        f"--workers {workers} "
        f"--timeout 120 "
        f"--access-logfile - "
        f"--error-logfile - "
        f"--log-level info"
    )
    os.execvp("gunicorn", gunicorn_cmd.split())
