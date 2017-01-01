class HeaterController:

    targetTemperatureRange = None
    sensor = None
    gpioControlPin = None

    def __init__ (self, sensorArg, targetTemperatureRangeArg, gpioControlPinArg):
        self.sensor = sensorArg
        self.targetTemperatureRange = targetTemperatureRangeArg
        self.gpioControlPin = gpioControlPinArg

    def printVariables (self):
        print ('This heater controller listens to a DHT22 sensor')
        print ('The target temperature range is {}'.format(self.targetTemperatureRange))
        print ('The GPIO pin that is used is {}'.format(self.gpioControlPin))

    def querySensor(self) :
        temperature = self.sensor.getTemperature()
        print("Sensor queried: Returned T = {:4.2f} C".format(temperature))
        self.isTemperatureInRange(temperature)

    def isTemperatureInRange(self, temperature) :
        if temperature > self.targetTemperatureRange[0] and temperature < self.targetTemperatureRange[1] :
            print ("Measured temperature ({:4.2f} C) is within the target range {}".format(temperature, self.targetTemperatureRange))
        else :
            print ("Measured temperature ({:4.2f} C) is outside the target range {}".format(temperature, self.targetTemperatureRange))


#Close of class
