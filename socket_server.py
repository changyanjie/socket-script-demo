# coding: utf-8
import __future__
import socket
import sys
import six
import time
from flask import Flask
from flask_socketio import SocketIO, send, emit
from prettytable import PrettyTable
from script import agent_retailer
from utils import html_p
app = Flask(__name__)
app.config['SECRET_KEY'] = '452377b6a9d011e883eb88e9fe4f3130'
socketio = SocketIO(app, async_mode='threading')


def send_msg(event=None, title=None, table_obj=None):
    """"""
    table_attrs = {"class": "table table-bordered table-hover small text-center"}
    title = html_p(title) if title else ''
    content = ''
    if isinstance(table_obj, six.text_type):
        content = html_p(table_obj)
    elif isinstance(table_obj, PrettyTable):
        content = table_obj.get_html_string(attributes=table_attrs) \
            if table_obj and len(table_obj._rows) > 0 else u'无记录'
    if event is None:
        send(title + content)
    else:
        emit(event, title + content)


@socketio.on('agent_retailer')
def handle_agent_retailer(json):
    """"""
    event = 'agent_retailer'
    retailer_id = json['retailer_id']
    send_msg(event, u'查询商户信息:', agent_retailer.search_retailer_info(retailer_id))
    # 测试分段输出，sleep 3s
    time.sleep(3)
    send_msg(event, u'当前主承运商:', agent_retailer.search_current_agents(retailer_id))


if __name__ == "__main__":
    args = sys.argv
    localhost = socket.gethostbyname(socket.gethostname())
    debug = False
    if len(args) > 1 and args[1] == 'local':
        localhost = '127.0.0.1'
        debug = True
    socketio.run(app, host=localhost, port=8090, debug=debug)
