import requests

api_key = "1ab3a5f55b954b848b692717210807"
city = str(input("Enter a city name to see the weather information: ")).lower()
print("")

url = "https://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=yes".format(api_key, city)

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Here are the location details for the given city: ")
    print("")
    print("The place you are looking for is {}.".format(data["location"]["name"]))
    print("The place {} belongs to the state {} which is located in {}.".format(data["location"]["name"], data["location"]["region"], data["location"]["country"]))
    print("The latitude and longitude of {} is {}, {}.".format(data["location"]["name"], data["location"]["lat"], data["location"]["lon"]))
    print("The time zone of the place {} is {}.".format(data["location"]["name"], data["location"]["tz_id"]))
    date, time = data["location"]["localtime"].split()
    print("The current date at {} is {} which is in the format of YYYY-MM-DD.".format(data["location"]["name"], date))
    print("The current time at {} is {} which is in the 24 hours format.".format(data["location"]["name"], time))
    print("")

    print("Here are the weather information for the given city: ")
    print("")
    print("Temperature of {} in celsius is {}C and feels like {}C".format(data["location"]["name"], data["current"]["temp_c"], data["current"]["feelslike_c"]))
    print("Temperature of {} in farenheit is {}F and feels like {}F".format(data["location"]["name"], data["current"]["temp_f"], data["current"]["feelslike_f"]))
    print("Now the place {} has a weather condition of {}.".format(data["location"]["name"], data["current"]["condition"]["text"]))
    wind_direction_dict = {"N" : "North",
                           "S" : "South",
                           "E" : "East",
                           "W" : "West",
                           "NE" : "North East",
                           "NW" : "North West",
                           "SE" : "South East",
                           "SW" : "South West",
                           "WNW" : "West-North West", 
                           "NNW" : "North-North West",
                           "NNE" : "North-North East",
                           "ENE" : "East-North East",
                           "ESE" : "East-South East",
                           "SSE" : "South-South East",
                           "SSW" : "South-South West", 
                           "WSW" : "West-South West"}
    print("The current wind direction in {} is {}.".format(data["location"]["name"], wind_direction_dict[str(data["current"]["wind_dir"])]))
    print("The current wind speed in {} is {} Miles per Hour.".format(data["location"]["name"], data["current"]["wind_mph"]))
    print("The current wind speed in {} is {} Kilometer per Hour.".format(data["location"]["name"], data["current"]["wind_kph"]))
    print("The current wind direction in {} is {} Degree.".format(data["location"]["name"], data["current"]["wind_degree"]))
    print("The current humidity in {} is {}.".format(data["location"]["name"], data["current"]["humidity"]))
    uv_index = int(data["current"]["uv"])
    if uv_index >= 1 and uv_index < 3:
        print("The UV radiation in {} is {}, which is {}.".format(data["location"]["name"], uv_index, "Low"))
    elif uv_index >= 3 and uv_index < 6:
        print("The UV radiation in {} is {}, which is {}.".format(data["location"]["name"], uv_index, "Moderate"))
    elif uv_index >= 6 and uv_index < 8:
        print("The UV radiation in {} is {}, which is {}.".format(data["location"]["name"], uv_index, "High"))
    elif uv_index >= 8 and uv_index > 11:
        print("The UV radiation in {} is {}, which is {}.".format(data["location"]["name"], uv_index, "Very High"))
    else:
        print("The UV radiation in {} is {}, which is {}.".format(data["location"]["name"], uv_index, "Extreme"))
    print("The air pressure in {} is {} in millibars and {} in inches.".format(data["location"]["name"], data["current"]["pressure_mb"], data["current"]["pressure_in"]))
    print("The air percipitation in {} is {} in millmeters and {} in inches.".format(data["location"]["name"], data["current"]["precip_mm"], data["current"]["precip_in"]))
    print("The cloud coverage in {} at present is {} percentage.".format(data["location"]["name"], data["current"]["cloud"]))
    print("The {} has visibility of {} kilometer and {} miles".format(data["location"]["name"], data["current"]["vis_km"], data["current"]["vis_miles"]))
    print("The wind gust in {} is {} kilometer per hour and {} miles per hour.".format(data["location"]["name"], data["current"]["gust_kph"], data["current"]["gust_mph"]))
    print("")

    print("Here are the air quality details for the given city: ")
    print("")
    print("The carbon monoxide present in the air in {} is {} micro-gram per cubic meter.".format(data["location"]["name"], data["current"]["air_quality"]["co"]))
    print("The nitrogen dioxide present in the air in {} is {} micro-gram per cubic meter.".format(data["location"]["name"], data["current"]["air_quality"]["no2"]))
    print("The ozone present in the air in {} is {} micro-gram per cubic meter.".format(data["location"]["name"], data["current"]["air_quality"]["o3"]))
    print("The sulphur dioxide present in the air in {} is {} micro-gram per cubic meter.".format(data["location"]["name"], data["current"]["air_quality"]["so2"]))
    print("The particulate matter 2.5 (PM 2.5) present in the air in {} is {} micro-gram per cubic meter.".format(data["location"]["name"], data["current"]["air_quality"]["pm2_5"]))
    print("The particulate matter 10 (PM 10) present in the air in {} is {} micro-gram per cubic meter.".format(data["location"]["name"], data["current"]["air_quality"]["pm10"]))
    us_index_dict = {1 : "Good",
                     2 : "Moderate",
                     3 : "Unhealthy for sensitive group",
                     4 : "Unhealthy",
                     5 : "Very unhealthy",
                     6: "Hazardous"}
    print("The air quality in {} is {} according to US-EPA-Index".format(data["location"]["name"], us_index_dict[int(data["current"]["air_quality"]["us-epa-index"])]))
    uk_index_dict = {1 : "Low",
                     2 : "Low",
                     3 : "Low",
                     4 : "Moderate",
                     5 : "Moderate",
                     6 : "Moderate",
                     7 : "High",
                     8 : "High",
                     9 : "High",
                     10 : "Very High"}
    print("The air quality in {} is {} according to UK-DEFRA-Index".format(data["location"]["name"], uk_index_dict[int(data["current"]["air_quality"]["gb-defra-index"])]))
    print("")

    astronomy_url = "https://api.weatherapi.com/v1/astronomy.json?key={}&q={}&dt={}".format(api_key, city, date)
    astro_response = requests.get(astronomy_url)
    astro_data = astro_response.json()
    astronomy = astro_data["astronomy"]["astro"]
    print("Here are the astronomy details for the given city: ")
    print("")
    print("The sun rises in {} at the time of {}.".format(data["location"]["name"], astronomy["sunrise"]))
    print("The sun set in {} at the time of {}.".format(data["location"]["name"], astronomy["sunset"]))
    print("The moon rises in {} at the time of {}.".format(data["location"]["name"], astronomy["moonrise"]))
    print("The moon set in {} at the time of {}.".format(data["location"]["name"], astronomy["moonset"]))
    print("Today the moon phase is {} in {}.".format(astronomy["moon_phase"], data["location"]["name"]))
    print("The moon illumination in {} is {} percentage".format(data["location"]["name"], astronomy["moon_illumination"]))
    print("")

else:
    print("Can't able to fetch the data. Check that the given city name is correct or check for stable internet connection.")