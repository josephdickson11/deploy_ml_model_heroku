from flask import Flask, render_template


# name of flask app
app = Flask(__name__)


# run the server
# this line of code is not needed when running the flask run command in terminal
# app.run(debug= True)

# defining static app routes

@app.route("/", methods=['GET', 'POST', 'PUT'])  # decorator
def home():  # route handler function
    # returning a response
    return render_template('index.html', name = 'Joseph', gender = 'male')
