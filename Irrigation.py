import argparse

from GetHumidityByLocation import GetHumidityByLocation
from OpenWeather import OpenWeather



class SoilMoistureSensor:
    def __init__(self, humidity):
        self.moisture_level = humidity

    def read_moisture(self):
        return self.moisture_level


class IrrigationSystem:
    def __init__(self, global_data):

        self.sprinkler_status = False
        self.write_to_sheet = False
        self.weather_fetcher = 0
        self.humidity_fetcher = 0
        self.current_temperature = None
        self.current_humidity = None
        self.is_on = False

    def IrrigationSystem_Run(self):
        #IrrigationSystem_Run
        self.current_temperature = self.weather_fetcher
        self.current_humidity = self.humidity_fetcher
        if self.current_temperature is None or self.current_humidity is None:
            print("Could not fetch weather data. Skipping irrigation check.")
            return

        import main
        self.current_temperature = main.global_data[1]
        self.current_humidity = main.global_data[2]
        self.sprinkler_status = main.global_data[3]

        #self.current_temperature = 29
        #self.current_humidity = 49 // for testing purpose
        if self.current_temperature < 30:

            if self.current_humidity < 50:
                self.is_on = True
            elif 50 <= self.current_humidity <= 80:
                self.is_on = False
            elif self.current_humidity > 80:
                self.is_on = False
        else:
            self.is_on = False

        from main import global_data

        if self.is_on != self.sprinkler_status:
            self.write_to_sheet = True
        else:
            self.write_to_sheet = False

        self.sprinkler_status = self.is_on
        global_data[3] = self.sprinkler_status
        global_data[4] = self.write_to_sheet
        print("sprinkler:", self.sprinkler_status)
        print("write to sheet:", self.write_to_sheet)





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the irrigation system for a specific city.")
    parser.add_argument("global_data", type=list, help="Destination city for weather information.")

    args = parser.parse_args()

    irrigation_system = IrrigationSystem(args.global_data)
    irrigation_system.IrrigationSystem_Run()
