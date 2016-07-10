import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(__file__, '../../../libindic')))
from spellchecker import Malayalam as Spellchecker
from flask import request, render_template
import json

from spellcheckerweb import app


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/api/check/", methods=['GET', 'POST'])
def inflect():
    word = request.args.get('word').strip()
    result = None
    if word:
        mlchecker = Spellchecker()
        result = mlchecker.check_and_generate(word)
        return json.dumps(result)
