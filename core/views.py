# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest

def root(_: WSGIRequest) -> HttpResponse:
    return HttpResponse("Hallo!")

def home(_: WSGIRequest) -> HttpResponse:
    return redirect("/")
