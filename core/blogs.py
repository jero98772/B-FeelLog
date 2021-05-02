from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/blog3.html")
	def blog3():
		return render_template("blog/blog3.html")
	@app.route("/blog/blog4.html")
	def blog4():
		return render_template("blog/blog4.html")
	@app.route("/blog/blog5.html")
	def blog5():
		return render_template("blog/blog5.html")
	@app.route("/blog/blog1.html")
	def blog1():
		return render_template("blog/blog1.html")
	@app.route("/blog/blog2.html")
	def blog2():
		return render_template("blog/blog2.html")