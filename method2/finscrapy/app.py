#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for
import config

app = Flask('fintech', static_folder='./static', template_folder='./applications/templates')
app.config.from_object(config)

def register_blueprints():
    from applications.initial import index
    app.register_blueprint(index)

register_blueprints()

@app.route('/')
def index():
    return redirect(url_for('index.initial'))