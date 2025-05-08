FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=cv_project.settings

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Run migrations and collect static files when the container launches
RUN mkdir -p /app/static /app/media

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cv_project.wsgi:application"]