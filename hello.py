"""
How to run the file?
$ export FLASK_APP=hello
$ flask run
"""

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
# we will get redirected to hello_world function and the func displays the contents in it.

# Now imagine we need to redirect to user() and print `Hello Admin`. So we have to give `return redirect(url_for("user"))`.
# But how will we pass the name as `Admin`? For that , we will explicitly pass the value to the function param like below:
# return redirect(url_for("user",name="Admin"))

@app.route('/post/<int:post_id>') # -> http://127.0.0.1:5000/post/1
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'