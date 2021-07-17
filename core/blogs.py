from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/transalatesen/english.html")
	def transalatesenenglish():
		return render_template("blog/transalatesen/english.html")
	@app.route("/blog/transalatesen/Spanish.html")
	def transalatesenSpanish():
		return render_template("blog/transalatesen/Spanish.html")
	@app.route("/blog/no translate.html")
	def no translate():
		return render_template("blog/no translate.html")