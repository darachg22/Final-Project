from flask import Flask, render_template
import requests 

app = Flask(__name__)

#Weather report for App
def weather_forecast(): 
    url = "https://www.met.ie/Open_Data/json/National.json"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/NationalWeather')
def about():
    forecast = weather_forecast()
    return render_template("NationalWeather.html", forecast=forecast)

@app.route('/SligoWeather')
def contact():
    return render_template("SligoWeather.html")

@app.route('/SurfStrandhill')
def strandhill():
    return render_template("SurfStrandhill.html")

@app.route('/SurfDunmoran')
def surf_dunmoran():
    return render_template("SurfDunmoran.html")

@app.route('/SurfEaskey')
def surf_easkey():
    return render_template("SurfEaskey.html")

if __name__ == '__main__':
    app.run(debug=True)
