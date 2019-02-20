#!/usr/bin/python

#-----------------------------------
# TASK APP -- Database API Layer
#-----------------------------------


import json
import sqlite3


#---------------------------------------------#
#Connect to database
#---------------------------------------------#

def get_db():
    try:
        conn = sqlite3.connect('task_manager.db')
        c = conn.cursor()
        return conn, c
    except:
        return False

#---------------------------------------------#
# Interacting with database
#---------------------------------------------#

########
# def add_task():
#     cursor, conn = get_db()
#     with cursor.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `tasks` (`title`, `description`, 'date_created', 'date_due', 'status', 'priority') VALUES (?, ?, ?, ?, ?, ?)"
#         cursor.execute(sql)
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     conn.commit()
########

# def select_all():
#     conn, c = get_db()
#     query = "SELECT * FROM tasks"
#     results = c.execute(query)
#     tasks = []
#     for row in results:
#         for key in c.description:
#             tasks.append({key[0]:value for value in row})
#     conn.close()
#
#     return tasks

def select_all():
    conn, c = get_db()
    query = "SELECT * FROM tasks"
    results = c.execute(query)
    tasks = []
    for row in results:
        for col in c.description:
            tasks.append({key[0]:value for value in row})
    conn.close()

 def add_task(request):
     conn, c = get_db()
     for i in range(len(request)):
        task = request[i]
        title = task['title']
        description = task['description']
        date_created = task['date_created']
        date_due = task['date_due']
        status = task['status']
        priority = task['priority']
        c.execute('INSERT INTO tasks(title, description, date_created, date_due, status, priority) VALUES (?, ?, ?, ?, ?, ?)', (title, description, date_created, date_due, status, priority))
        conn.commit()
#     conn.close()




# print(select_all())