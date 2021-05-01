from webbrowser import get
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    username = request.form.get('username')
    password = request.form.get('pasword')
    return f'<h1>username: {username}, password: {password} </h1>'


if __name__ == '__main__':
    app.run(debug=True)