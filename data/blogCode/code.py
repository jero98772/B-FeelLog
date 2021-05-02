
@app.route(BLOGWEBDIR+"blog3.html")
def blog3():
    return render_template("blog/blog3.html")
    
@app.route(BLOGWEBDIR+"blog2.html")
def blog2():
    return render_template("blog/blog2.html")
    
@app.route(BLOGWEBDIR+"blog4.html")
def blog4():
    return render_template("blog/blog4.html")
    
@app.route(BLOGWEBDIR+"blog1.html")
def blog1():
    return render_template("blog/blog1.html")
    