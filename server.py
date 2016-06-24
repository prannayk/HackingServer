from flask import Flask, request, json, render_template, session, redirect
from subprocess import call
import sys 
import os

app = Flask("HackingServer")
