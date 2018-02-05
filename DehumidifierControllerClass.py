# Import GPIO interface control module
import RPi.GPIO as GPIO


class DehumidifierController:

    def __init__(self, sensorArg, targetHumidityRangeArg, gpioControlPinArg):
        # Save input arguments to instance variables
        # Variable defining the sensor control object that this object listens to
        self.sensor = sensorArg
        # Variable defining the range of acceptable humidities (should be a tuple)
        # Units are percent.
        self.targetHumidityRange = targetHumidityRangeArg
        # Variable defining the GPIO pin that controls the humidifier relay
        self.gpioControlPin = gpioControlPinArg

        # Initialize remaining instance variables to sensible values
        # Variable defining the activity state of the dehumidifier.
        self.isDehumidifierActive = False

        # Variable defining the setup status of the GPIO interface
        self.isGpioSetup = False

    def __del__(self):
        if self.isGpioSetup:
            GPIO.cleanup(self.gpioControlPin)

    def printVariables(self):
        print('This dehumidifier controller listens to  to a DHT22 sensor')
        print('The humidity range is {}'.format(self.targetHumidityRange))
        print('The control pin number is {}'.format(self.gpioControlPin))

    def querySensor(self):
        humidity = self.sensor.getHumidity()
        print("Sensor queried: Returned H = {:4.2f} %".format(humidity))
        self.isHumidityInRange(humidity)
        return humidity

    def isHumidityInRange(self, humidity):
        if humidity > self.targetHumidityRange[0] and humidity < self.targetHumidityRange[1]:
            print("Measured humidity ({:4.2f} %) is within the target range {}".format(
                humidity, self.targetHumidityRange))
        else:
            print("Measured humidity ({:4.2f} %) is outside the target range {}".format(
                humidity, self.targetHumidityRange))

    def switchDehumidifier(self):
        if not self.isGpioSetup:
            self.setupGpio()

        humidity = self.querySensor()
        # Is the humidity below the target range? Note same range should be used
        # for humidifier and dehumidifier target ranges
        # Zero is left in place in case humidity buffer is desired
        if humidity > (0 + self.targetHumidityRange[1]):
            self.activateDehumidifier()
        elif self.isDehumidifierActive:
            self.deactivateDehumidifier()

    def activateDehumidifier(self):
        print('Activating the dehumidifier')
        # set output pin to be "high" 3.3 V
        GPIO.output(self.gpioControlPin, GPIO.HIGH)
        self.isDehumidifierActive = True

    def deactivateDehumidifier(self):
        print('Deactivating the dehumidifier')
        # set output pin to be "low" 0 V
        GPIO.output(self.gpioControlPin, GPIO.LOW)
        self.isDehumidifierActive = False

    def setupGpio(self):
        # set the pin labelling mode to "broadcom mode"
        GPIO.setmode(GPIO.BCM)
        # define the pin to be an output pin
        GPIO.setup(self.gpioControlPin, GPIO.OUT)
        # Register that GPIO is set up
        self.isGpioSetup = True
# end of class definition
