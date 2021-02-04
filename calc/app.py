from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_page():
    """returns the sum of the query parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{add(a,b)}"

@app.route('/sub')
def sub_page():
    """returns the different between the query parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{sub(a,b)}"

@app.route('/mult')
def mult_page():
    """returns the product of the query parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{mult(a,b)}"

@app.route('/div')
def div_page():
    """returns the quotient the query parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{div(a,b)}"

@app.route('/math/<op>')
def all_math(op):
    """returns the result of the specified operation on the query parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    func = { 'add': add, 'sub': sub, 'mult': mult, 'div': div}
    result = func[op](a, b)
    return str(result)
