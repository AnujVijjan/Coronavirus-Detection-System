from email.mime.text import MIMEText
from flask import Flask, render_template, request, url_for, flash
from flask_mail import Mail, Message
import pandas as pd
import pickle
import smtplib
import smtplib


app = Flask(__name__)
mail=Mail(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Setting secret key, if you dont while flashing if will show exception.

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if(request.method == "POST"):
        myDict = request.form

        fever = int(myDict['fever'])
        age = int(myDict['age'])
        bodyPain = int(myDict['bodyPain'])
        runnyNose = int(myDict['runnyNose'])
        breathDiff = int(myDict['breathDiff'])

        # Input Features
        inputFeatures = [fever, age, bodyPain, runnyNose, breathDiff]

        # Predicting new Values 
        infProb = clf.predict_proba([inputFeatures])[0][1]

        return render_template('show.html', inf=round(infProb * 100))
    return render_template('index.html')

@app.route('/contact/', methods=["GET", "POST"])
def contact_form():
    if(request.method == "POST"):
        myDict = request.form

        senderName = myDict['name']
        senderEmail = myDict['email']
        senderSubject = myDict['subject']
        senderMessage = myDict['message']
        
        mediatorEmail = 'corona.helpcenter.587@gmail.com'
        receiverEmail = 'anujvijjan10@gmail.com'
        port = 587
        msg = MIMEText(senderMessage)

        msg['Subject'] = senderSubject
        msg['From'] = senderName + " " + senderEmail
        msg['To'] = receiverEmail

        with smtplib.SMTP('smtp.gmail.com', port) as server:
            server.starttls()
            server.login(mediatorEmail, '123456789Corona')
            server.sendmail(senderEmail, receiverEmail, msg.as_string())
            flash("Successfully sent email")
    return render_template('/contact.html')

if __name__ == "__main__":
    app.run(debug=True)
    
