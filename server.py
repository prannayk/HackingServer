from flask import Flask, request, json, render_template, session, redirect
from subprocess import call
import sys 
import os
from OpenSSL import SSL




app = Flask("HackingServer")
app.secret_key = "hackingserversrocks"

# Configurations
app.config['UPLOAD_FOLDER'] = "uploads/"
app.config['FNAME'] = ""

@app.route("/",methods=["GET"])
def render_home():
	return render_template('index.html')

@app.route("/upload",methods=["POST"])
def upload_it():
	_file = request.files["file"]
	_filename = _file.filename
	call(["mkdir",app.config['UPLOAD_FOLDER']+_filename])
	_file.save(os.path.join(app.config['UPLOAD_FOLDER']+_filename,'random.txt'))
	app.config['FNAME'] = _file.filename
	call(["cp","ccode",app.config['UPLOAD_FOLDER']+_filename+'/ccode'])
	return redirect('/fileHome')

@app.route('/fileHome',methods=['GET'])
def fileHome():
	return render_template('file.html',data=app.config['FNAME'])

app.debug = True
app.run()
