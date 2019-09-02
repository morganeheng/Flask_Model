import requests
import sys

if len(sys.argv) < 2:
	print("il faut entrer au moins un commentaire")
	print('exemple : python test_web_service.py "ce produit est nul"')

for i in range(1, len(sys.argv)):
    data = {"commentaire":sys.argv[i]}
    res = requests.post('http://127.0.0.1:5000/commentaire_json', json=data)
    print(data["commentaire"])
    print(res.text)