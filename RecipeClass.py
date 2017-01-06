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
        except mysql.connector.errors.DatabaseException as error :
            print (error)
            self.dbConnection = None
            self.dbCursor = None
            return

        try :
            # specifying dictionary=True creates a cursor thatreturns rows as
            # dictionaries with keys corresponding to the column names.
            self.dbCursor = self.dbConnection.cursor(dictionary=True)
        except mysql.connector.errors.DatabaseException as error :
            print (error)
            self.dbCursor = None

    def loadInfoForRecipe(self) :
        recipeQuery = ('select * from recipes left join literature on recipes.literature_id = literature.id where recipes.id=%s')
        if self.dbCursor is not None :
            self.dbCursor.execute(recipeQuery, (self.recipeId,))
            for row in self.dbCursor :
                print (row)

    def loadInfoForStages(self) :
        pass


# select min_temp.value as min_temp from temperatures_for_recipes left join min_temp on min_temp.id = temperatures_for_recipes.min_temp_id where temperatures_for_recipes.recipe_id = 1;
