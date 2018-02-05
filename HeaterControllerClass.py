# Import GPIO interface control module
import RPi.GPIO as GPIO


class HeaterController:

    def __init__(self, sensorArg, targetTemperatureRangeArg, gpioControlPinArg):
        self.sensor = sensorArg
        self.targetTemperatureRange = targetTemperatureRangeArg
        self.gpioControlPin = gpioControlPinArg

        self.isHeaterActive = False

        self.isGpioSetup = False

    def __del__(self):
        if self.isGpioSetup:
            GPIO.cleanup(self.gpioControlPin)

    def printVariables(self):
        print('This heater controller listens to a DHT22 sensor')
        print('The target temperature range is {}'.format(
            self.targetTemperatureRange))
        print('The GPIO pin that is used is {}'.format(self.gpioControlPin))

    def querySensor(self):
        temperature = self.sensor.getTemperature()
        print("Sensor queried: Returned T = {:4.2f} C".format(temperature))
        self.isTemperatureInRange(temperature)
        return temperature

    def isTemperatureInRange(self, temperature):
        if temperature > self.targetTemperatureRange[0] and temperature < self.targetTemperatureRange[1]:
            print("Measured temperature ({:4.2f} C) is within the target range {}".format(
                temperature, self.targetTemperatureRange))
        else:
            print("Measured temperature ({:4.2f} C) is outside the target range {}".format(
                temperature, self.targetTemperatureRange))

    def switchHeater(self):
        if not self.isGpioSetup:
            self.setupGpio()

        temperature = self.querySensor()
        # Is the temperature below the target range?
        if temperature < self.targetTemperatureRange[1] and not self.isHeaterActive:
            self.activateHeater()
        elif temperature > self.targetTemperatureRange[1] and self.isHeaterActive:
            self.deactivateHeater()

    def activateHeater(self):
        print('Activating the heater')
        # set output pin to be "high" 3.3 V
        GPIO.output(self.gpioControlPin, GPIO.HIGH)
        self.isHeaterActive = True

    def deactivateHeater(self):
        print('Deactivating the heater')
        # set output pin to be "low" 0 V
        GPIO.output(self.gpioControlPin, GPIO.LOW)
        self.isHeaterActive = False

    def setupGpio(self):
        # set the pin labelling mode to "broadcom mode"
        GPIO.setmode(GPIO.BCM)
        # define the pin to be an output pin
        GPIO.setup(self.gpioControlPin, GPIO.OUT)
        # Register that GPIO is set up
        self.isGpioSetup = True


# Close of class
