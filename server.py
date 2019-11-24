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
    global message_list
    message_list = list()
    with open("loginfile.csv") as login:
        loginfile = csv.DictReader(login)
        for i in loginfile:
            users.append(i)
    with open("message.csv") as messages:
        messages_user = csv.DictReader(messages) 
        for j in messages_user:
            message_list.append(j)



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
        val = str(uuid.uuid4())
        id = val
        username = request.json['username']
        password = request.json['password']
        writer.writerow({"id":id,"username":username,"password":password})
    return json.dumps({"success":"success"+username,"username":username})

@app.route("/login",methods = ["POST"])                             # Login using the Users global List                            
def login_route():
    read_user()
    username = request.json["username"]
    password = request.json["password"]
    for i in users:
        if i["username"] == username and i["password"]:
            return json.dumps({"success":i})
    
    return json.dumps({"success":"Wrong Username/Password"})


@app.route("/sendmessage",methods = ["POST"])                                                   #Sening messages to user with message id
def message():
    read_user()
    try:
        with open("message.csv") as reader:
            fieldnames = ['id','msg_id','msg','sender','receiver']
    except FileNotFoundError:
        with open("message.csv","w") as writer:
            fieldnames = ['id','msg_id','msg','sender','receiver']
            writer = csv.DictWriter(writer,fieldnames = fieldnames)
            writer.writeheader()
    with open("message.csv","a") as writer:
        writer = csv.DictWriter(writer,fieldnames=fieldnames)
        if not writer.fieldnames == fieldnames:
            writer.writeheader()
        val = str(uuid.uuid4())
        print(val)
        msg = request.json['msg']
        id = int(request.json['id'])
        sender = request.json['sender']
        receiver = request.json['receiver']
        writer.writerow({'id':id,'msg_id':val,'msg':msg,'sender':sender,'receiver':receiver})
    return "msg sent"

@app.route("/showmessage",methods =["POST"])                                                    #Showmessage
def show_msg():
    read_user()
    messages = list()
    username = request.json['username']
    for i in message_list:
        if i["receiver"] == username:
            messages.append(i)
    return json.dumps({"message_list":messages})



