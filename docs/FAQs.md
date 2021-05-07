# FAQs 
**Question:** whe n i run get this error. 

	Traceback (most recent call last):
	  File "/tmp/B-FeelLog/B-FeelLog.py", line 7, in <module>
	    from core.main import webpage
	  File "/tmp/B-FeelLog/core/main.py", line 7, in <module>
	    from flask import Flask, render_template ,request,session,redirect
	ModuleNotFoundError: No module named 'flask'
**Answer:** please run 
	
	python setup.py install

**Question:** when i run the code nothing happend
**Answer:** you go to [localhost:9600/blog.html](http://localhost:9600/blog.html) ,later you need autheticate you in

**Question:** i dont have acces to [configurations](http://localhost:9600/blog/config.html). i have this error:

	please get loged!!
	error: you cannot perform this operation unless you are root.
	please get loged with your token!! 

**Answer:** you need autheticate you with your token , you can autheticate in 

	localhost:9600/blog/<TOKEN>/

replace <TOKEN> for you own token , if frist time use have this Token :

	defaulttoken

come [here](localhost:9600/blog/defaulttoken/)

and you need give you token in the input.

** plese change you toke [http://localhost:9600/blog/token.html](http://localhost:9600/blog/token.html)

**Question:** how i can customise my blog ?
**Answer:** you can change you [token](http://localhost:9600/blog/token.html) and the [author name](http://localhost:9600/blog/author.html) , in the beta of frist version

**Question:** I don't see the changes taking effect
**Answer:** you can go to main ,or [here](http://localhost:9600/blog.html) 

**Question:** how do I create my first entry?
**Answer:** go to Create topic in confgurations ,[here](http://localhost:9600/blog/createNewTopic.html)

**Question:** 
**Answer:** 