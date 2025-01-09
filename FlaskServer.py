from flask import Flask # import Flask class to create web application

app = Flask(__name__) # creates an instance of the Flask class

@app.route("/ask", methods=['POST']) # define url-endpoint that only handles POST requests
def ask():

