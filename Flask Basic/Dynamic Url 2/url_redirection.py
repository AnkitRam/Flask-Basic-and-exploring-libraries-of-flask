from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Home Page!</h1>"

@app.route("/pass")
def passed():
    return "<h1> congrate you are passed!</h1>"

@app.route("/fail")
def fail():
    return "<h1> Sorry you are Failed!</h1>"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num <30:
        return redirect(url_for("fail"))
    else:
        time.sleep(1)
        return redirect(url_for("passed"))




if __name__ == "__main__":
    app.run(debug=True)