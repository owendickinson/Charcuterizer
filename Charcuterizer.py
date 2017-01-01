from HumidifierControllerClass import HumidifierController
from HeaterControllerClass import HeaterController

#create an object of type HumidifierController
hc1 = HumidifierController("Funky sensor 1", (55, 65), 15)
hc1.printVariables()

#create an object of type HumidifierController
hc2 = HumidifierController("Funky sensor 2", (90, 95), 14)
hc2.printVariables()

tc = HeaterController("Hugh's patience length", (14, 20), 15)
tc.printVariables()
