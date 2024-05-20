# Final-Project
My project for the Web Services and Applications module. This repository contains all the files necessary to fit the brief given for project choice B. 

## Weather and Wave Data Web Application

### Overview
This Flask-based web application provides real-time weather and wave data. It includes a RESTful API for retrieving buoy data and dynamic web pages using AJAX to display the data.

### Features
- RESTful API to fetch buoy M4 data
- Displays weather data from Met Éireann
- Fetches wave data from Marine Institute's ERDDAP service

### Requirements
- Python 3
- Flask
- pandas
- requests

### Setup

1. Install dependencies:
    pip install flask pandas requests

2. Run the Flask app:
 python Final-Project.py
   

### Project Structure
- `Final-Project.py`: Main Flask application file
- `templates/`: HTML templates
  - `index.html`: Home page
  - `NationalWeather.html`: National weather data page
  - `SligoWeather.html`: Sligo weather data page
  - `BuoyM4.html`: Buoy M4 data page
  - `SurfDunmoran.html`: Widget to show surfing conditions in Dunmoran
  - `SurfEaskey.html`: Widget to show surfing conditions in Easkey
  - `SurfStrandhill.html`: Widget to show surfing conditions in Strandhill
- `static/Images`: Static image files
- `References`: A document containing all the links to the skeleton codes needed to complete this project

### Usage
1. Open your web browser at `http://127.0.0.1:5000`.
2. Navigate to different sections using the menu:
    - National Weather: Displays national weather forecast
    - Sligo Weather: Displays weather data for Sligo
    - SurfDunmoran: Shows surfing conditions in Dunmoran
    - SurfEaskey: Shows surfing conditions in Easkey
    - SurfStrandhill: Shows surfing conditions in Strandhill
    - Buoy M4 Data: Shows the latest wave data from buoy M4, which is the main buoy serving Sligo
3. Each page has a home button to return to main page. 

