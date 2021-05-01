
from flask import Flask, render_template, request
# import requests
from data import API_DATA
import smtplib,ssl

GMAIL_SMTP_SERVER = "smtp.gmail.com"
PORT = 465
context = ssl.create_default_context() # CREATES A SECURE SSL CONTEXT

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def get_all_posts():
    return render_template("index.html", api_data=API_DATA)

@app.route('/about.html')
def get_about():
    return render_template("about.html")

@app.route('/contact.html')
def get_contact():
    return render_template("contact.html")

@app.route('/contact', methods=['POST', 'GET'])
def post_contact():
# def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message from Form\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP_SSL(GMAIL_SMTP_SERVER, PORT, context=context) as server:
            server.login(EMAIL, PASSWORD)
            server.sendmail(from_addr=GMAIL_SMTP_SERVER, to_addrs=EMAIL, msg=message)
    
    # return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in API_DATA:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template("post.html", requested_post=requested_post)    

if __name__ == "__main__":
    app.run(debug=True)
    # , host='0.0.0.0'