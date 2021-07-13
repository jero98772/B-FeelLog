from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/tema1/german.html")
	def tema1german():
		return render_template("blog/tema1/german.html")
	@app.route("/blog/tema1/Spanish.html")
	def tema1Spanish():
		return render_template("blog/tema1/Spanish.html")