from flask import Flask, render_template
app = Flask(__name__)


header_dict = {
    'header1':'header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 header1 ',
    'header2' : 'header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 header2 ',
    'header3' : 'header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 header3 '
}

@app.route('/')
def home(index):
    return render_template('index.html', hdict = header_dict, index = index)

# @app.route('/')
# def header():
#     return render_template(f'{name}.html')

if __name__ == '__main__':
    app.run(debug=True)