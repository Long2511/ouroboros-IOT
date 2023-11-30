import argparse
import requests
from simple_chalk import chalk


class GetHumidityByLocation:
    API_KEY = '9850a4b7b8874b78b35151949232411'
    BASE_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

    def __init__(self, global_data):
        self.output = None
        self.public_ip = self.get_public_ip()
        self.data = None
        self.global_data = global_data

        print("Init world Weather Online")

    def get_public_ip(self):
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data['query']

    def get_humidity(self):
        url = f"{self.BASE_URL}?q={self.public_ip}&key={self.API_KEY}&format=json"
        response = requests.get(url)
        if response.status_code != 200:
            print(chalk.red("Error: Unable to retrieve humidity information."))
            exit()
        self.data = response.json().get("data").get("current_condition")[0].get("humidity")

    def process_humidity_data(self):
        humidity = self.data

        self.output = {
            "humidity": float(humidity),
        }

    def GetHumidity_Run(self):
        self.get_humidity()
        self.process_humidity_data()

        print(self.output["humidity"])
        from main import global_data
        global_data[2] = self.output["humidity"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get weather information for a destination.")
    parser.add_argument("global_data", type=str, help="global_data needed.")
    args = parser.parse_args()

    world_weather_online = GetHumidityByLocation(args.global_data)
    world_weather_online.GetHumidity_Run()
