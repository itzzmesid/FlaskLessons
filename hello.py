from flask import Flask, redirect, url_for
from markupsafe import escape 	
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<h1>Hello World</h1>"
 
@app.route("/<name>")
def user(name):
	#return f"Hello {name}"
	return f"Hello, {escape(name)}"
# < > grabs any value after / 
# and passes it to name variable
# Hence it is imp to verify its integrity
# We use escape to prevent malicious html codes being executed.

# Implementing Redirecting
@app.route("/admin")
def rd():
	return redirect(url_for("hello_world"))
# Here whenever we goes to /admin , 
# we will get redirected to hello_world function and the
# func displays the contents in it.









"""
How to run the file?
$ export FLASK_APP=hello
$ flask run
"""