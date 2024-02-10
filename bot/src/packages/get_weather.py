import requests
import discord

class WeatherInfo():

    def __init__ (self, client):
        self.client = client
        self.weather_api_url = "https://weather.tsukumijima.net/api/forecast"
        self.city_id_map = {
            "Tokyo": "130010",
            "Kanagawa": "140010",
        }

    async def check_rain(self):
        weather_data = self.get_weather("Tokyo")
        today_weather = weather_data["forecasts"][0]["telop"]
        # if ("雨" in today_weather):
        await self.send_weather_details(weather_data)
            

    def get_weather(self, city_name):
        access_url = self.weather_api_url + self.set_weather_query(city_name)
        weather_data = requests.get(access_url).json()
        return weather_data

    def set_weather_query(self, city):
        city_id = self.city_id_map[city]
        return "?city=" + city_id
    
    async def send_weather_details(self, weather_data):
        today_weather_embed = discord.Embed(title=weather_data["title"],
                                            color=0x00ff00,
                                            url="https://weather.yahoo.co.jp/weather/jp/13/4410.html"
                                            )
        today_weather_embed.set_image(url=weather_data["forecasts"][0]["image"]["url"])
        today_weather_embed.add_field(name=weather_data["forecasts"][0]["telop"],
                                      value=weather_data["forecasts"][0]["detail"]["weather"])
        today_weather_embed.set_footer(text="made by koto74")
        channel = self.client.get_channel(1203047813131542628)
        await channel.send(embed=today_weather_embed)

