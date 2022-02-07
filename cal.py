from flask import Flask, json, request

app = Flask(__name__)

#Add two numbers 
@app.route('/add', methods=['POST','OPTIONS'])

def addition():
    # Get the request in JSON format and return None if it fails
    numbers = request.get_json(silent=True)

    # Check the numbers sent via POST
    check = check_numbers(numbers)
    if check == None:
        result = {"result": numbers['n1'] + numbers['n2']}
    else:
        result = {"result": check}
        
    return format_result(result)


#Subtract two numbers
@app.route('/subtract', methods=['POST','OPTIONS'])
def substraction():
    numbers = request.get_json(silent=True)

    check = check_numbers(numbers)
    if check == None:
        result = {"result": numbers['n1'] - numbers['n2']}
    else:
        result = {"result": check}
    
    return format_result(result)

#Divide two numbers 

@app.route('/div', methods=['POST','OPTIONS'])
def division():
    numbers = request.get_json(silent=True)
    
    check = check_numbers(numbers)
    if check == None:
        result = {"result": numbers['n1'] / numbers['n2']}
    else:
        result = {"result": check}
    
    return format_result(result)

# Multiplies two numbers

@app.route('/mult', methods=['POST', 'OPTIONS'])
def multiplication():
    numbers = request.get_json(silent=True)
    
    check = check_numbers(numbers)

    if check == None:
        result = {"result": numbers['n1'] * numbers['n2']}
    else:
        result = {"result": check}
    
    return format_result(result)

