# The following line imports the code for the class (blueprint) which defines the way
# that objects of type HumTemSensor behave, from a file called
# HumTemSensorClass.py
from HumTemSensorClass import HumTemSensor

# The following line imports the code for the class (blueprint) which defines the way
# that objects of type HumidifierController behave, from a file called
# HumidifierControllerClass.py
from HumidifierControllerClass import HumidifierController

# The following line imports the code for the class (blueprint) which defines the way
# that objects of type HumidifierController behave, from a file called
# HumidifierControllerClass.py
from DehumidifierControllerClass import DehumidifierController

# The following line imports the code for the class (blueprint) which defines the way
# that objects of type HeaterController behave, from a file called
# HeaterControllerClass.py
from HeaterControllerClass import HeaterController

# The following line imports the code for the class (blueprint) which defines the way
# that objects of type schedule behave, from a file called
# ScheduleClass.py
from ScheduleClass import Schedule

import time
import datetime

# create and initialize a schedule
schedule = Schedule([3, 4, 5], [(18, 20),(25, 27),(18, 25)], [(60, 70),(80, 90),(65, 85)])
schedule.printVariables()
print ("Current humidity range is {}".format(schedule.getHumidityRange()))
print ("Current temperature range is {}".format(schedule.getTemperatureRange()))


# create an object of type HumTemSensor, the first argument is the GPIO pin
# number dusing the BROADCOM numbering scheme
hts = HumTemSensor(18)

tc = HeaterController(hts, (20, 21), 14)
tc.printVariables()

targetHumidityRange = (65, 80)

#create an object of type HumidifierController
hc = HumidifierController(hts, targetHumidityRange, 15)
hc.printVariables()
hc.querySensor()

#create an object of type HumidifierController
dhc = DehumidifierController(hts, targetHumidityRange, 17)
dhc.printVariables()
dhc.querySensor()

try :
    while True :
        hc.targetHumidityRange = schedule.getHumidityRange()
        dhc.targetHumidityRange = schedule.getHumidityRange()
        tc.targetTemperatureRange = schedule.getTemperatureRange()

        hc.switchHumidifier()
        dhc.switchDehumidifier()
        tc.switchHeater()



        time.sleep(60)
except KeyboardInterrupt :
    print ("KeyboardInterrupt encountered")
