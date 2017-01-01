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

# create an object of type HumTemSensor, the first argument is the GPIO pin
# number dusing the BROADCOM numbering scheme
hts = HumTemSensor(18)

tc = HeaterController(hts, (20, 25), 15)
tc.printVariables()
tc.querySensor()

#create an object of type HumidifierController
hc1 = HumidifierController(hts, (55, 65), 15)
hc1.printVariables()

#create an object of type HumidifierController
hc2 = HumidifierController(hts, (90, 95), 14)
hc2.printVariables()
