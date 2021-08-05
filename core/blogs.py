from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/siolo.html")
	def siolo():
		return render_template("blog/siolo.html")
	@app.route("/blog/no traducir.html")
	def no traducir():
		return render_template("blog/no traducir.html")
	@app.route("/blog/siolo/english.html")
	def sioloenglish():
		return render_template("blog/siolo/english.html")
	@app.route("/blog/siolo/Spanish.html")
	def sioloSpanish():
		return render_template("blog/siolo/Spanish.html")
	@app.route("/blog/otra/english.html")
	def otraenglish():
		return render_template("blog/otra/english.html")
	@app.route("/blog/otra/Spanish.html")
	def otraSpanish():
		return render_template("blog/otra/Spanish.html")
	@app.route("/blog/topic1/english.html")
	def topic1english():
		return render_template("blog/topic1/english.html")
	@app.route("/blog/topic1/Spanish.html")
	def topic1Spanish():
		return render_template("blog/topic1/Spanish.html")