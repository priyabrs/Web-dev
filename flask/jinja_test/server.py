from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

year = datetime.date.today().year

@app.route('/')
def home():
    random_number = random.randint(1,100)
    return render_template('index.html', num=random_number, year=year)

# @app.route('/template/<name>.html')
# def page(name):
#     return render_template(f'{name}.html')

if __name__ == '__main__':
    app.run(debug=True)