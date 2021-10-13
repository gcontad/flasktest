
#!/usr/bin/env python
import pymongo
from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import Flask, render_template,request
#from pymongo import Connection
import os 
#remember you have to add rows to this. 

#one_item={"item":"Raena","id":6}
#db.testpython.insert_one(one_item)
app = Flask(__name__)


client = pymongo.MongoClient("mongodb://172.17.0.2:27017/") 
  
# Database Name 
db = client["testpython"] 
  

#This app section allows the Flask to present a landing page.
@app.route("/")
def index():
   return render_template("index.html")


#This will retrieve the results of the request aboce
@app.route('/result',methods = ['POST', 'GET'])
def result():
   try:
       if request.method == 'POST':
          formdata = request.form["in"]
          result=db.testpython.find_one({"id":int(formdata)})
          result2=result['id']
          return render_template("result.html",result =result['item'], result2=str(result2))
   except Exception as e:
   	  return "<html><center><h1>That user doesn't exist !</h1></center></html>"
 
      
#This site will enter a new user
@app.route("/add_user")
def add_user_land():
   return render_template("add_user.html")    

#This site will enter a new user and then present the user that has been entered
@app.route("/entered_person",methods = ['POST','GET'])
def entered_person():
	try:
	   if request.method=='POST':
	      input0=request.form["name"]
	      input1=request.form["id"]
	      db.testpython.insert_one({"item":str(input0),"id":int(input1)})
	      result3=db.testpython.find_one({"id":int(input1)})
	      return render_template("entered_person.html", entered=result3['item'],personid=result3['id'])
	except Exception as e:
	   return "<html><center> Wrong data dude </center></html>"



if __name__ == '__main__':
   app.run(port=5000,debug=True,host='0.0.0.0')
   




 


 

#db.testpython.updateOne({item:"Johnny"})
#db.testpython.insertOne({item:"JOhnny", "id":1})
