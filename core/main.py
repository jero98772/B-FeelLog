#!/usr/bin/env python
# -*- coding: utf-8 -*-"
"""
B→FeelLog - 2021 - por jero98772
B→FeelLog - 2021 - by jero98772
"""
from flask import Flask, render_template ,request,session,redirect
from .tools.webutils import *
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
BLOGWEBDIR = "/blog/"
BLOGPATH = "core/templates/blog/"
AUTHORFILE = "data/authorfile.txt"
TOKENPATH = "data/token.txt"
BLOGFILE = "core/blogs.py"
INDEX = "/blog.html"
TOKEN = readLine(TOKENPATH)
AUTHOR = readLine(AUTHORFILE)
BLOGS = os.listdir(BLOGPATH)
#DBCONFIG = "topicsConfig"
if os.path.isfile(BLOGFILE):
	try:
		from .blogs import blogs 
		from .blogs import app as appblogs 
		joinWebpage(BLOGS,appblogs,app,url=BLOGWEBDIR)
	except:
		updateBlog(BLOGS,BLOGFILE)
class webpage:
	app.secret_key = TOKEN
	print("\n* Configuration token:\n"+TOKEN+"\n","go to :\n\n\tlocalhost:9600"+BLOGWEBDIR+TOKEN+"/\n\nto get acces to configuration , rember your token is\n\n\t"+TOKEN,"\n")
	@app.route(INDEX,methods=['POST','GET'])
	def index():
		updateBlog(BLOGS,BLOGFILE)
		return render_template("index.html", topics = BLOGS, name = AUTHOR )
	@app.route(BLOGWEBDIR+"/add.html",methods=['POST','GET'])	
	def add():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			if request.method == "POST":
				txtp =request.form["txtp"]
				txtq = request.form["txtq"]
				txtid = request.form["id"]
				name = request.form["destiantion"]
				#if os.path.isfile(BLOGFILE):
				content = doHtml(txtp,txtq,txtid,AUTHOR)
				writeblog(BLOGPATH+name+".html",content)
			return render_template("config/addData.html",webs= os.listdir(BLOGPATH))
	@app.route(BLOGWEBDIR+"/createNewTopic.html",methods=['POST','GET'])	
	def CreateNewTopic():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			if request.method == "POST":
				topicName = request.form["topicName"]
				template = request.form["template"]
			return render_template("config/createNewTopic.html")
	@app.route(BLOGWEBDIR+"/token.html",methods=['POST','GET'])
	def token():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root.\n please get loged with your token!!"
		else:
			if request.method == "POST":
				if request.form['new Token'] == 'new Token':
					writeTxt(TOKENPATH,genToken(),"w")
					session["loged"] = False
				elif request.form['custom Token'] == 'custom Token':
					writeTxt(TOKENPATH,request.form['customTokenValue'],"w")
					session["loged"] = False
				return redirect(INDEX)
			return render_template("config/token.html")
	@app.route(BLOGWEBDIR+"/author.html",methods=['POST','GET'])
	def author():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root.\n please get loged with your token!!"
		else:
			if request.method == "POST":
				if request.form['who'] == 'who':
					author = request.form['author']
					writeTxt(AUTHORFILE,author,"w")
					session["author"] = author
				return redirect(INDEX)
			return render_template("config/author.html",defautlAuthor = AUTHOR)
	@app.route(BLOGWEBDIR+"/config.html",methods=['POST','GET'])
	def config():
		return render_template("config/configmenu.html")
	@app.route(BLOGWEBDIR+TOKEN+"/",methods=['POST','GET'])
	def trueLoged():
		msg = ""
		if request.method == "POST":
			if request.form["key"] == TOKEN:
				session["loged"] = True
				return redirect(BLOGWEBDIR+"/customise.html")
			else:
				msg = "Invalid token"
		return render_template("config/addkey.html",error=msg)
