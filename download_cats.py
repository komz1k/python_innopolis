import requests

url1 = "https://api.thecatapi.com/v1/images/search?limit=10"

response = requests.get(url1).json()

a = []
for i in range(10):
    a.append(response[i]["url"])

for i in range(10):
    file = open(f"cat{i}.jpg", "wb")
    file.write(requests.get(a[i]).content)
    file.close()