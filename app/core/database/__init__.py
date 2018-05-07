from pymongo import MongoClient
from logging import warn
from mongoengine import connect
from app.config.config import HOST, DATABASE_NAME, DATABASE_PORT


class Connection:

    __host = HOST
    __port = DATABASE_PORT
    __database = DATABASE_NAME
    __client = MongoClient(__host, __port)[__database]
    __collection = __client

    def __init__(self, host=__host, port=__port, database=__database):
        try:
            if host is not None:
                self.__host = host

            if port is not None:
                self.__port = port

            if database is not None:
                self.__database = database

            if self.__database is not database:
                warn('change database from ' + self.__database + ' to ' + database)
            '''
                ... re compile mongo client
            '''
            self.__client = MongoClient(self.__host, self.__port)[self.__database]
            self.__collection = self.__client
            connect(self.__database, host=self.__host, port=self.__port)
        except:
            print('Error: Unable to connect')

Connection()
