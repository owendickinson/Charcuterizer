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
from HeaterControllerClass import HeaterController

import time

# create an object of type HumTemSensor, the first argument is the GPIO pin
# number dusing the BROADCOM numbering scheme
hts = HumTemSensor(18)

tc = HeaterController(hts, (18, 21), 15)
tc.printVariables()
try :
    while True :
        tc.switchHeater()
        time.sleep(0.5)
except KeyboardInterrupt :
    print ("KeyboardInterrupt encountered")

#create an object of type HumidifierController
hc1 = HumidifierController(hts, (55, 65), 15)
hc1.printVariables()
hc1.querySensor()

#create an object of type HumidifierController
hc2 = HumidifierController(hts, (90, 95), 14)
hc2.printVariables()
hc2.querySensor()
