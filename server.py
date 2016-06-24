from flask import Flask, request, json, render_template, session, redirect
from subprocess import call
import sys 
import os

app = Flask("HackingServer")
app.secret_key = "hackingserversrocks"

@app.route("/",methods=["GET"])
def render_home():
	return render_template('index.html')
