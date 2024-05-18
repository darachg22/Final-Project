from flask import Flask, render_template, url_for
import requests
import pandas as pd 

app = Flask(__name__)

def weather_forecast():
    url = "https://www.met.ie/Open_Data/json/National.json"
    response = requests.get(url)
    data = response.json()
    return data

def wave_forecast_data():
    url = "http://erddap.marine.ie/erddap/tabledap/IMI-WaveBuoyForecast.json?time,longitude,latitude,stationID,significant_wave_height,mean_wave_period,mean_wave_direction,wave_power_per_unit_crest_length,peak_period,energy_period&stationID=M4"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/NationalWeather')
def national_weather():
    forecast = weather_forecast()
    return render_template("NationalWeather.html", forecast=forecast)

@app.route('/SligoWeather')
def sligo_weather():
    return render_template("SligoWeather.html")

@app.route('/SurfStrandhill')
def surf_strandhill():
    return render_template("SurfStrandhill.html")

@app.route('/SurfDunmoran')
def surf_dunmoran():
    return render_template("SurfDunmoran.html")

@app.route('/SurfEaskey')
def surf_easkey():
    return render_template("SurfEaskey.html")

@app.route("/buoy_m4")
def buoy_m4():
    wave_data = wave_forecast_data()
    return render_template("buoy_m4.html", wave_data=wave_data)

if __name__ == '__main__':
    app.run(debug=True)
