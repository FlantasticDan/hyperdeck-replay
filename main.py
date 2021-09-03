from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO

from hyperdeck import Hyperdeck
from bundle import bundle

a = Hyperdeck('192.168.0.131', 'A')
b = Hyperdeck('192.168.0.132', 'B')
c = Hyperdeck('192.168.0.133', 'C')
d = Hyperdeck('192.168.0.134', 'D')

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

@app.get('/')
def index():
    return render_template('index.html')

@socketio.on('standard-command')
def standard_command(payload):
    if payload['decks']['a']:
        a.send_standard_command(payload['command'])
    if payload['decks']['b']:
        b.send_standard_command(payload['command'])
    if payload['decks']['c']:
        c.send_standard_command(payload['command'])
    if payload['decks']['d']:
        d.send_standard_command(payload['command'])

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