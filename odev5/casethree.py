from flask import Flask, request, jsonify,render_template,session,redirect,url_for,send_from_directory
from pymongo import MongoClient
app = Flask(__name__)
host = "localhost"
port= 27017
username = "alihandurmus1907"
password = "aF2QbJmfM65bZgkW"
database = 'flaskmongodb'

connection = MongoClient(host,port,username=username,password=password)
db = connection[database]
UsersCollection = db['Users']
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/echo/<text>")
def repeat(text):
    return render_template("text.html",txt=text)
@app.route('/adduser',methods=['POST'])
def add_user():
    user_data = request.json
    UsersCollection.insert_one(user_data)
    return jsonify({'message':'Kullanıcı başarıyla eklendi'})
@app.route('/25',methods=['GET'])
def get_users_over_25():
    users = UsersCollection.find({'age':{'$gt':25}})
    user_list = []
    for user in users:
        user_list.append(user)
    return jsonify(user_list)
@app.route('/',methods=['GET'])
def get_all_user():
    users = UsersCollection.find({})
    user_list = []
    for user in users:
        user_list.append(user)
    return jsonify(user_list),200
@app.route('/deleteuser',methods=['POST','DELETE'])
def delete_user():
    user_id = request.args.get('id')
    UsersCollection.delete_one({'_id':user_id})
    return jsonify({'message':'Kullanıcı başarıyla silindi'})
if __name__=="__main__":
    app.run(host='localhost',port=5000)

#Dependencies
from flask import Flask,render_template,session,redirect,url_for,jsonify,send_from_directory


# App stuff


#Routers










