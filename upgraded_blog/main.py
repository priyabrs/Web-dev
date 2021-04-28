
from flask import Flask, render_template
import requests
from data import API_DATA

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