import requests
import discord

class WeatherInfo():

    def __init__ (self, client):
        self.client = client
        self.weather_api_url = "https://weather.tsukumijima.net/api/forecast"
        self.city_id_map = {
            "東京": "130010",
            "神奈川": "140010",
        }

    async def send_rain_alert(self, send_channel_id):
        for city in self.city_id_map.keys():
            weather_data = self.get_weather(city)
            if (weather_data is None):
                return
            today_weather = weather_data["forecasts"][0]["telop"]
            if ("雨" in today_weather):
                await self.send_rain_weather_details(weather_data, city, send_channel_id) 

    def get_weather(self, city_name):
        access_url = self.weather_api_url + self.set_weather_query(city_name)
        try:
            weather_data = requests.get(access_url).json()
        except requests.exceptions.RequestException as e:
            print(e)
            return None
        return weather_data

    def set_weather_query(self, city):
        city_id = self.city_id_map[city]
        return "?city=" + city_id

    # 雨の日の天気情報を送信 
    async def send_rain_weather_details(self, weather_data, city, send_channel_id):
        today_weather_embed = discord.Embed(title="今日 " + city + " は雨が降るらしいよ！",
                                            color=0x00ff00,
                                            url="https://weather.yahoo.co.jp/weather/jp/13/4410.html"
                                            )
        today_weather_embed.add_field(name=weather_data["title"],
                                      value=weather_data["forecasts"][0]["telop"])
        today_weather_embed.set_footer(text="made by koto74")
        channel = self.client.get_channel(send_channel_id)
        await channel.send(embed=today_weather_embed)

