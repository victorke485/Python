import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

token = os.getenv("pixela_token")

# Creating user account
url = "https://pixe.la/v1/users"
user_parameters = {
    "token": token,
    "username": "victor5678",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=url, json=user_parameters)
print(response.text)

# Creating graph
graph_url = "https://pixe.la/v1/users/victor5678/graphs"
request_header = {
    "X-USER-TOKEN": token,
}
graph_config = {
    "id": "graph1",
    "name": "Coding Tracker",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

# response = requests.post(url=graph_url, headers=request_header, json=graph_config)
# print(response.text)

# Adding information to a graph
graph_url = "https://pixe.la/v1/users/victor5678/graphs/graph1"
request_header = {
    "X-USER-TOKEN": token,
}
graph_information = {"date": "20260512", "quantity": "12"}
# response = requests.post(url=graph_url, headers=request_header, json=graph_information)
# print(response.text)
