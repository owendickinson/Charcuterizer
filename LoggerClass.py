import mysql.connector
import datetime
from ScheduleClass import Schedule

class Logger :

    recipeId = None

    dbConnection = None
    dbCursor = None

    runningBatchLog = None

    def __init__(self, recipeIdArg) :
        self.recipeId = recipeIdArg

    def __del__(self):
        if self.dbConnection is not None :
            self.dbConnection.close()

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

    def loadRunningBatchLog(self) :
        runningBatchQuery = ('select logs_for_batches.* from (select batches.id as batch_id from recipes left join batches on batches.recipe_id = recipes.id where recipes.id = %s order by batches.id desc limit 1) as last_batch_for_recipe left join logs_for_batches on last_batch_for_recipe.batch_id = logs_for_batches.batch_id;')
        self.dbCursor.execute(runningBatchQuery, (self.recipeId,))
        self.runningBatchLog = dict(zip(self.dbCursor.column_names, self.dbCursor.fetchone()))

    def heartbeat(self) :
        self.loadRunningBatchLog()
        heartbeatQuery = ('update logs_for_batches set time_last_alive = %s where id = %s')
        self.dbCursor.execute(heartbeatQuery, (datetime.datetime.now(), self.runningBatchLog['id']))
        self.dbConnection.commit()

    def completedStage(self) :
        self.loadRunningBatchLog()
        nextStageCompleted = 0
        if self.runningBatchLog['last_stage_completed'] is not None :
            nextStageCompleted = self.runningBatchLog['last_stage_completed'] + 1
        completedStageQuery = ('update logs_for_batches set time_last_alive = %s, time_last_stage_completed = %s, last_stage_completed = %s where id = %s')
        self.dbCursor.execute(completedStageQuery, (datetime.datetime.now(), datetime.datetime.now(), nextStageCompleted, self.runningBatchLog['id']))
        self.dbConnection.commit()

    def newBatch(self, comment = '') :
        newBatchQuery = ('insert into batches (recipe_id, start_date, comments) values (%s, %s, %s)')
        self.dbCursor.execute(newBatchQuery, (self.recipeId, datetime.datetime.now(), comment))
        batchId = self.dbCursor.lastrowid
        print ('batchId', batchId)
        newBatchLogQuery = ('insert into logs_for_batches (batch_id, time_last_alive) values (%s, %s)')
        self.dbCursor.execute(newBatchLogQuery, (batchId, datetime.datetime.now()))

        self.dbConnection.commit()
