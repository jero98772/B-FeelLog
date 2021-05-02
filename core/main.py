#!/usr/bin/env python
# -*- coding: utf-8 -*-"
"""
B→FeelLog - 2021 - por jero98772
B→FeelLog - 2021 - by jero98772
"""
from flask import Flask, render_template ,request,session
from .tools.webutils import *
app = Flask(__name__)
BLOGWEBDIR = "/blog/"
BLOGPATH = "core/templates/blog/"
AUTHORFILE = "data/authorfile.txt"
TOKENPATH = "data/token.txt"
BLOGFILE = "core/blogs.py"
#BLOG = readCode(BLOGFILE)
TOKEN = readLine(TOKENPATH)
AUTHOR = readLine(AUTHORFILE)
BLOGS = os.listdir(BLOGPATH)
DBCONFIG = "topicsConfig"
if os.path.isfile(BLOGFILE):
	print("fileok")
	try:
		from .blogs import blogs 
		from .blogs import app as appblogs 
		print("blog")
		print("error")
		joinWebpage(BLOGS,appblogs,app,url=BLOGWEBDIR)
	except:
		updateBlog(BLOGS,BLOGFILE)
		print("no Error")
class webpage:
	app.secret_key = TOKEN
	print("Configuration token:\n"+TOKEN+"\n","go to :\n\tlocalhost:9600"+BLOGWEBDIR+TOKEN+"/\nto get acces to configuration , rember your token is\n\t"+TOKEN)
	@app.route(BLOGWEBDIR[:-1]+".html",methods=['POST','GET'])
	def index():
		updateBlog(BLOGS,BLOGFILE)
		frame = ""
		return render_template("index.html", topics = BLOGS )
	@app.route(BLOGWEBDIR+TOKEN+"/add.html",methods=['POST','GET'])	
	def add():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			if request.method == "POST":
				txtp =request.form["txtp"]
				txtq = request.form["txtq"]
				txtid = request.form["id"]
				name = request.form["destiantion"]
				content = doHtml(txtp,txtq,txtid,AUTHOR)
				writeblog(BLOGPATH+name+".html",content)
			return render_template("config/addData.html",webs= os.listdir(BLOGPATH))
	@app.route(BLOGWEBDIR+TOKEN+"/createNewTopic.html",methods=['POST','GET'])	
	def CreateNewTopic():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			if request.method == "POST":
				topicName = request.form["topicName"]
				template = request.form["template"]
			return render_template("config/createNewTopic.html")
	@app.route(BLOGWEBDIR+TOKEN+"/config.html",methods=['POST','GET'])
	def config():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			if request.method == "POST":
				if request.form['who'] == 'who':
					writeTxt(AUTHORFILE,request.form['author'],"w")
				if request.form['new Token'] == 'new Token':
					writeTxt(TOKENPATH,genToken(),"w")
					session["loged"] = False
				if request.form['custom Token'] == 'custom Token':
					writeTxt(TOKENPATH,request.form['customTokenValue'],"w")
					session["loged"] = False
			return render_template("config/config.html",defautlAuthor = AUTHOR)
	@app.route(BLOGWEBDIR+TOKEN+"/",methods=['POST','GET'])
	def trueLoged():
		if request.method == "POST":
			if request.form["key"] == TOKEN:
				session["loged"] = True
		return render_template("config/addkey.html")
