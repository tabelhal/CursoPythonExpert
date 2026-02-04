import requests
import geocoder

#b7256228f73ed0b4b063df5a01f3efa7
#86b49b06bf5482d98a9f540754b726c5

API_KEY = "b7256228f73ed0b4b063df5a01f3efa7"

g = geocoder.ip('me')

lat, lon = g.latlng

url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=pt_br"
)

response = requests.get(url)
dados = response.json()

if response.status_code == 200:
    cidade = dados["name"]
    temperatura = dados["main"]["temp"]
    condicao = dados["weather"][0]["description"]

    print(f"📍 Cidade: {cidade}")
    print(f"🌡️ Temperatura: {temperatura}°C")
    print(f"☁️ Condição do tempo: {condicao}")
else:
    print("❌ Erro ao obter o clima:")
    print(dados)
