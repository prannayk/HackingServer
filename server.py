from flask import Flask, request, json, send_from_directory, render_template, session, redirect
from subprocess import call, Popen
import shlex
import sys 
import os
from OpenSSL import SSL
import random
import math


app = Flask("HackingServer")
app.secret_key = "hackingserversrocks"

# Configurations
app.config['UPLOAD_FOLDER'] = "uploads/"
app.config['FNAME'] = ""

@app.route("/",methods=["GET"])
def render_home():
	return render_template('index.html',number = int(math.ceil((random.random()*1000000))))

@app.route("/upload",methods=["POST"])
def upload_it():
	_file = request.files["file"]
	_filename = request.form['filename']
        os.system("mkdir " + app.config['UPLOAD_FOLDER'] + _filename)
        #p = Popen(shlex.split("mkdir" + app.config['UPLOAD_FOLDER'] + _filename), shell=True)
	#call("mkdir " + app.config['UPLOAD_FOLDER']+_filename, shell=True)
	call(["mkdir",app.config['UPLOAD_FOLDER']+_filename])

	_file.save(app.config['UPLOAD_FOLDER']+_filename+'/random.txt')
	app.config['FNAME'] = _filename
	call([os.environ['binaryCall'],"uploads/"+_filename+"/random.txt"])
        #os.system(os.environ['binaryCall'] + " uploads/" + _filename + "/random.txt")
	call(["cp","hash.txt",app.config['UPLOAD_FOLDER']+_filename+'/hash.txt'])
        #os.system("cp hash.txt " + app.config['UPLOAD_FOLDER'] + _filename + "/hash.txt")
	return redirect('/fileHome?name='+_filename)

@app.route('/fileHome',methods=['GET'])
def fileHome():
	return send_from_directory(app.config['UPLOAD_FOLDER'],app.config['FNAME']+'/hash.txt')

app.debug = True
app.run()
