import pigpio
import DHT22
import time

class HumTemSensor:
    gpioControlPin = None

    waitTime = None

    gpioInterface = None

    humTemSensor = None

    def __init__(self, gpioControlPinArg, waitTimeArg=1):
        self.gpioControlPin = gpioControlPinArg
        self.waitTime = waitTimeArg

    def setUpSensor(self):
        # Creating and object of type pi from the module that the class of type pi is defined in.
        # and calling it gpioInterface. So we are giving the property gpioInterface set up in the class
        # section a variable 'pi' instead of it being none. In the brackets the built in constructor
        # is operating its own __init__.
        self.gpioInterface = pigpio.pi()
        #This is creating an object type sensor defined in the DHT22 import.It will do the __init__ self bit itself
        #but it isn't written in. We learned by internet research that this object type needs two arguments
        # to be defined. They are the interface type and the pin number used. We called tham as seen below.
        self.humTemSensor = DHT22.sensor (self.gpioInterface, self.gpioControlPin)

    def getTemperature(self):
        if self.humTemSensor is not None :
            self.humTemSensor.trigger()
            time.sleep (self.waitTime)
            # we are saving the value determined in the right hand side of the assignment (=) as the word temperature.
            temperature = self.humTemSensor.temperature()
            # This bit sends the value back to the part of the code that asked for it.
            return temperature

    def getHumidity(self):
        if self.humTemSensor is not None :
            self.humTemSensor.trigger()
            time.sleep (self.waitTime)
            humidity = self.humTemSensor.humidity()
            return humidity
