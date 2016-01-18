#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#http://pythonclub.com.br/what-the-flask-pt-1-introducao-ao-desenvolvimento-web-com-python.html

from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello_world():
	return "Olá mundo!! <strong> E viva o galo <strong>", 200




from flask import jsonify

def json_api():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    return jsonify(pessoas=pessoas, total=len(pessoas))


app.run()
