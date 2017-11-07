from weather import Weather
weather = Weather()

# Lookup via location name.

location = weather.lookup_by_location('Auburn, AL')
condition = location.condition()
astronomy = location.astronomy()
atmosphere = location.atmosphere()
units = location.units()
wind = location.wind()
print ("Date updated: " + condition['date'])
print ("Condition: " + condition['text'])
print ("Temperature: " + condition['temp'] + " degrees Farenheit")
print ("Sunrise: " + astronomy['sunrise'])
print ("Sunset: " + astronomy['sunset'])
print ("Pressure: " + atmosphere['pressure'] + " inches")
print ("Rising: " + atmosphere['rising'])
print ("Visibility: " + atmosphere['visibility'] + " miles")
print ("Humidy: " + atmosphere['humidity'] + " percent")
print ("Wind Direction: " + wind['direction'] + " degrees")
print ("Wind Speed: " + wind['speed'] + " miles per hour")
print ("Wind Chill: " + wind['chill'] + " degrees Farenheit")

forecasts = location.forecast()
for forecast in forecasts:
    print("--------------------")
    print(forecast.date())
    print(forecast.text())
    print("High: " + forecast.high() + " degrees Farenheit")
    print("Low: " + forecast.low() + " degrees Farenheit")
