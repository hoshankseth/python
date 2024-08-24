import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/commits")
print(response)
output = response.json()
print("Name:- " + output[0]["commit"]["author"]["name"] + " Email:- " +  output[0]["commit"]["author"]["email"])

#test=200
for i in range(len(output)):
    print("Name:- " + output[i]["commit"]["author"]["name"] + " Email:- " +  output[i]["commit"]["author"]["email"])
