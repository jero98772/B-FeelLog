from flask import Flask, render_template
app = Flask(__name__)
class blogs():
	@app.route("/blog/test.html")
	def test():
		return render_template("blog/test.html")
	@app.route("/blog/blog_test.html")
	def blog_test():
		return render_template("blog/blog_test.html")