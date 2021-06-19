
# Integrating MapQuest API

import urllib.parse
import requests

# Mapquest urls
route_url = "http://www.mapquestapi.com/directions/v2/route?"
optimized_url = "http://www.mapquestapi.com/directions/v2/optimizedroute?"
alternate_url = "http://www.mapquestapi.com/directions/v2/alternateroutes?"

# Credentials and search data
my_api_key = "UEq7JEURMWpZFKUhTasybcRGVHT0hhO1"
origin = "Colombo"
destination = "Kandy"

# For route 
request_url = route_url + urllib.parse.urlencode({"key":my_api_key, "from":origin, "to":destination})

response_data = requests.get(request_url).json()

if response_data["info"]["statuscode"] == 0:
    # Print heading 
    print("\n\n**********************************************************\n")
    print("Route\n") 
    # Print total distance
    print("Total Distance: ",response_data["route"]["distance"])
    # Print maneuvers
    for each in response_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str(round(each["distance"]*1.61,2)) + "km)")

    print("\n**********************************************************\n\n")

# For optimized route 
request_url = optimized_url + urllib.parse.urlencode({"key":my_api_key, "from":origin, "to":destination})

response_data = requests.get(request_url).json()

if response_data["info"]["statuscode"] == 0:
    # Print heading 
    print("\n\n**********************************************************\n")
    print("Optimized Route\n") 
    # Print total distance
    print("Total Distance: ",response_data["route"]["distance"])
    # Print maneuvers
    for each in response_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str(round(each["distance"]*1.61,2)) + "km)")
    response_data.clear()
    print("\n**********************************************************\n\n")

# For alternate route 
request_url = alternate_url + urllib.parse.urlencode({"key":my_api_key, "from":origin, "to":destination})

response_data = requests.get(request_url).json()

if response_data["info"]["statuscode"] == 0:
    # Print heading 
    print("\n\n**********************************************************\n")
    print("Alternate Routes\n") 
    # Print total distance
    print("Total Distance: ",response_data["route"]["distance"])
    # Print maneuvers
    for each in response_data["route"]:
        print("\n################################################################")
        print("Another route\n")
        for each in response_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str(round(each["distance"]*1.61,2)) + "km)")

    print("\n**********************************************************\n\n")
