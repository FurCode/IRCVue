__author__ = 'foxlet'
from flask import render_template
from ircvue import app
from ircvue import brandingdata
import xmlrpc.client
import configparser

@app.route("/createaccount", methods=['POST'])
def register_xmlrpc():
    serverconf = configparser.ConfigParser()
    try:
        serverconf.read_file(open('config/nickservbot.ini'))
    except FileNotFoundError:
        serverconf.read_file(open('ircvue/config/nickservbot.ini'))
    remote = str(branding['XMLRPC']['TargetAddress'])
    server = xmlrpc.client.ServerProxy(remote)
    try:
        server.DoCommand("NickServ", "user", "REGISTER password email");
    except Error as v:
        print("ERROR", v)

    return render_template('register.html', name=brandingdata.name, gettingstarted=brandingdata.gettingstarted, NetworkSite=brandingdata.NetworkSite, NetworkWebchat=brandingdata.NetworkWebchat)