import requests

class Weather:
  def tempWeek():
    api_url = "https://api.weather.gov/points/40.7,-73.9"
    r = requests.get(api_url)

    api_url_forecast = "https://api.weather.gov/gridpoints/OKX/36,34/forecast"
    req = requests.get(api_url_forecast)
    info = req.json()

    properties = info['properties']
    periods = properties['periods']

    today = periods[0]

    temp = today['temperature']
    wind = today['windSpeed']

    windNum = wind[0:1]

    forecast = today["shortForecast"]
    
    return([temp,windNum,forecast])
    #return(windNum)

    
    
  tempWeek()
    
    