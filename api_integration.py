#!/usr/bin/python

#-----------------------------------
# TASK APP -- Database API Layer
#-----------------------------------


import json
import sqlite3
from datetime import date

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

def update_task(request):
    conn, c = get_db()
    for i in range(len(request)):
        task = request[i]
        task_id = task['id']
        title = task['title']
        description = task['description']
        # date_created = task['date_created']
        date_due = task['date_due']
        status = task['status']
        priority = task['priority']
        c.execute('UPDATE tasks SET title = ?, description = ?, date_due = ?, status = ?, priority = ? WHERE id = ?', (title, description, date_due, status, priority, task_id))
        conn.commit()

def select_all():
    conn, c = get_db()
    query = "SELECT * FROM tasks"
    results = c.execute(query)
    tasks = []
    for row in results:
        tasks.append({"id":row[0],"title":row[1],"description":row[2],"date_created":row[3],"date_due":row[4],"status":row[5],"priority":row[6]})
    conn.close()
    return tasks

def add_task(request):
    conn, c = get_db()
#    for i in range(len(request)):
#        task = request[i]
    title = request['title']
    description = request['description']
    date_created = str(date.today())
    date_due = request['date_due']
#        status = task['status']
    priority = request['priority-radio']
    c.execute('INSERT INTO tasks(title, description, date_created, date_due, priority-radio) VALUES (?, ?, ?, ?, ?)', (title, description, date_created, date_due, priority))
    conn.commit()
#     conn.close()

#
# request = [{"id":"1", "title":"Clean the car","description":"Buy cleaning products and get organised","date_due":"26-02-2019","status":"to do","priority":"high",}]
# # #
# # #
# # # add_task(request)
# update_task(request)

# print(select_all())
