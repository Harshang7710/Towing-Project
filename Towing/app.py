from flask import Flask,render_template,request
from pymongo import MongoClient

app = Flask("login")
client = MongoClient("mongodb://127.0.0.1:27017")
db = client["Harshang"]
collection = db["authentication"]

@app.route("/")
def login():
    return render_template("start.html")

@app.route("/uselogin")
def uselogin():
    return render_template("userlogin.html")


@app.route("/servicemanlogin")
def servicemanlogin():
    return render_template("servicemanlogin.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/registration1")
def registration1():
    return render_template("registration1.html")



#@app.route("/decision", methods=["POST"])
#def decision():
#    email = request.form.get("email")
#    passwd = request.form.get("password")
#    #user=request.form.get
#    output=collection.find({"email": email})
#    for i in output: 
#        output = i['password']
#    if output == passwd:
#            return render_template("index.html")
#    else:
#            return render_template("fail.html")


@app.route("/decision", methods=["POST"])
def decision():
    email = request.form.get("email")
    passwd = request.form.get("password")
    
    user = collection.find_one({"email": email})
    
    if user and user.get("name"):
        name = user["name"]
        vehicleno=user['vehicleno']
        
        if user.get("password") == passwd:
            return render_template("index.html", name=name,vehicleno=vehicleno)
    
    return render_template("fail.html")


@app.route("/SVCdecision", methods=["POST"])
def SVCdecision():
    email = request.form.get("email")
    passwd = request.form.get("password")
    output=collection.find({"email": email})
    for i in output: 
        output = i['password']
    if output == passwd:
            return render_template("servicemanindex.html")
    else:
            return render_template("fail.html")

@app.route("/createUser", methods=["POST"])
def createUser():
    email = request.form.get("email")
    passwd = request.form.get("password")
    name = request.form.get("name")
    phno = request.form.get("phno")
    vehicleno = request.form.get("vehicleno")
    collection.insert_one({"name": name,"password": passwd,"email": email,
                           "phno": phno,"vehicleno":vehicleno})
    return render_template("start.html")

@app.route("/mainIndex")
def index():
    return render_template("index.html")

@app.route("/servicemanindex")
def servicemanindex():
    return render_template("servicemanindex.html")


@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/feedback1")
def feedback1():
    return render_template("feedback1.html")


@app.route("/contact1")
def contact1():
    return render_template("contact1.html")


@app.route("/sendMsg")
def sendMsg():
    return render_template("sendMsg.html")

app.run(debug=True)