# Calculator-API-Flask
Addition, subtraction, division and multiplication of two numbers 

## App structure 
- cal.py: includes 4 endpoints, explain in [Endpoints](##endpoints) section
- cal_eval.py: includes only 1 endpoint, explain in [Endpoints](##endpoints) section

## Getting started 
### Prerequisites 
To run this project, an environment with [Python 3.7](https://wiki.python.org/moin/BeginnersGuide/Download) and [Flask](http://flask.pocoo.org/docs/1.0/installation/#installation) is required

## Using this project 
### Clone the repo 
```
git clone https://github.com/minhtanngo/Calculator-API-Flask.git
``` 

Access the project directory 
``` 
cd Calculator-API-Flask
``` 

Inside the project directory, execute the following: 
- To use the cal.py 
```
set FLASK_APP=cal.py 
flask run
```
- To use the cal_eval.py
```
set FLASK_APP=cal_eval.py 
flask run
```

You should see something like this if you configured correctly:
```
 * Serving Flask app "cal.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

 ## Endpoints 
 The webservice has the following endpoints: 
 - Add two numbers and return the result
 ```
POST: /add
 ```
 - Subtract two numbers and return the result
 ```
POST: /sub
 ```
 - Divide two numbers and return the result
 ```
POST: /div
 ```
 - Multiply two numbers and return the result
 ```
POST: /mult
 ```

The endpoints can be tested with the following body and URLs: 
```
POST Body:
{"n1":5, "n2":10}

URLs:
http://localhost:5000/add
http://localhost:5000/sub
http://localhost:5000/div
http://localhost:5000/mult
```
