# pip install python-weather
import python_weather
import asyncio

async def get_weather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get('Lisbon')
        print(f"Temperatura atual: {weather.temperature}°C")
        print(f"Condição: {weather.description}")

if __name__ == '__main__':
    asyncio.run(get_weather())
