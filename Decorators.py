#!/usr/bin/env python
#
# Created by carlosjimz on 22/11/2018 18:02
#
##############################################################

import os
import logging
import sqlite3

DB_FILENAME = "users.db"
TABLE_NAME = "users"


# class DBManagerWithDecorators:
#
#     def db_handler(db_function):
#         def inner(cursor):
#             commands = db_function(cursor)
#             function_name = db_function.__qualname__
#
#             try:
#                 for command in commands:
#                     cursor.execute(command)
#                     print('Executing {} command.'.format(command), command)
#             except Exception as e:
#                 logging.error("Error in %s: %s", function_name, e)
#                 return -1
#             else:
#                 logging.info("%s run successfully", function_name)
#                 return 0
#         return inner
#
#     @db_handler
#     def select_allitems_from_table(self, cursor, tablename):
#         return (
#             """SELECT * FROM {0}""".format(tablename)
#         )
#
#     @db_handler
#     def create_table(self, cursor, tablename, columns):
#         columns = ''.join(['%s %s,' % (key, value) for (key, value) in columns.items()])
#         return (
#             """CREATE TABLE {0} ({1})""".format(tablename, columns)
#         )
#
#     @staticmethod
#     def create_db(filename):
#         return sqlite3.connect(filename)

sentence = ""


def db_handler(query):
    def inner(cursor):
        commands = query(cursor)
        query_name = query.__qualname__

        try:
            for command in commands:
                cursor.execute(command)
                print("Executing"+query)
        except Exception as e:
            logging.error("Error in %s: %s", query_name, e)
            return -1
        else:
            logging.info("%s run successfully", query_name)
            return 0
    return inner

@db_handler
def hendler_select_allitems_from_table(cursor, tablename):
    return (
        # '''SELECT * FROM {0}'''.format(tablename)
        '''SELECT * FROM  users'''
    )

@db_handler
def handler_create_table(cursor):
    return (
        sentence
    )

@db_handler
def handler_create_table2(cursor):
    return (
        '''CREATE TABLE users
             (name text, surname text, age real, email text, phone real)'''
    )


def select_allitems_from_table(cursor, tablename):
    sentence = """SELECT * FROM {0}""".format(tablename)
    return hendler_select_allitems_from_table(cursor=cursor)


def create_table(cursor, tablename, columns):
    columns = ''.join(['%s %s,' % (key, value) for (key, value) in columns.items()])
    sentence = """CREATE TABLE {0} ({1})""".format(tablename, columns[:-1])
    return handler_create_table2(cursor=cursor)


def create_db(filename):
    return sqlite3.connect(filename)

columns = {'name': 'text', 'surname': 'text', 'age': 'real', 'email': 'text', 'phone': 'real'}

os.remove(DB_FILENAME)
cursor = create_db(DB_FILENAME)
create_table(cursor=cursor, tablename=TABLE_NAME, columns=columns)
select_allitems_from_table(cursor=cursor, tablename=TABLE_NAME)
