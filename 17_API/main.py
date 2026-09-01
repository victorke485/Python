# API (Application Programming Interface) is set of commands, functions, protocols, and
# objects that programmers can use to create software or interact with an external system.
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# print(response.status_code)

# Response code:
# 1xx - hold on
# 2xx - here you go
# 3xx - go away
# 4xx - you screwed up
# 5xx - i screwed up

response.raise_for_status() # Raise an exception

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
