__author__ = 'foxlet'

from ircvue import main as app
from ircvue.util import messages
import os



if os.path.isdir("ircvue/") == False:
    pass
else:
    try:
        os.chdir("ircvue/");
    except FileNotFoundError:
        print(messages.m_missingconfig)

app();

