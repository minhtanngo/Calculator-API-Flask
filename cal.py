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


def check_numbers(numbers):
    """
    - Numbers should be a dictionary (JSON), Length = 2, keys 'n1' and 'n2'.
    - Returns None if all conditions are met, otherwise returns an error message.
    """
    
    if numbers == None:
        return "Please POST two numbers to use this API with format {\"n1\":<number>, \"n2\":<number>}"
    if len(numbers) != 2:
        return "Only 2 numbers are allowed"
    if 'n1' not in numbers or 'n2' not in numbers:
        return "The JSON POST data should have format {\"n1\":<number>, \"n2\":<number>}"

    return None

def format_result(result):
    """
    - Formats the result 
    - Turn it into JSON format
    """
    # Turns result into a response object, with JSON data
    result = json.jsonify(result)    
    
    # Add CORS headers to response
    result.headers.add('Access-Control-Allow-Headers', 'content-type')
    result.headers.add('Access-Control-Allow-Origin', '*')

    return result

if __name__ == '__main__':
    app.run(debug=True)