# Put your app in here.

from flask import Flask, request
import operations as ops

app = Flask(__name__)  # creating an instance of the Flask Class

@app.route('/<math>')
def calculate(math):
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    if math == 'add':
        return str(ops.add(a,b))
    elif math == 'sub':
        return str(ops.sub(a,b))
    elif math == 'mult':
        return str(ops.mult(a,b))
    elif math == 'div':
        return str(ops.div(a,b))
    else:
        return "There was an error."
    
@app.route('/math/<oper>') # note: arguments are not referenced here
def do_math(oper):          # reference oper here to capture the path
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    # Create a function dictionary
    equation = {             # note: the functions are not strings
        'add':ops.add, 
        'sub':ops.sub, 
        'mult':ops.mult, 
        'div':ops.div}
    
    if oper in equation:
        return str(equation[oper](a,b))     # note: calling the dictionary value will execute the function
    else:
        return f'That calculation ({oper}) was not found.'