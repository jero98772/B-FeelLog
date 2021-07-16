from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/tarslate/english.html")
	def tarslateenglish():
		return render_template("blog/tarslate/english.html")
	@app.route("/blog/tarslate/Spanish.html")
	def tarslateSpanish():
		return render_template("blog/tarslate/Spanish.html")
	@app.route("/blog/no langue.html")
	def no langue():
		return render_template("blog/no langue.html")