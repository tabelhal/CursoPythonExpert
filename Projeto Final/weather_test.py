# pip install python-weather
import python_weather
import asyncio


async def get_weather():
    # 'unit=IMPERIAL' para Fahrenheit ou 'unit=METRIC' para Celsius
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # Substitua 'Lisbon' pela sua cidade
        weather = await client.get('Lisbon')
        TRANSLATIONS_PT = {
            "Sunny": "Ensolarado",
            "Clear": "Céu limpo",
            "Partly cloudy": "Parcialmente nublado",
            "Cloudy": "Nublado",
            "Overcast": "Encoberto",
            "Rain": "Chuva",
            "Light rain": "Chuva fraca",
            "Heavy rain": "Chuva forte",
            "Thunderstorm": "Trovoada",
            "Snow": "Neve",
            "Fog": "Nevoeiro",
            "Mist": "Névoa",
        }

        description_en = weather.description
        description_pt = TRANSLATIONS_PT.get(description_en, description_en)

        print(f"Temperatura atual: {weather.temperature}°C")
        print(f"Condição: {description_pt}")

if __name__ == '__main__':
    asyncio.run(get_weather())
