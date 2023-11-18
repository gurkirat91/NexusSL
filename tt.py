from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)


dp = {'kirat@gmail.com': '1234','rupinder@gmail.com' : '1234'}



@app.route("/",methods=["POST","GET"])
def login():
    if(request.method=="POST"):
        name = request.form["username"]
        password = request.form["password"]
        if name not in dp:
            # print("invalid user")
            return render_template("login.html",info="invalid user")
        else:
            if dp[name] != password:
                # print("wrong password")
                return render_template("login.html",info="wrong password")
            else:
                return redirect(url_for("home"))
    else:
        return render_template("login.html")
    # if(request.method=="POST"):           #go to home after login
    #     usr=request.form["username"];
    #     print(usr)
    #     return redirect(url_for("home"))
    # else:
    #     return render_template("login.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/home")
def home():
    return render_template("home_sign_to_text.html")

@app.route("/text_to_sl",methods=["POST","GET"])
def text_to_sl():
    if (request.method == "POST"):
        name = request.form["tts"]
        print(name)
    return render_template("text_to_sign.html")

if __name__== "__main__":
    app.run(debug=True)

















