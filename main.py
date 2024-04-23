import requests

# Pixela_API
pixela_api = "https://pixe.la/v1/users"
parameters = {
    "token":"fjdshkjfh6768327jhdf8w7ehj",
    "username":"niravpatel6656",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url=pixela_api,json=parameters)

# Graph_API
graph_api = "https://pixe.la/v1/users/niravpatel6656/graphs"
graph_header = {
    "X-USER-TOKEN":"fjdshkjfh6768327jhdf8w7ehj"
}

graph_parameters = {
    "id":"niravtest",
    "name":"gym_graph",
    "unit":"km",
    "type":"float",
    "color":"momiji"
}
graph_response = requests.post(url=graph_api,json=graph_parameters,headers=graph_header)

# Pixel_API
post_pixel_api = "https://pixe.la/v1/users/niravpatel6656/graphs/niravtest"

post_pixel_parameters = {
    "date": "20240420",
    "quantity": "30.0"
}
post_pixel_response = requests.post(url=post_pixel_api,headers=graph_header,json=post_pixel_parameters)

print(post_pixel_response.text)
