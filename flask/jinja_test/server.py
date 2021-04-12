from flask import Flask, render_template
import api_call
import random
import datetime
app = Flask(__name__)

year = datetime.date.today().year

@app.route('/')
def home():
    random_number = random.randint(1,100)
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def page(name):
    guessed_age = api_call.guess_age(name)
    guessed_gender = api_call.guess_gender(name)
    return render_template('guess.html', name=name, age=guessed_age, gender=guessed_gender)

@app.route('/blog')
def get_blog():
    all_posts = api_call.blog()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)