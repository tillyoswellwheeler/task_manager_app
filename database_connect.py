#!/usr/bin/python

#-----------------------------------
# TASK APP -- Database API Layer
#-----------------------------------


import json


def getdb():
    try:
        conn = psycopg2.connect(user="matildaoswell-wheeler",
                                password="",
                                host="127.0.0.1",
                                port="5432",
                                database="task_manager")
        cursor = conn.cursor()
        # Print PostgreSQL Connection properties
        print(conn.get_dsn_parameters(), "\n")
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        return cursor
    except:
        return False
# try:


# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
#
# finally:
#     #closing database connection.
#         if conn:
#             cursor.close()
#             conn.close()
#             print("PostgreSQL connection is closed")


########
def add_task():
    cursor, conn = get_db()
    with cursor.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `tasks` (`title`, `description`, 'date_created', 'date_due', 'status', 'priority') VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    conn.commit()
########


cursor.close()
conn.close()