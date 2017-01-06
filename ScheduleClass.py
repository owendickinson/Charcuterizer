import datetime

class Schedule :

    transitionTimes = []
    temperatureRanges = []
    humidityRanges = []

    currentStage = 0

    def __init__(self, stageDurationsArg, temperatureRangesArg, humidityRangesArg) :
        self.createTransitionTimes(stageDurationsArg)
        self.humidityRanges = humidityRangesArg
        self.temperatureRanges = temperatureRangesArg

    def update(self) :
        updateRequired = self.isUpdateRequired()
        if updateRequired is not None and updateRequired :
            self.currentStage += 1

    def isUpdateRequired(self) :
        if not self.isComplete() :
            return datetime.date.today() > self.transitionTimes[self.currentStage]
        else :
            return None

    def createTransitionTimes(self, stageDurations) :
        self.transitionTimes = []
        print('createTransitionTimes::stageDurations', stageDurations)
        for duration in stageDurations :
            if len(self.transitionTimes) == 0 :
                self.transitionTimes.append(datetime.date.today() + datetime.timedelta(days = duration))
            else :
                self.transitionTimes.append(self.transitionTimes[-1] + datetime.timedelta(days = duration))

    def printVariables(self) :
        print("Schedule:")
        print("Transition times:\n{}".format(self.transitionTimes))
        print("Temperature Ranges\n{}".format(self.temperatureRanges))
        print("Humidity Ranges:\n{}".format(self.humidityRanges))

    def isComplete(self) :
        return self.currentStage == len(self.transitionTimes) - 1

    def getHumidityRange(self) :
        self.update()
        return self.humidityRanges[self.currentStage]

    def getTemperatureRange(self) :
        self.update()
        return self.temperatureRanges[self.currentStage]
