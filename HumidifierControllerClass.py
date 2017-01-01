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
        print ('This humidifier controller listens to  to a DHT22 sensor')
        print ('The humidity range is {}'.format(self.targetHumidityRange))
        print ('The control pin number is {}'.format(self.gpioControlPin))

    def querySensor(self) :
        humidity = self.sensor.getHumidity()
        print("Sensor queried: Returned H = {} %".format(humidity))
        self.isHumidityInRange(humidity)

    def isHumidityInRange(self, humidity) :
        if humidity > self.targetHumidityRange[0] and humidity < self.targetHumidityRange[1] :
            print ("Measured humidity ({} %) is within the target range {}".format(humidity, self.targetHumidityRange))
        else :
            print ("Measured humidity ({} %) is outside the target range {}".format(humidity, self.targetHumidityRange))


# end of class definition
