# Maintain a folder named  `templates` for storing the html pages

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/child1")
def inherited():
	return render_template("child1.html")

@app.route("/<user>")
def home(user):
	return render_template("index.html",content=user, r=2) # We can pass multiple values here
	# We can pass even a list as values
	# Eg - return render_template("index.html",value=['s','d','f']) . In corresponding HTML page we can access this list via 
	# mentioning as {{value}} within a for loop to traverse all the elements inside the list

