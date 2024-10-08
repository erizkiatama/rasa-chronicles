# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migration files
RUN python manage.py migrate

# Run the Django development server
CMD ["sh", "-c", "gunicorn rasa_chronicles.wsgi:application --bind 0.0.0.0:8000"]
