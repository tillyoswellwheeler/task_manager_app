from flask import Flask, render_template, request, jsonify, url_for
import requests
import api_integration as db_api
import datetime
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        db_api_response = requests.get("http://127.0.0.1:5000/tasks")
        api_data = db_api_response.json()
    #    if data_postcode['status'] == 200:
    #        print('Postcode not recognized!')
        return render_template("home.html", title="Homepage", **locals())




    if request.method == 'POST':
        if 'find_task_submit' in request.form:
            find_task_data = request.form.to_dict()
            delete_task = db_api.move_task(find_task_data)


        elif 'sort_submit' in request.form:
            if 'sort_radio' == "1": #priority
                db_api_response = requests.get("http://127.0.0.1:5000/tasks")
            elif 'sort_radio' == "2": #date
                db_api_response = requests.get("http://127.0.0.1:5000/tasks")
                print(db_api_response)
                api_data = []
                for row in db_api_response:
                    api_data.append({"id":row[0],"title":row[1],"description":row[2],"date_created":row[3],"date_due":row[4],"status":row[5],"priority":row[6]})
                conn.close()
                print(api_data)
                jsonify(api_data)
                return render_template("home.html", title="Homepage", **locals())
        else:
            form_data = request.form.to_dict()
            db_api.add_task(form_data)


#        description = form_data["description"]
#        title = form_data["title"]
#            due_date = form_data["due_date"]
#            due_created = form_data["date_created"]
#        json_data = jsonify(form_data)
#        return json_data
#        post_db_response = requests.post("http://127.0.0.1:5000/tasks", data = json_data)

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
        return jsonify(dummy_api_data)

#    elif request.method == 'POST':
#        db_api.add_task(post_db_response)



if __name__ == "__main__":
    app.run(debug = True)
