from flask import Flask


app = Flask(__name__)
from spellcheckerweb import views
