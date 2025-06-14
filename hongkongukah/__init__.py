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