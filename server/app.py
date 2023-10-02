#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter

@app.route("/count/<int:parameter>")
def count(parameter):
    num_list = ""
    for num in range(parameter):
        num_list+= f"{num}" + "\n"
    return num_list

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    num3 = int(num1)
    num4 = int(num2)
  
    if operation == "+":
        result = num3 + num4
        return f"{result}"
    elif operation == "-":
        return f"{num3 - num4}"
    elif operation == "*":
        return f"{num3 * num4}"
    elif operation == "div":
        return f"{num3 / num4}"
    elif operation == "%":
        return f"{num3 % num4}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)