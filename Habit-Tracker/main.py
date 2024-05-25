from datetime import datetime
import requests

USERNAME = "__USERNAME__" # choose a unique username
TOKEN = "__YOUR_TOKEN__" # create a random token consists of chars & nums
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "__GRAPH_NAME__" # choose a graph name eg graph1

# creates a user in pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# creates a new graph
today = datetime.now()
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora" # it means blue in japanese
}

# header required for one of the auth type
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# to update the existing graph
graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_update_config = {
    "unit": "hours"
}

response = requests.put(url=graph_update_endpoint, json=graph_update_config, headers=headers)
print(response.text)

# to create a new pixel for today
create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours felt productive for you today?"),
}

response = requests.post(url=create_endpoint, json=pixel_config, headers=headers)
print(response.text)

# updates any existing day's pixel value 
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240524"
update_config = {
    "quantity": "Any previous updates?",
}

response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

# deletes existing pixel specifiec in date
delete_date = input("Which date you wanna cleared?(format: yyyymmdd : ") 
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
