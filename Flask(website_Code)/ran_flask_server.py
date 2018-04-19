from flask import Flask, render_template, request
from api_parse import data
from api_parse.you_tube import *
from api_parse.hotline_parse import *

app = Flask(__name__)


@app.route('/')
def data_reg():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def data_handle():
    if request.form['text_field']:
        about_item = hot_line(request.form['text_field'])[0]
        comments_hot_line = hot_line(request.form['text_field'])[1]
        return render_template("data_handled.html", data=data.get_html_content(
            request.form['text_field']),
                               videos=youtube_search(
                                   request.form['text_field']),
                               about_item=about_item,
                               comments_hotline=
                               comments_hot_line)


if __name__ == '__main__':
    DEBUG = True
    app.run()
