# SPDX-FileCopyrightText: 2025 HongKongukah.com
# SPDX-License-Identifier: MIT

from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def index() -> str:
    """Route for the index (landing page)."""
    return render_template("index.html")

@app.route("/about")
def about() -> str:
    """Route for the about page."""
    return render_template("about.html")

@app.route("/bingo")
def bingo() -> str:
    """Route for the bingo card page."""
    return render_template("bingo.html")

@app.route("/charity")
def charity() -> str:
    """Route for the charity information page."""
    return render_template("charity.html")

