from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/nuevoconespacioalfinal /german.html")
	def nuevoconespacioalfinal german():
		return render_template("blog/nuevoconespacioalfinal /german.html")
	@app.route("/blog/nuevoconespacioalfinal /Spanish.html")
	def nuevoconespacioalfinal Spanish():
		return render_template("blog/nuevoconespacioalfinal /Spanish.html")
	@app.route("/blog/test2_test_2_espacios_/german.html")
	def test2_test_2_espacios_german():
		return render_template("blog/test2_test_2_espacios_/german.html")
	@app.route("/blog/test2_test_2_espacios_/Spanish.html")
	def test2_test_2_espacios_Spanish():
		return render_template("blog/test2_test_2_espacios_/Spanish.html")
	@app.route("/blog/test_espacios/german.html")
	def test_espaciosgerman():
		return render_template("blog/test_espacios/german.html")
	@app.route("/blog/test_espacios/Spanish.html")
	def test_espaciosSpanish():
		return render_template("blog/test_espacios/Spanish.html")
	@app.route("/blog/Hola_mundo_/german.html")
	def Hola_mundo_german():
		return render_template("blog/Hola_mundo_/german.html")
	@app.route("/blog/Hola_mundo_/Spanish.html")
	def Hola_mundo_Spanish():
		return render_template("blog/Hola_mundo_/Spanish.html")