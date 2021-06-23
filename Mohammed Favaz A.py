import requests

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

store = open('weather.txt','w')

store.write ("-------------------------------------------------------------\n")
store.write ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
store.write ("\n-------------------------------------------------------------")

store.write ("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
store.write("\nCurrent weather desc  :")
store.write(weather_desc)
store.write ("\nCurrent Humidity      :")
store.write(str(hmdt))
store.write('%')
store.write ("\nCurrent wind speed    :")
store.write(str(wind_spd))
store.write('kmph')
store.close()