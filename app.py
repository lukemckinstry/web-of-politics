from flask import Flask, url_for, redirect, request
from flask import render_template

import os
from werkzeug.utils import secure_filename



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')