# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

# Use a base Python docker image
FROM python:3.12.10-bookworm

# Set the working directory to app
WORKDIR /app

# Copy necessary folders
COPY hongkongukah/ hongkongukah/
COPY core/ core/
# COPY static/ static/
# COPY .env .env
COPY manage.py manage.py

# Install Python app dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

# Expose port for gunicorn
EXPOSE 8000

# Start gunicorn and serve website
CMD ["gunicorn", "--workers=3", "-k", "eventlet", "-b", "0.0.0.0:8000", "hongkongukah.wsgi"]
