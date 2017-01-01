class HeaterController:

    targetTemperatureRange = None
    sensor = None
    gpioControlPin = None

    def __init__ (self, sensorArg, targetTemperatureRangeArg, gpioControlPinArg):
        self.sensor = sensorArg
        self.targetTemperatureRange = targetTemperatureRangeArg
        self.gpioControlPin = gpioControlPinArg
    def printVariables (self):
        print ('This heater controller listens to {}'.format(self.sensor))
        print ('The target temperature range is {}'.format(self.targetTemperatureRange))
        print ('The GPIO pin that is used is {}'.format(self.gpioControlPin))
#Close of class        
