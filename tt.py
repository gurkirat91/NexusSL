from flask import Flask,redirect,url_for,render_template,request,Response
from models.main import textToSign
import cv2
import numpy as np


cap = cv2.VideoCapture(0)
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
        input_tts = request.form["tts"]
        print(input_tts)
        textToSign(input_tts)
        return redirect(url_for("text_to_sign_res"))
    else:
        return render_template("text_to_sign.html")


@app.route("/text_to_sign_res",methods=["POST","GET"])
def text_to_sign_res():
    # return render_template("text_to_sign_res.html")
    if (request.method == "POST"):
        input_tts = request.form["tts"]
        print(input_tts)
        textToSign(input_tts)
        return redirect(url_for("text_to_sign_res"))
    else:
        return render_template("text_to_sign_res.html")
#
# @app.route("/text_to_sl",methods=["POST","GET"])
# def text_to_sl():
#     if (request.method == "POST"):
#         input_tts = request.form["tts"]
#         print(input_tts)
#         textToSign(input_tts)
#     return render_template("text_to_sign.html")


def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Preprocess the frame as needed
            frame = cv2.resize(frame, (450,350))
            input_data = np.expand_dims(frame, axis=0)

            # Make predictions
            # predictions = model.predict(input_data)

            # Process predictions and display on the frame as needed

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')






if __name__== "__main__":
    app.run(debug=True)

















