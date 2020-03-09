import requests
import json
# import jason

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response.
print(response.status_code)
print (response)

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
# Print the content of the response (the data the server returned)
print(response.content)
data = response.json()
print (type(data))
print (data["number"])
print (data["people"][0]["name"])
print (type(data["people"]))
for key in data["people"]:
    print ("name is {}".format(key["name"]))
for key in data:
    print ("name is {} key is {}".format(data[key], key))
