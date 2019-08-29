import requests
data = {"commentaire":"ce produit est nul"}
res = requests.post('http://127.0.0.1:5000/commentaire_json', json=data)
print(data["commentaire"])
print(res.text)
data = {"commentaire":"ce produit est top"}
res = requests.post('http://127.0.0.1:5000/commentaire_json', json=data)
print(data["commentaire"])
print(res.text)