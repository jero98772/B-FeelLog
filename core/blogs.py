from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/blog1Translations_spanish.html")
	def blog1Translations_spanish():
		return render_template("blog/blog1Translations_spanish.html")
	@app.route("/blog/blog1Translations_english.html")
	def blog1Translations_english():
		return render_template("blog/blog1Translations_english.html")
	@app.route("/blog/test.html")
	def test():
		return render_template("blog/test.html")
	@app.route("/blog/blog_test.html")
	def blog_test():
		return render_template("blog/blog_test.html")