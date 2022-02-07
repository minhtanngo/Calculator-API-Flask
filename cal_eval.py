from flask import Flask, request, json 
import re 

app = Flask(__name__)

#Add 2 numbers and return the result 
@app.route('/calc', methods = ['POST', 'OPTIONS'])

def cal():
    if request.method == 'OPTIONS':
        return format_result({"result" : 0})
    
    exp_json = request.get_json(silent=True)

    #Check if the json request has the key expression
    if "expression" not in exp_json:
        return format_result("result": "You have to post an expression to use this API")

    #Get the expression string from the dict 
    exp = exp_json['expression']

    #Check if expression is correct 
    check = check_expression(exp)

    #if no errors, evaluates the expression 
    if check == None:
        result = {"result" : eval(exp)}
    else:
        result = {"result" : check}

    return format_result(result)