from scheduler import Scheduler
from OpenWeather import OpenWeather
from GetHumidityByLocation import GetHumidityByLocation
from Irrigation import IrrigationSystem
from PublishResult import PublishResult

import time

global_data = ['ho chi minh', 0 , 0, False, False]  # [city, temp, humanity, current status  , status change ]

scheduler = Scheduler()
scheduler.SCH_Init()

taskOpenWeather = OpenWeather(global_data)
irrigation_system = IrrigationSystem(global_data)
getHumidityByLocation = GetHumidityByLocation(global_data)
publishResult = PublishResult(global_data)

scheduler.SCH_Add_Task(taskOpenWeather.openWeather_Run, DELAY=1000, PERIOD=5000)
scheduler.SCH_Add_Task(getHumidityByLocation.GetHumidity_Run, DELAY=1000, PERIOD=5000)
scheduler.SCH_Add_Task(irrigation_system.IrrigationSystem_Run, DELAY=1000, PERIOD=5000)
scheduler.SCH_Add_Task(publishResult.PublishResult_run, DELAY=1000, PERIOD=5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
