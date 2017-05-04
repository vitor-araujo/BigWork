from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/mission")
def mission():
    return render_template("mission.html")

@app.route("/company")
def company():
    return render_template("company.html")

@app.route("/intel")
def intel():
    return render_template("intel.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/techintel")
def techintel():
    return render_template("techintel.html")

@app.route("/usercv")
def usercv():
    return render_template("usercv.html")

if __name__ == "__main__":
  app.run(host="192.168.0.193")