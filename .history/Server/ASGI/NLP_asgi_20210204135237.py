import flask,json
from flask import request

'''

flask: seb using the decorator @server.route()
to transfer normal func into server login

'''

server = flask.Flask(__name__)

@server = flask.Flask(__name__)

def login():
    InputLanguage = request.values.get('Input')
    res = tn.parse(input=InputLanguage)
    return res

server.run(debug=True,port=8888,host='0.0.0.0')
