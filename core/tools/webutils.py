#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
B→FeelLog - 2021 - por jero98772
B→FeelLog - 2021 - by jero98772
"""
import time
import base64
import hashlib
import os
def writeTxt(name,content,option = "a"):
	content = str(content)
	with open(name, option) as file:
		file.write(content)
		file.close()
def writeblog(name,content,option = "ab+",replaceTo="<!--addition-->"):
	"""
	content = content + "\n<!--addition-->"
	with open(name, option) as file:
		file.readLines()#.replace("<!--addition-->",content)
		file.write()
		file.close()
	"""
	try:
		initTemplate = "{% extends  'template.html'%}{% block content %}"
		endTemplate = "{% endblock %}"
		newContent = readFile(name).replace(replaceTo,content+replaceTo)
	except:
		newContent = replaceTo.replace(replaceTo,content+replaceTo)
	writeTxt(name,newContent,option="w")
def hashStrHex(password):
	password = str(password)
	hashPassowrd = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
def webTranslate(txt,writeIn,translateTo):
	"""
	webTranslate(txt,writeIn,translateTo )
	  - txt			  -text to trasnlate
	  - writeIn		  -in which language is it written
	  - translateTo	  -language to be translated
	rember language prefix
	en -> english
	es -> spanish 
	...
	"""
	from deep_translator import GoogleTranslator 
	translatedTxt = GoogleTranslator(source=writeIn, target=translateTo).translate(txt)
	return translatedTxt
#txt = "mi amigo fue la casa del perro, cuando descubrio que una serpiente se lo comio";print(webTranslate(txt,"es","en"))
#txt to test
def doHtmlInit(name,content):
	return f"""
	<!DOCTYPE html>
	<html lang="en">
		<meta charset="UTF-8"> 
		<head>
			<title>blog {name}</title>
		</head>
		<body>
				<h1>{name}</h1>
				<br>
			<center>
				<hr>
				{content}
			</center>
		</body>
	</html>
	"""
def doHtml(txtp,txtq,id,who):
	now = time.ctime()
	return f"""
	<div id="{id}">
	<h2>{txtp}</h2>
	<br>
	<table width = "420">
		<tr>
			<td>
				<p>{txtq}</p>
			</td>
		</tr>
	</table>
	<p>{now},by {who}.</p>
	</div>
	<hr>
	"""
def readFile(name):
	with open(name, 'r') as file:
		content = ""
		for i in file.readlines():
			content += str(i).replace("\n","")
		return content
def readLine(name):
	with open(name, 'r') as file:
		return file.readline()
def readCode(name):
	content = ""
	with open(name, 'r') as file:
		for i in file.readlines():
			content += str(i)
		return content
def genToken():
	now = time.ctime()
	return hashStrHex(str(now))
def genTokenFile(filename):
	try :
		if readLine(filename) == "":
			pass
	except:
		writeTxt(filename,genToken())
def initTopic(name):
	os.mkdir("../templates/")
def blogsview(path,app):
	blogpath = path[path.index("templates/")+len("templates/"):] 
	blogs = os.listdir(path)
	for blog in blogs:
		@app.route("/"+blogpath+str(blog), endpoint=blog[:-5] )
		def site():
			return render_template(blogpath+blog) 
	return site()
def genBlogPreview(name,):
	txt = f'\n\t@app.route("/blog/{name}")\n\tdef {name[:-5]}():\n\t\treturn render_template("blog/{name}")'
	return txt
def updateBlog(dirs,dataDir):
    newCode = """from flask import Flask, render_template
app = Flask(__name__)
class blogs():"""
    for i in dirs:
        newCode += genBlogPreview(i)
    writeTxt(dataDir,newCode,"w")
    #tryng to move to emacs is ... a disasters with tabs 
def joinWebpage(direccions,webApp,actualapp,url=""):	
		for webroute in direccions:		
			@actualapp.route(url+webroute, endpoint=webroute , methods=['GET','POST'])
			def site():
				return webApp
		return site()