# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='home'),
    path('home/', views.home, name='home'),
]
