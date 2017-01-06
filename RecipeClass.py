import mysql.connector

class Recipe :

    recipeId = None

    dbConnection = None
    dbCursor = None

    durations = None
    minimumTemperatures = None
    maximumTemperatures = None
    minimumHumidities = None
    maximumHumidities = None

    recipeInfo = None



    def __init__(self, recipeIdArg) :
        self.recipeId = recipeIdArg

    def connectToDb(self) :
        try :
            self.dbConnection = mysql.connector.connect(user='charcuterizer',
            password='Sweetbee4',
            host='localhost',
            database='charcuterizer')
        except mysql.connector.errors.DatabaseError as error :
            print (error)
            self.dbConnection = None
            self.dbCursor = None
            return

        try :
            self.dbCursor = self.dbConnection.cursor()
        except mysql.connector.errors.DatabaseError as error :
            print (error)
            self.dbCursor = None

    def makeDictionaryFromRow(self, row) :
        dict(zip(self.dbCursor.column_names, row))

    def loadInfoForRecipe(self) :
        recipeQuery = ('select * from recipes left join literature on recipes.literature_id = literature.id where recipes.id=%s')
        if self.dbCursor is not None :
            self.dbCursor.execute(recipeQuery, (self.recipeId,))
            self.recipeInfo = self.makeDictionaryFromRow(self.dbCursor.fetchone())

    def loadInfoForStages(self) :
        self.minimumTemperatures = []
        self.maximumTemperatures = []
        self.minimumHumidities = []
        self.maximumHumidities = []
        self.durations = []

        # min temperatures
        minTempQuery = ('select min_temp.value as min_temp from temperatures_for_recipes left join min_temp on min_temp.id = temperatures_for_recipes.min_temp_id where temperatures_for_recipes.recipe_id = %s;')
        self.dbCursor.execute(minTempQuery, (self.recipeId,))
        for row in self.dbCursor :
            self.minimumTemperatures.append(self.makeDictionaryFromRow(row))

        # max temperatures
        maxTempQuery = ('select max_temp.value as min_temp from temperatures_for_recipes left join min_temp on min_temp.id = temperatures_for_recipes.min_temp_id where temperatures_for_recipes.recipe_id = %s;')
        self.dbCursor.execute(maxTempQuery, (self.recipeId,))
        for row in self.dbCursor :
            self.maximumTemperatures.append(self.makeDictionaryFromRow(row))

        # min humidities
        minHumidityQuery = ('select min_humidity.value as min_humidity from humidities_for_recipes left join min_humidity on min_humidity.id = humidities_for_recipes.min_humidity_id where humidities_for_recipes.recipe_id = %s;')
        self.dbCursor.execute(minHumidityQuery, (self.recipeId,))
        for row in self.dbCursor :
            self.minimumHumidities.append(self.makeDictionaryFromRow(row))

        # max humidities
        minHumidityQuery = ('select max_humidity.value as max_humidity from humidities_for_recipes left join max_humidity on max_humidity.id = humidities_for_recipes.max_humidity_id where humidities_for_recipes.recipe_id = %s;')
        self.dbCursor.execute(minHumidityQuery, (self.recipeId,))
        for row in self.dbCursor :
            self.maximumHumidities.append(self.makeDictionaryFromRow(row))

        # durations
        durationQuery = ('select duration.value as duration from durations_for_recipes left join duration on duration.id = durations_for_recipes.duration_id where durations_for_recipes.recipe_id = %s;')
        self.dbCursor.execute(durationQuery, (self.recipeId,))
        for row in self.dbCursor :
            self.durations.append(self.makeDictionaryFromRow(row))

        print ('{}\n{}\n{}\n{}\n{}\n'.format(self.minimumTemperatures,
                                             self.maximumTemperatures,
                                             self.minimumHumidities,
                                             self.maximumHumidities,
                                             self.durations))


# select min_temp.value as min_temp from temperatures_for_recipes left join min_temp on min_temp.id = temperatures_for_recipes.min_temp_id where temperatures_for_recipes.recipe_id = 1;
