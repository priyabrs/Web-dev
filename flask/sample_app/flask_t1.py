from email.mime import image
from flask import Flask
import random

# def get_random():
#     return random.randint(0,9)

RANDOM_NO = random.randint(0,9)
print(RANDOM_NO)

app = Flask(__name__)

def make_bold(func):
    def inner_func():
        str1 = func()
        return f'<b>{str1}</b>'
    return inner_func

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


@app.route('/<num>')
def guess(num):
    num = int(num)
    if num > RANDOM_NO:
        return '<img src="https://media3.giphy.com/media/hulrdGSUweWQDBBtfY/giphy.gif?cid=ecf05e47jx1k9t8i68dk0dsh916n8o37znt4ny6fexkau190&rid=giphy.gif&ct=g">'
    elif num < RANDOM_NO:
        return '<img src="https://media2.giphy.com/media/rS2uLYRGkGWySNX69v/giphy.gif?cid=ecf05e475e0tf5q0c9e09n7txnjrofl04h00mkle1cnl0f0a&rid=giphy.gif&ct=g">'
    else:
        return '<img src="https://media4.giphy.com/media/3oFzmkkwfOGlzZ0gxi/giphy.gif?cid=ecf05e47y3ic2urxporzt89z80f79s8zjeg1zvvoaajlo0mq&rid=giphy.gif&ct=g">'
    # return f'<h1>Hello there {name}</h1>'

# @app.route('/<path:name>')
@app.route('/<name>/<int:number>')
def greet_path(name, number):
    return f'<h1>Hello {name} and num: {number}</h1>'

if __name__ == '__main__':
    app.run(debug=True)


# class User():
#     def __init__(self, name) -> None:
#         self.name = name
#         self.is_logged_in = False

# def authenticate(func):
#     def inner_func(*args, **kwargs):
#         if args[0].is_logged_in:
#             func(args[0])
#         else:
#             print('User needs to be logged in!!')
#     return inner_func

# @authenticate
# def create_blog(user):
#     print(f"{user.name}'s Blog post")

# nu_user = User('Priyabrata')
# nu_user.is_logged_in=True
# create_blog(nu_user)