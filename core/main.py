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
#LANGUAGETAG = "main_langue_"
TOKEN = readLine(TOKENPATH)
AUTHOR = readLine(AUTHORFILE)
BLOGS = blogNames(BLOGPATH)
BLOGSFILES = filesInFolders(BLOGPATH)
print(BLOGSFILES)
SUPORTEDLANGUAGES = ["No translate","spanish","english","dutch"]
#DBCONFIG = "topicsConfig"
if os.path.isfile(BLOGFILE):
	try:
		from .blogs import blogs 
		from .blogs import app as appblogs 
		joinWebpage(BLOGSFILES,appblogs,app,url=BLOGWEBDIR)
	except:
		updateBlog(BLOGSFILES,BLOGFILE)
class webpage:
	app.secret_key = TOKEN
	print("\n* Configuration token:\n"+TOKEN+"\n","go to :\n\n\tlocalhost:9600"+BLOGWEBDIR+TOKEN+"/\n\nto get acces to configuration , rember your token is\n\n\t"+TOKEN,"\n")
	@app.route(INDEX,methods=['POST','GET'])
	def index():
		session["author"] = AUTHOR
		updateBlog(BLOGSFILES,BLOGFILE)
		#joinWebpage(BLOGS,appblogs,app,url=BLOGWEBDIR)
		return render_template("index.html", topics = BLOGS,topicsaddres =BLOGSFILES, name = AUTHOR )
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
				if os.path.isdir(BLOGPATH+name):#translate because is dir 
					files = os.listdir(BLOGPATH+name)
					#manageTranslate(str(session["translateFrom"])+".html",languages)
					print("trasnlate")
					for file in files:
						print(file[:-5],"for")
						if file[0].isupper():
							print(file,"main")
							mainLangue = file[0].lower()+file[1:-5]
							print("mainLangue is "+file)
							content = doHtml(txtp,txtq,txtid,AUTHOR)
							writeblog(BLOGPATH+name+"/"+file,content)	
						else:
							transalateTo = file[:-5]
							print("trasnlate to"+transalateTo)
					else:
						txtp_translated = webTranslate(txtp,mainLangue,transalateTo)
						txtq_translated = webTranslate(txtq,mainLangue,transalateTo)
						content = doHtml(txtp_translated,txtq_translated,txtid,AUTHOR)
						writeblog(BLOGPATH+name+"/"+transalateTo+".html",content)
						print("trasnlate")
						print("end trasnlate")
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
			msg = ""
			if request.method == "POST":
				name = request.form["name"]
				translateTo = request.form["translate_to"]
				translateFrom = request.form["translate_from"]
				if SUPORTEDLANGUAGES[0] == translateTo or translateTo == translateFrom:
					msg = " was create a topic without trasnlate option"+"\nyou can not translate from "+translateTo+" to "+translateFrom
					writeblog(BLOGPATH+name+".html","")
					#return redirect(BLOGWEBDIR+"config.html")
				else:
					os.mkdir(BLOGPATH+name)
					writeblog(BLOGPATH+name+"/"+translateFrom[0].upper()+translateFrom[1:]+".html","")
					writeblog(BLOGPATH+name+"/"+translateTo+".html","")
			return render_template("config/createNewTopic.html" ,languages = SUPORTEDLANGUAGES, msg = msg)
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
				return redirect(BLOGWEBDIR+"author.html")
			else:
				msg = "Invalid token"
		return render_template("config/addkey.html",error=msg)
	@app.route("/blog/testLangue/english.html")
	def testLangueenglish():
		return render_template("blog/testLangue/english.html")
	@app.route("/blog/testLangue/Spanish.html")
	def testLangueSpanish():
		return render_template("blog/testLangue/Spanish.html")