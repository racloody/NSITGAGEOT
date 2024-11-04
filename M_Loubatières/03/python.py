import requests
import json

url = 'https://api.openweathermap.org/data/2.5/map'
ville = 'Auch'
appid = '502e08d685626bbcd6a33a146233834e'

reponse = requests.get(f'{url}?q={ville}&appid={appid}')

# Assurez-vous que la réponse est au format JSON
if reponse.status_code == 200:
    # Convertir le contenu JSON de la réponse en dictionnaire Python
    data = reponse.json()
    # Afficher le contenu avec une mise en forme JSON
    print(json.dumps(data, indent=4))
else:
    print