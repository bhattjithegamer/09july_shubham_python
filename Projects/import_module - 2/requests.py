import requests

url = "https://www.youtube.com/watch?v=kc7oVwn1UjU&list=RDkc7oVwn1UjU&index=1"

req = requests.get(url)

data=req.json()

for i in data:
    print(f"Country Name:{i['name']["official"]}")
    print(f"Region:{i['region']}")