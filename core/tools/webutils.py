#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
B→FeelLog - 2021 - por jero98772
B→FeelLog - 2021 - by jero98772
"""
import time
import base64
from hashlib import sha256
import os
def writeTxt(name,content,option = "a"):
	content = str(content)
	with open(name, option) as file:
		file.write(content)
		file.close()
def changeThis(name,old,new,option = "ab+",replaceTo="<!--this-->"):
	oldString = replaceTo+old+replaceTo
	newString = replaceTo+new+replaceTo
	newContent = readFile(name).replace(oldString,newString)
	#add integrate a main.py
	writeTxt(name,newContent,option="w")
def writeblog(name,content,option = "ab+",replaceTo="<!--addition-->"):
	if content == "":
		initTemplate = "{% extends  'template.html'%}{% block content %}"
		endTemplate = "{% endblock %}"
		content = initTemplate+content+replaceTo+endTemplate
		newContent =  content 
	else:
		newContent = readFile(name).replace(replaceTo,content+replaceTo)
	writeTxt(name,newContent,option="w")
def hashStrHex(password):
	password = str(password)
	hashPassowrd = str(sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
def upadateAuthor(author,newAuthor,path ):
	newContent = readFile(path).replace(author,newAuthor)
	writeTxt(path,newContent,option="w")
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
def manageTranslate(writeIn,translateTo):
	try:
		translateTo[translateTo.index(writeIn)] = ""
	except:
		pass 
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
def manyblogs(path):
	return len(os.listdir(path))
def blogsview(path,app):
	blogpath = path[path.index("templates/")+len("templates/"):] 
	blogs = os.listdir(path)
	for blog in blogs:
		@app.route("/"+blogpath+str(blog), endpoint=blog[:-5] )
		def site():
			return render_template(blogpath+blog) 
	return site()
def genBlogPreview(name,path=""):
	txt = f'\n\t@app.route("/blog/{name}")\n\tdef {str(name[:-5]).replace("/","")}():\n\t\treturn render_template("blog/{name}")'
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
def blogNames(path,tag = ".html"):
	folderFiles = os.listdir(path)
	files = []
	for i in folderFiles:
		if i[-5:] != tag:
			name =  [i+"__"+ii for ii in os.listdir(path+i)] 
			files += name
		else: 
			files +=  [i]
	return files
def filesInFolders(path,tag = ".html"):
	folderFiles = os.listdir(path)
	files = []
	for i in folderFiles:
		if i[-5:] != tag:
			name =  [i+"/"+ii for ii in os.listdir(path+i)] 
			files += name
		else: 
			files +=  [i]
	return files
def blogsNames(path,tag = ".html"):
	blogs = os.listdir(path)
	names = []
	for i in blogs:
		if i[-5:] == tag:
			names.append(i[:-5])
		else:
			names.append(i)
	return names
def getPrimaryLanguage(languages):
	for language in languages:
		if language[0].isupper():
			return language
			break
def clearName(txt,exludeChars,notavailablenames,limit=0,errorMsg = ["the name have some exlude characters , plese only use numeric and upper or lower case letters","the name exlucde the number of characters, limit is: "]):
	if txt in notavailablenames:
		msg = errorMsg[0]
		okName = False
	if exludeChars != "":
		for i in txt:
			if i in exludeChars:
				msg = errorMsg[0]
				okName = False
				break
			else: 
				msg = ""
				okName = True	
	if len(txt) > limit :
		okName = False
		msg = errorMsg[1]+str(limit)+" of characters"
	return okName ,msg
def createFile(name):
	content =str(content)
	with open(name, 'x') as file:
		file.write(" ")
		file.close()
def changeName(txt):
	newname = ""
	if txt[-1:] == " ":
		newname = txt[:-1]
	newname.replace(" ","_")
	return newname
def deleteFiles(path,selectedFiles):
	for i in selectedFiles:
		os.remove(path+file)
def BilingueName2path(names,replacechar = "__"):
	for i in range(len(names)):
		names[i] = names[i].replace(replacechar,"/")
def moveFiles(path,name,replacechar = "__"):
	directoriName = name.replace(replacechar,"/")
	fileName =  name[:name.index(replacechar)]+".html"
	numOfFiles = len(os.listdir(directoriName))
	if numOfFiles:
		createFile(path+fileName)
		#replace content
	elif numOfFiles > 2:
		 pass
		#true , move dir
	#if 2 langues is name/lange.html , if 1 lange 1 name.html
def deleteAndMove(deletename,path,names):
	print(names,deletename,path)
	for file in deletename:
		print("remove:"+path+file.replace("__","/"))#os.remove(path+file)
		#print("move: "+file)
		moveFiles(path,file)
	#deleteFiles(path,deletename)
	BilingueName2path(names)
	print(names,deletename)
#	if <name>[:langue] 

	#move
	#if "__" in name:

#how i know is 2 files? slice str and before is folder ...

