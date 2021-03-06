from flask import Flask
from flask import render_template
from flask import request
from algorithm import *

app = Flask(__name__)

import logging
logging.basicConfig(filename='hasherapp.log',level=logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Welcome to hasherapp!'

@app.route('/compute', methods=['GET', 'POST'])
def compute():
	if request.method == 'GET':
		    return render_template('compute.html')
	else:
		hashlist = request.form.getlist('hashlist')
		app.logger.info('hashlist: %s -- %s' % (hashlist, type(hashlist)))

		texttohash = request.form['texttohash']
		app.logger.info('texttohash: %s -- %s' % (texttohash, type(texttohash)))

		passcount = request.form['passcount']
		try:
			passcount = int(passcount)
		except ValueError:
			passcount = 0
		app.logger.info('passcount: %d -- %s' % (passcount, type(passcount)))

		result = hash_text(hashlist, texttohash, passcount)
		
		return render_template('compute.html', result=result)

@app.route('/hashlist', methods=['GET'])
def hashlist():
	hashes = hash_list()
	return hashes
