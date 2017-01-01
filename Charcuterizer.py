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
# that objects of type HumidifierController behave, from a file called
# HumidifierControllerClass.py
from HeaterControllerClass import HeaterController

import time

# create an object of type HumTemSensor, the first argument is the GPIO pin
# number dusing the BROADCOM numbering scheme
hts = HumTemSensor(18)

tc = HeaterController(hts, (20, 21), 15)
tc.printVariables()
# try :
#     while True :
#         tc.switchHeater()
#         time.sleep(0.5)
# except KeyboardInterrupt :
#     print ("KeyboardInterrupt encountered")

targetHumidityRange = (65, 80)

#create an object of type HumidifierController
hc = HumidifierController(hts, targetHumidityRange, 15)
hc.printVariables()
hc.querySensor()

#create an object of type HumidifierController
dhc = DehumidifierController(hts, targetHumidityRange, 15)
dhc.printVariables()
dhc.querySensor()

try :
    while True :
        hc.switchHumidifier()
        dhc.switchDehumidifier()
        time.sleep(0.5)
except KeyboardInterrupt :
    print ("KeyboardInterrupt encountered")
