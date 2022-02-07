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


