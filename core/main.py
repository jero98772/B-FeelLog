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
BLOGS = filesInFolders(BLOGPATH)
SUPORTEDLANGUAGES = ["spanish","english","dutch"]
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
		session["author"] = AUTHOR
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
				print("1")
				if os.path.isdir(BLOGPATH+name):
					languages = os.listdir(BLOGPATH+name)
					manageTranslate(str(session["translateFrom"])+".html",languages)
					print("trasnlate")
					for language in languages:
						print(language[:-5])
						txtp_translated = webTranslate(txtp,session["translateFrom"],language)
						txtq_translated = webTranslate(txtq,session["translateFrom"],language)
						content = doHtml(txtp_translated,txtq_translated,txtid,AUTHOR)
						writeblog(BLOGPATH+name+"/"+language,content)
						print("trasnlate")
					else:
						print("end trasnlate")
						content = doHtml(txtp,txtq,txtid,AUTHOR)
						writeblog(BLOGPATH+name+"/"+str(session["translateFrom"])+".html",content)	
				else:
					content = doHtml(txtp,txtq,txtid,AUTHOR)
					writeblog(BLOGPATH+name+".html",content)
					print("out")
				#os.listdir(name)
				#acceder a los directiros 
				#guradar 

			return render_template("config/addData.html",blogs = blogsNames(BLOGPATH))
	@app.route(BLOGWEBDIR+"/createNewTopic.html",methods=['POST','GET'])	
	def CreateNewTopic():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			if request.method == "POST":
				translateFrom = request.form["translate_from"]
				translateTo = request.form["translate_to"]
				session["translateFrom"] = translateFrom
			return render_template("config/createNewTopic.html" ,languages = SUPORTEDLANGUAGES)
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
				return redirect(BLOGWEBDIR+"configmenu.html")
			else:
				msg = "Invalid token"
		return render_template("config/addkey.html",error=msg)
