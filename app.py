from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from time import gmtime, strftime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

clients = []

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('message')
def handle_message(json):
    send("(" +str(strftime("%H:%M:%S", gmtime()))+") " + json, broadcast=True)

@app.route("/")
def main():
    return render_template('index.htm')


if __name__ == '__main__':
    socketio.run(app)
