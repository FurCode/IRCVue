__author__ = 'foxlet'

import configparser

branding = configparser.ConfigParser()
try:
    branding.read_file(open('config/branding.ini'))
except FileNotFoundError:
    branding.read_file(open('ircvue/config/branding.ini'))
name = str(branding['NETWORK']['NetworkName'])
NetworkWebchat = str(branding['NETWORK']['NetworkWebchat'])
NetworkSite = str(branding['NETWORK']['NetworkSite'])
gettingstarted = branding['FEATURES'].getboolean('EnableGettingStarted')