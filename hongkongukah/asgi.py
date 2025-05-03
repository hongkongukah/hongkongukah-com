# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

"""
ASGI config for hongkongukah project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongkongukah.settings')

application = get_asgi_application()
