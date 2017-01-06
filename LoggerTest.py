from LoggerClass import Logger

logger = Logger(1)

logger.connectToDb()

logger.newBatch()

logger.heartbeat()
