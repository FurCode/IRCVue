__author__ = 'foxlet'

from flask import Flask
from flask import render_template
from ircvue.util import messages, colorer
import sys
import configparser
import logging
import ircvue.brandingdata

app = Flask(__name__)

import ircvue.register_xmlrpc
import ircvue.register_form
@app.route("/")
def welcome():
    return render_template('index.html', name=brandingdata.name, gettingstarted=brandingdata.gettingstarted, NetworkSite=brandingdata.NetworkSite, NetworkWebchat=brandingdata.NetworkWebchat)

def main():
    messages.initmessage();
    debug = configparser.ConfigParser()
    debug.read('config/debug.ini')
    try:
        EnableDebug = debug['DEBUG'].getboolean('EnableDebug')
    except KeyError:
        logging.error(messages.m_missingconfig);
        sys.exit(1);
    MakePublic = debug['DEBUG'].getboolean('MakePublic')
    BindAddress = debug['DEBUG']['BindAddress']
    BindPort = int(debug['DEBUG']['BindPort'])

    if EnableDebug == True:
        app.debug = True
    else:
        pass
    if MakePublic == True:
        app.run(host=BindAddress, port=BindPort)
    else:
        app.run()

if __name__ == "__main__":
    main();