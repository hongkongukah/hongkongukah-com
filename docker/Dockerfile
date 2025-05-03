# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

# Use a base Python docker image
FROM python:3.12.10-bookworm

# Set the working directory to app
WORKDIR /app

# Copy necessary folders
COPY hongkongukah/ hongkongukah/

# Install Python app dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose port for gunicorn
EXPOSE 8000

# Copy environment file
COPY .env .env

# Start gunicorn and serve website
CMD ["gunicorn", "--workers=3", "-k", "eventlet", "-b", "0.0.0.0:8000", "hongkongukah.wsgi"]
