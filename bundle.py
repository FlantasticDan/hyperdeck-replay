  
import os
import sys

import webbrowser

def bundle(app):
    try:
        app.template_folder = os.path.join(sys._MEIPASS, 'templates')
        app.static_folder = os.path.join(sys._MEIPASS, 'static')
        webbrowser.open_new('http://localhost:5555')
    except Exception:
        pass