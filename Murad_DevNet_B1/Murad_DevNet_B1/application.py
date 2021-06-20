# Integrating MapQuest API

import urllib.parse
import requests

resource_url1 = "http://www.mapquestapi.com/directions/v2/route?"
resource_url2 = "http://www.mapquestapi.com/directions/v2/routeshape?"
resource_url3 = "http://www.mapquestapi.com/directions/v2/routematrix?"

my_api_key = "rjj8QKl54NcK3XMPKdq05zlfhw3rOrGV"
origin = input("From: ")
destination = input("To: ")

request_url1 = resource_url1 + urllib.parse.urlencode({"key":my_api_key, "from":origin, "to":destination})

response_data1 = requests.get(request_url1).json()

request_url2 = resource_url2 + urllib.parse.urlencode({"key":my_api_key, "sessionId":response_data1["route"]["sessionId"], "mapWidth":320, "mapHeight":240, "mapScale":1733371, "mapLat":40.491304, "mapLng":-77.2614665})
response_data2 = requests.get(request_url2).json()
                                                      
if response_data2["info"]["statuscode"] == 0:
    print("Data For Route Shape\n")
    print("******************************************************************")
    print(response_data2)
    print("******************************************************************")
else:
    print("No Data for Route Shape")
                                                      

request_url3 = resource_url3 + urllib.parse.urlencode({"key":my_api_key})
response_data3 = requests.get(request_url3).json()
if response_data3["info"]["statuscode"] == 0:
    print("Data For Route Shape\n")
    print("******************************************************************")
    print(response_data3)
    print("******************************************************************")
else:
    print("No Data for Route Matrix")




