from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='eventlet')

@app.get('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, port=5555)