from flask import Flask, render_template, request, jsonify
import requests
import api_integration as db_api
import datetime
import sqlite3

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        db_api_response = requests.get("http://127.0.0.1:5000/tasks")
        api_data = db_api_response.json()
    #    if data_postcode['status'] == 200:
    #        print('Postcode not recognized!')
        return render_template("home.html", title="Homepage", **locals())

    if request.method == 'POST':
        form_data = request.form
#        description = form_data["description"]
#        title = form_data["title"]
#            due_date = form_data["due_date"]
#            due_created = form_data["date_created"]
        post_db_response = requests.post("http://127.0.0.1:5000/tasks", data=form_data)

#        return jsonify({
#        'json_data': post_db_response
#        })


        db_api_response = requests.get("http://127.0.0.1:5000/tasks")
        api_data = db_api_response.json()
        return render_template("home.html", title="Homepage", **locals())

@app.route("/new_task")
def new_task():
    return render_template("new_task.html", title="Create New Task")

@app.route("/tasks", methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        dummy_api_data = db_api.select_all()
#        [
#    {"id":"0001",
#    "title":"Take dog to the vets",
#    "description":"Skye needs immunisations.",
#    "date_created":"10-02-2019","date_due":"26-02-2019",
#    "status":"to do",
#    "priority":"high",},
#    {"id":"0002",
#    "title":"Get a hair cut",
#    "description":"Book with the hairdresser's recommended by sister, she had a great experience.",
#    "date_created":"12-02-2019",
#    "date_due":"17-02-2019",
#    "status":"to do",
#    "priority":"medium",},
#    {"id":"0003",
#    "title":"Get milk",
#    "description":"Book with the hairdresser's recommended by sister, she had a great experience.",
#    "date_created":"12-02-2019",
#    "date_due":"17-02-2019",
#    "status":"to do",
#    "priority":"medium",},
#    {"id":"0001",
#    "title":"Take dog to the vets",
#    "description":"Skye needs immunisations.",
#    "date_created":"10-02-2019","date_due":"26-02-2019",
#    "status":"to do",
#    "priority":"high",},
#    ]
        return jsonify(dummy_api_data)

    elif request.method == 'POST':
        db_api.add_task(request)


if __name__ == "__main__":
    app.run(debug = True)
