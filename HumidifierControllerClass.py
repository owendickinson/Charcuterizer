class HumidifierController :

    # Variable defining the range of acceptable humidities (should be a tuple)
    # Units are percent.
    targetHumidityRange = None

    # Variable defining the sensor control object that this object listens to
    sensor = None

    # Variable defining the GPIO pin that controlls the humidifier relay
    gpioControlPin = None

    def __init__(self, sensorArg, targetHumidityRangeArg, gpioControlPinArg) :
        self.sensor = sensorArg
        self.targetHumidityRange = targetHumidityRangeArg
        self.gpioControlPin = gpioControlPinArg

    def printVariables(self):
        print ('This humidifier controller listens to {}'.format(self.sensor))
        print ('The humidity range is {}'.format(self.targetHumidityRange))
        print ('The control pin number is {}'.format(self.gpioControlPin))

# end of class definition
