from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import json
import csv
import uuid


def read_user():                                                     # Reading file to load data for login
    global users
    users = list()
    with open("loginfile.csv") as login:
        loginfile = csv.DictReader(login)
        for i in loginfile:
            users.append(i)



@app.route("/Secureregister",methods = ["POST"])                #Regsitration                            # Id Generated using UUID 
def write_file():
    try:
        with open("loginfile.csv") as reader:
            fieldnames = ['id','username','password']
    except FileNotFoundError:
        with open("loginfile.csv","w") as writer:
            fieldnames = ['id','username','password']
            writer = csv.DictWriter(writer,fieldnames = fieldnames)
            writer.writeheader()
    with open("loginfile.csv","a") as writer:
        writer = csv.DictWriter(writer,fieldnames=fieldnames)
        if not writer.fieldnames == fieldnames:
            writer.writeheader()
        val = int(str(uuid.uuid4()))
        id = val
        username = request.json['username']
        password = request.json['password']
        writer.writerow({"id":id,"username":username,"password":password})
    return json.dumps({"success":"success"+username})

@app.route("/login",methods = ["POST"])                             # Login using the Users global List                            
def login_route():
    read_user()
    username = request.json["username"]
    password = request.json["password"]
    for i in users:
        if i["username"] == username and i["password"]:
            return json.dumps({"success":i})
    
    return json.dumps({"success":"Wrong Username/Password"})

