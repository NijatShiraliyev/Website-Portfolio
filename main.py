from datetime import datetime

from flask import render_template, Flask, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, EmailField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv
import smtplib
app = Flask(__name__)
load_dotenv()

password = os.getenv("PASSWORD")
user = "nijat.shiraliyev@yahoo.com"

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Please enter your name")])
    email = EmailField("Email", validators=[DataRequired("Please enter your email")])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")

@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        to = "nicatshiraliev@gmail.com"
        message = form.message.data
        today = datetime.today()
        formatted_date = today.strftime('%#d/%#m/%Y')  #
        msg = (f"From: {user}\n"
               f"To: {to}\n"
               f"Subject: Portfolio\n"
               f"Date: {formatted_date}\n\n"
               f"From {email}\n{message}")

        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
            server.starttls()
            server.login(user, password)
            server.sendmail(user, to, msg)
        return redirect(url_for("home"))

    return render_template("index.html", form=form)


if __name__ == '__main__':
   app.run(debug=False)
