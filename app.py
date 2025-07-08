from script import convert_decimal_to_digital

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    decimal = request.args.get('decimal')
    digital = convert_decimal_to_digital(decimal)
    return digital
