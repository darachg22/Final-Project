from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Sligo Surf Report Web App"

@app.route('/about')
def about():
    return 'This is the a web application that shows the surf report for the Sligo area.'

@app.route('/Surf Decider')
def contact():
    return 'Contact us for more information.'

@app.route('/Current Surfing Statistics')
def contact():
    return 'Contact us for more information.'


if __name__ == '__main__':
    app.run(debug=True)
