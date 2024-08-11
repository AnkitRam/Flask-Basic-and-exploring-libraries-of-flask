from flask import Flask # type: ignore

app = Flask(__name__) #creating object and variable

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Welcome {name.title()}!</h1>"

@app.route("/addition/<int:num>")
def addition(num):
    return f"<h1> Input is {num}, output is {num +10} </h1>"

@app.route("/about")
def about():
    return "<h1>Welcome to About Page</h1>"

if __name__ == "__main__":
    app.run(debug=True) #running the application in debug mode
