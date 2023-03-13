#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:num>')
def count(num):
    nums = ''
    for n in range(num):
        nums += f'{n}\n'
    return nums

@app.route('/math/<int:num1><string:operator><int:num2>')
def math(num1, operator, num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == 'div':
        return str(num1 / num2)
    elif operator == '%':
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
