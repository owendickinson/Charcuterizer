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

from RecipeClass import Recipe

from LoggerClass import Logger

import time
import datetime

# create a Recipe (loads recipe data from the database)
recipe = Recipe(1)
recipe.connectToDb()
recipe.loadInfoForRecipe()
recipe.loadInfoForStages()


recovering = True
# Use the recipe to create a schedule
schedule = None
if recovering :
    schedule = recipe.makeScheduleForInterruptedRecipe()
else :
    schedule = recipe.makeScheduleForRecipe()
# OLD CODE => schedule = Schedule([3, 4, 5], [(18, 20),(25, 27),(18, 25)], [(60, 70),(80, 90),(65, 85)])
schedule.printVariables()
print ("Current humidity range is {}".format(schedule.getHumidityRange()))
print ("Current temperature range is {}".format(schedule.getTemperatureRange()))

# create a Logger object to monitor progress
logger = Logger(recipe.recipeId)

# create a new batch and batch log for this recipe
logger.connectToDb()
logger.newBatch('Test With Comment')

# create an object of type HumTemSensor, the first argument is the GPIO pin
# number dusing the BROADCOM numbering scheme
hts = HumTemSensor(18)

tc = HeaterController(hts, schedule.getTemperatureRange(), 14)
tc.printVariables()

#create an object of type HumidifierController
hc = HumidifierController(hts, schedule.getHumidityRange(), 15)
hc.printVariables()
hc.querySensor()

#create an object of type HumidifierController
dhc = DehumidifierController(hts, schedule.getHumidityRange(), 17)
dhc.printVariables()
dhc.querySensor()

try :
    while not schedule.isComplete() :
        hc.targetHumidityRange = schedule.getHumidityRange()
        dhc.targetHumidityRange = schedule.getHumidityRange()
        tc.targetTemperatureRange = schedule.getTemperatureRange()

        hc.switchHumidifier()
        dhc.switchDehumidifier()
        tc.switchHeater()

        if schedule.isUpdateRequired() :
            logger.completedStage()
        else :
            print ('heartbeat')
            logger.heartbeat()

        time.sleep(60)
except KeyboardInterrupt :
    print ("KeyboardInterrupt encountered")
