from flask import Flask, render_template
import requests 

app = Flask(__name__)

#Weather report for App
def weather_forecast(): 

    url = "https://data.gov.ie/dataset/met-eireann-live-text-forecast-data/resource/8350fd63-f6c3-4977-ad16-1dc35fb0972a"
    response = requests.get(url)
    data = response.json()
    return data


@app.route("/")
def index():

    forecast = weather_forecast()
    return render_template("index.html", forecast=forecast)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/statistics')
def statistics():
    return render_template("statistics.html")

if __name__ == '__main__':
    app.run(debug=True)
