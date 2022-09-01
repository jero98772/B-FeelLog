#!/usr/bin/env python
# -*- coding: utf-8 -*-"
"""
B→FeelLog - 2021 - por jero98772
B→FeelLog - 2021 - by jero98772
"""
from flask import Flask, render_template ,request,session,redirect,send_file,send_from_directory
from .tools.webutils import *
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
EXCLUDEDCHARACTER = "#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
BLOGWEBDIR = "/blog/"
TEMPLATE = "core/templates/template.html"
BLOGPATH = "core/templates/blog/"
AUTHORFILE = "data/authorfile.txt"
TOKENPATH = "data/token.txt"
WHATISFILE = "data/whatisfile.txt"
BLOGFILE = "core/blogs.py"
INDEX = "/blog.html"
FILEUPLOAD = "static/uploads"

FILESONLINE = "core/templates/config/files.html"
app.config['UPLOAD_FOLDER']=FILESONLINE
TOKEN = readLine(TOKENPATH)
AUTHOR = readLine(AUTHORFILE)
USE = readLine(WHATISFILE)
try:
	BLOGS = blogNames(BLOGPATH)
except:
	os.mkdir(BLOGPATH)
BLOGSFILES = filesInFolders(BLOGPATH)
SUPORTEDLANGUAGES = ["No translate","spanish","english","german","basque","italian","russian"]
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
	@app.route(INDEX)
	def index():
		session["author"] = AUTHOR
		updateBlog(BLOGSFILES,BLOGFILE)
		return render_template("index.html", url= BLOGWEBDIR,topics = BLOGS, name = AUTHOR )
	@app.route(BLOGWEBDIR+"/config.html")
	def config():
		return render_template("config/configmenu.html")
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
				if os.path.isdir(BLOGPATH+name):#translate because is dir 
					files = os.listdir(BLOGPATH+name)
					for file in files:
						if file[0].isupper():
							mainLangue = file[0].lower()+file[1:-5]
							content = doHtml(txtp,txtq,txtid,AUTHOR)
							writeblog(BLOGPATH+name+"/"+file,content)	
						else:
							transalateTo = file[:-5]
					else:
						txtp_translated = webTranslate(txtp,mainLangue,transalateTo)
						txtq_translated = webTranslate(txtq,mainLangue,transalateTo)
						content = doHtml(txtp_translated,txtq_translated,txtid,AUTHOR)
						writeblog(BLOGPATH+name+"/"+transalateTo+".html",content)
				else:
					content = doHtml(txtp,txtq,txtid,AUTHOR)
					writeblog(BLOGPATH+name+".html",content)
			return render_template("config/addData.html",blogs = blogsNames(BLOGPATH))
	@app.route(BLOGWEBDIR+"/createNewTopic.html",methods=['POST','GET'])	
	def CreateNewTopic():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root."
		else:
			msg = ""
			if request.method == "POST":
				name = str(request.form["name"])
				nameIsOk ,errormsg = clearName(name,EXCLUDEDCHARACTER,BLOGS)
				if nameIsOk:
					name = changeName(name)
				try :
					translateTo = request.form["translate_to"]
				except:
					translateTo = SUPORTEDLANGUAGES[0]
				translateFrom = request.form["translate_from"]
				if translateTo == translateFrom:
					msg = "you can not translate from "+translateTo+" to "+translateFrom
				if SUPORTEDLANGUAGES[0] == translateTo or translateTo == translateFrom:
					msg = " was create a topic without trasnlate option"
					writeblog(BLOGPATH+name+".html","")
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
				if request.form.get('new Token'):
					newToken = genToken()
					writeTxt(TOKENPATH,newToken,"w")
					session["loged"] = False
					return "you new Token is :\n\t"+newToken
				if request.form.get('custom Token'):
					writeTxt(TOKENPATH,request.form['customTokenValue'],"w")
					session["loged"] = False
					return "remember, save your token"
				return redirect(INDEX)
			return render_template("config/token.html")
	@app.route(BLOGWEBDIR+"/author.html",methods=['POST','GET'])
	def author():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root.\n please get loged with your token!!"
		else:
			if request.method == "POST":
				newAuthor = request.form['author']
				upadateAuthor(AUTHOR,newAuthor,TEMPLATE)
				writeTxt(AUTHORFILE,newAuthor,"w")
				return redirect(INDEX)
			return render_template("config/author.html",defautlAuthor = AUTHOR)
	@app.route(BLOGWEBDIR+"/thisSite.html",methods=['POST','GET'])
	def thisSite():
		if not session.get("loged"):
			return "error: you cannot perform this operation unless you are root.\n please get loged with your token!!"
		else:
			if request.method == "POST":
				whatis = request.form['this']
				upadateAuthor(USE,whatis,TEMPLATE)
				writeTxt(WHATISFILE,whatis,"w")
				return redirect(INDEX)
			return render_template("config/thisSite.html",defautlUse = USE)

	@app.route(BLOGWEBDIR+TOKEN+"/",methods=['POST','GET'])
	def trueLoged():
		msg = ""
		if request.method == "POST":
			if request.form["key"] == TOKEN:
				session["loged"] = True
				return redirect(BLOGWEBDIR+"token.html")
			else:
				msg = "Invalid token"
		return render_template("config/addkey.html",error=msg)
	@app.route(BLOGWEBDIR+"/deleteFiles.html",methods = ["POST","GET"])
	def deleteFiles():		
		msg = ""
		if request.method == "POST":
			deletechecks = request.form.getlist("delete")
			deleteAndMove(deletechecks,BLOGPATH,BLOGS) 
			deletemsg = str(deletechecks)[2:-2]
			msg =  "file removed are :"+deletemsg
		return render_template("config/deleteFiles.html",blogs = BLOGS,msg = msg)
	@app.route(BLOGWEBDIR+"/uploadFile.html",methods = ["POST","GET"])
	def uploadFile():
		if os.path.exists("static") and os.path.exists(FILEUPLOAD):		
			if request.method == "POST":
				if not os.path.exists(FILESONLINE):
					writeblog(FILESONLINE,"",option = "w")
				file = request.files["file"]
				ext = getExt(file)
				name = str(len(os.listdir(FILEUPLOAD)))+ext
				file.save(FILEUPLOAD+"/"+name)
		else:
			os.mkdir(FILEUPLOAD)
			os.mkdir("static")
		return render_template("config/uploadFile.html",msg = "")
	@app.route(BLOGWEBDIR+'/files.html', methods=['GET', 'POST'])
	def file():
		directory=os.getcwd()+"/"+FILEUPLOAD
		directories=os.listdir(directory)
		files=list(filter(isFile,directories))
		files.sort()
		return render_template("config/files.html",files=files,whatisthis=BLOGWEBDIR)
	@app.route(BLOGWEBDIR+'/download/<string:filename>', methods = ["GET", "POST"])
	def download(filename):
		filename=FILEUPLOAD+"/"+filename
		uploads = os.path.join(app.root_path+"/..", "")
		return send_from_directory(directory=uploads,path=filename,as_attachment=True)
	
