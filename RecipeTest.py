from RecipeClass import Recipe

# Create a instance of the Recipe class (an obect of type Recipe)
recipe = Recipe(1)

recipe.connectToDb()

recipe.loadInfoForRecipe()
recipe.loadInfoForStages()

schedule = recipe.makeScheduleForRecipe()
print('{}\n{}\n{}\n'.format(schedule.transitionTimes,
                            schedule.temperatureRanges,
                            schedule.humidityRanges))

schedule = recipe.makeScheduleForRecipe(startingStage=1)
print('{}\n{}\n{}\n'.format(schedule.transitionTimes,
                            schedule.temperatureRanges,
                            schedule.humidityRanges))

schedule = recipe.makeScheduleForinterruptedRecipe()
print('{}\n{}\n{}\n'.format(schedule.transitionTimes,
                            schedule.temperatureRanges,
                            schedule.humidityRanges))
