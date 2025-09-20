import requests
import pandas as pd

url = "https://fakestoreapi.com/products"

req = requests.get(url)
data = req.json()
a = pd.DataFrame(data)
print(a)
