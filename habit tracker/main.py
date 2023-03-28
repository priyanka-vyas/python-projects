import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "priyankavyas"
TOKEN = "gfdbijfmoiugwheijkdbfgheridslkhfyurewis"
user_params = {
    "token": "gfdbijfmoiugwheijkdbfgheridslkhfyurewis",
    "username": "priyankavyas",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
GRAPHID = "graph1"
today=datetime(year=2023, month=2,day=26)
post_graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15"
}
post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

response = requests.post(url=post_graph_endpoint, json=post_graph_params,headers=headers)
print(response.text)
