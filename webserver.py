from flask import Flask
from flask import request

import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    info = json.loads(request.data)
    return "{a:1}"