from flask import Flask, jsonify

app = Flask(__name__)

STARTED = False

@app.route('/start/')
def start():
    global STARTED
    STARTED = True
    response = jsonify({'message': 'Hello, World!'})
    response.status_code = 200  # Set the desired status code
    return response
@app.route('/stop/')
def stop():
    global STARTED
    STARTED = False 
    response = jsonify({'message': 'Hello, World!'})
    response.status_code = 200  # Set the desired status code
    return response
@app.route('/check/')
def check():
    global STARTED
    if STARTED == False:
        response = jsonify({'message': 'Hello, World!'})
        response.status_code = 404  # Set the desired status code
        return response
    else:
        response = jsonify({'message': 'Hello, World!'})
        response.status_code = 200  # Set the desired status code
        # STARTED = False
        return response


app.run(debug=True, port=5002)