from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/test_vasco/basque.html")
	def test_vascobasque():
		return render_template("blog/test_vasco/basque.html")
	@app.route("/blog/test_vasco/Spanish.html")
	def test_vascoSpanish():
		return render_template("blog/test_vasco/Spanish.html")
	@app.route("/blog/test_euskera/basque.html")
	def test_euskerabasque():
		return render_template("blog/test_euskera/basque.html")
	@app.route("/blog/test_euskera/Spanish.html")
	def test_euskeraSpanish():
		return render_template("blog/test_euskera/Spanish.html")