__author__ = 'foxlet'
from flask import render_template
from ircvue import app
from ircvue import brandingdata
import xmlrpc.client
import configparser

@app.route("/register")
def register_form():
    return render_template('form.html', name=brandingdata.name, gettingstarted=brandingdata.gettingstarted, NetworkSite=brandingdata.NetworkSite, NetworkWebchat=brandingdata.NetworkWebchat)