# -*- coding: utf-8 -*-
import socket
import sys
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = '58619d5c336542d29a798d08e98d01ca'
app.config['SESSION_TYPE'] = 'filesystem'
table_attrs = {"class": "table table-bordered table-hover small"}


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


if __name__ == "__main__":
    args = sys.argv
    localhost = socket.gethostbyname(socket.gethostname())
    debug = False
    if len(args) > 1 and args[1] == 'local':
        localhost = '127.0.0.1'
        debug = True
    app.run(host=localhost, port=8080, debug=debug)
