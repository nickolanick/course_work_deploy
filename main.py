from flask import Flask, render_template, request
from examples import data
from examples.you_tube import *

app = Flask(__name__)


@app.route('/')
def data_reg():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def data_handle():
    if request.form['text_field']:
        print(youtube_search(request.form['text_field']))
        return render_template("data_handled.html", data=data.get_html_content(request.form['text_field']),
                               videos=youtube_search(request.form['text_field']))


if __name__ == '__main__':
    app.run()
