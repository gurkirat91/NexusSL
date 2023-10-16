from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def login():
    if(request.method=="POST"):           #go to home after login
        usr=request.form["username"];
        print(usr)
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")
if __name__== "__main__":
    app.run(debug=True)