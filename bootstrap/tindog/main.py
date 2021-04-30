
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
# @app.route('/index.html')
def get_all_posts():
    return render_template("index.html")  

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    # , host='0.0.0.0'