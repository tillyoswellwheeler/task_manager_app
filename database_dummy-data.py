#-----------------------------------
# TASK APP -- Database Dummy Data
#-----------------------------------

import sqlite3


###---creating a database and cursor---###
conn = sqlite3.connect('task_manager.db')
c = conn.cursor()

def delete_table():
    c.execute('DROP TABLE tasks')

delete_table()

###---Creating a table within the database with column names---###
def create_table_tasks():
    c.execute(
        'CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, title TEXT , description TEXT, date_created TEXT, date_due TEXT, status TEXT, priority INT)')


create_table_tasks()

dummy_tasks = [{"title":"Take dog to the vets","description":"Skye needs immunisations.","date_created":"10-02-2019","date_due":"26-02-2019","status":"to do","priority":"high",},
{"title":"Get a hair cut","description":"Book with the hairdresser's recommended by sister, she had a great experience.","date_created":"12-02-2019","date_due":"17-02-2019","status":"to do","priority":"medium",},
{"title":"Take out bins","description":"It's your turn to take out the bins.","date_created":"16-02-2019","date_due":"18-02-2019","status":"done","priority":"low",},
{"title":"Ring mum","description":"Ring for a catch up.","date_created":"14-02-2019","date_due":"20-02-2019","status":"to do","priority":"medium",},
{"title":"Go food shopping","description":"Eggs, milk, bread, carrots.","date_created":"13-02-2019","date_due":"16-02-2019","status":"overdue","priority":"medium",},
{"title":"Mow lawn","description":"Mow the lawn whilst the weather is nice.","date_created":"08-02-2019","date_due":"20-02-2019","status":"overdue","priority":"low",},
{"title":"Bake cake","description":"Bake a lemon drizzle cake for Laura's birthday.","date_created":"21-02-2019","date_due":"30-02-2019","status":"to do","priority":"high",},
{"title":"Book plane ticket","description":"Book flight for trip to Spain.","date_created":"18-02-2019","date_due":"24-02-2019","status":"to do","priority":"high",}
]

###---Adding data from json file of random tasks to table in database (for loop to loop through values)---###
def dummy_data_entry():
    for i in range(len(dummy_tasks)):
        task = dummy_tasks[i]
        # task_id = task['id']
        title = task['title']
        description = task['description']
        date_created = task['date_created']
        date_due = task['date_due']
        status = task['status']
        priority = task['priority']
        c.execute('INSERT INTO tasks(title, description, date_created, date_due, status, priority) VALUES (?, ?, ?, ?, ?, ?)', (title, description, date_created, date_due, status, priority))
        conn.commit()

dummy_data_entry()

# ###---Retrieving all tasks
# def read_all_tasks():
#     c.execute('SELECT * FROM tasks ')
#     for row in c.fetchall():
#         print(row)
