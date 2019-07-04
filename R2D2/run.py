from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient
import requests
app1 = Flask(__name__)





@app1.route('/')
def index():  
   try: 
       conn = MongoClient() 
       print("Connected successfully!!!") 
   except:   
       print("Could not connect to MongoDB")
   db = conn.database
   collection=db.test
   cursor = collection.find()
   d=[]
   for record in cursor: 
       d.append(record) 

   return render_template("index.html",lists=d)

@app1.route("/movies_api_2")
def api_2():
   try: 
       conn = MongoClient() 
       print("Connected successfully!!!") 
   except:   
       print("Could not connect to MongoDB")
   db = conn.database
   collection=db.test
   cursor = collection.find()
   d=[]
   for record in cursor: 
       d.append(record) 
   return render_template("api2.html",lists=d)

@app1.route("/movid",methods=["POST","GET"])
def movid():
   if request.method=="POST":
      idx=request.form['movies']
      return redirect(url_for('movies',mov_id=idx))

@app1.route("/movies/<mov_id>")
def movies(mov_id):
   try: 
       conn = MongoClient() 
       print("Connected successfully!!!") 
   except:   
       print("Could not connect to MongoDB")
   db = conn.database
   collection=db.test
   cursor = collection.find({'id':mov_id})
   d={}
   s=""
   f=0
   for i in cursor:
      d["_id"]=i["_id"]
      d["id"]=i["id"]
      d["title"]=i["title"]
      d["rating"]=i["rating"]
      d["cast"]=i["cast"]
      f+=1
   if (f==0):
         return render_template("error.html")
   return render_template("movie_detail.html",**d)

@app1.route("/movie_find",methods=["POST","GET"])
def movie_find():
   if request.method=="POST":
      idx_name=request.form["movies_name"]
      try: 
          conn = MongoClient() 
          print("Connected successfully!!!") 
      except:   
          print("Could not connect to MongoDB")
      db = conn.database
      collection=db.test
      cursor = collection.find({'title':idx_name})
      d={}
      s=""
      f=0
      for i in cursor:
         d["_id"]=i["_id"]
         d["id"]=i["id"]
         d["title"]=i["title"]
         d["rating"]=i["rating"]
         d["cast"]=i["cast"]
         f+=1
      if (f==0):
         return render_template("error.html")
      return render_template("movie_detail.html",**d)
      
@app1.route("/api1documentation")
def api1documentation():
   return render_template("API1Code.html")

@app1.route("/api2documentation")
def api2documentation():
   return render_template("API2Code.html")

@app1.route("/howtouse")
def howtouse():
   return render_template("ReadMe.html")

@app1.route("/scCode")
def scCode():
   return render_template("ScrapCode.html")
   
if __name__ == '__main__':
   app1.run()
