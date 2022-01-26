from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO

from hyperdeck import Hyperdeck
from recording import format_number
from bundle import bundle

NUMBER = 0

a = Hyperdeck('192.168.1.205', 'A')
b = Hyperdeck('192.168.1.206', 'B')
c = Hyperdeck('192.168.1.207', 'C')
d = Hyperdeck('192.168.1.208', 'D')

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/id')
def get_id():
    global NUMBER
    return str(NUMBER)

@socketio.on('standard-command')
def standard_command(payload):
    global NUMBER
    if payload['command'] == 'record':
        NUMBER += 1
    if payload['decks']['a']:
        a.send_standard_command(payload['command'], format_number(NUMBER))
    if payload['decks']['b']:
        b.send_standard_command(payload['command'], format_number(NUMBER))
    if payload['decks']['c']:
        c.send_standard_command(payload['command'], format_number(NUMBER))
    if payload['decks']['d']:
        d.send_standard_command(payload['command'], format_number(NUMBER))

@socketio.on('granular-command')
def standard_command(payload):
    if payload['decks']['a']:
        a.send_granular_command(payload['command'], payload['direction'])
    if payload['decks']['b']:
        b.send_granular_command(payload['command'], payload['direction'])
    if payload['decks']['c']:
        c.send_granular_command(payload['command'], payload['direction'])
    if payload['decks']['d']:
        d.send_granular_command(payload['command'], payload['direction'])

if __name__ == '__main__':
    bundle(app)
    socketio.run(app,host='0.0.0.0', port=5555)