from script import convert_decimal_to_digital

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
