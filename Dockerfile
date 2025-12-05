FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=nsi_project.settings_prod

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files (will run during deployment)
RUN python manage.py collectstatic --noinput --clear

# Expose port
EXPOSE 8000

# Start command
CMD python manage.py migrate && gunicorn nsi_project.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120
