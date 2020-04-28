import logging
import os
import time
from time import gmtime, strftime
from pymongo import MongoClient

class DatabaseLoggingHandler(logging.Handler):

    def __init__(self, database, collection="logs"):
        logging.Handler.__init__(self)
        self.client = MongoClient("localhost")
        self.db = self.client[database]
        self.collection = self.db[collection]

    def emit(self, record):
        """save log record in file or database"""
        formatted_message = self.format(record)

        database_record = {
          "level": record.levelname,
          "module": record.module,
          "line": record.lineno,
          "asctime": record.asctime if getattr(record, "asctime", None) else strftime("%Y-%m-%d %H:%M", gmtime()),
          "message": record.message # use `formatted_message` for store formatted log
        }

        try:
            self.collection.insert_one(database_record)
        except Exception as e:
            print(e)
        
        
class FilterLevels(logging.Filter):
    def __init__(self, filter_levels=None):
        super(FilterLevels, self).__init__()
        self._filter_levels = filter_levels

    def filter(self, record):
        if record.levelname in self._filter_levels:
          return True
        return False
