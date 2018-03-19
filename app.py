from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from time import gmtime, strftime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     message = str(json);
#     print('received json: ' + str(json))

@socketio.on('message')
def handle_message(json, broadcast=True):
    send("(" +str(strftime("%H:%M:%S", gmtime()))+") " + json)

@app.route("/")
def main():
    return render_template('index.htm')


if __name__ == '__main__':
    socketio.run(app)
