from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Flask App! Visit <a href='http://127.0.0.1:5000/hello/Jackson/'>http://127.0.0.1:5000/hello/Jackson/</a> "
 
@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
        'test.html',name=name)


@app.route("/hi")
def hello_world():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()
