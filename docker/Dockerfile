# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

# Use a base Python docker image
FROM ghcr.io/astral-sh/uv:python3.13-alpine

# Set the working directory to app
WORKDIR /app

# Copy necessary folders
COPY hongkongukah/ hongkongukah/
COPY pyproject.toml pyproject.toml

# Install dependencies
RUN uv pip install --system .

# Expose port for gunicorn
EXPOSE 8000

# Start gunicorn and serve website
CMD ["gunicorn", "--workers=3", "-k", "eventlet", "-b", "0.0.0.0:8000", "hongkongukah:app"]
