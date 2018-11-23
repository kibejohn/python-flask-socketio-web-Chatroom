from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit



app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY')
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( "chatroom.html" )

@socketio.on( "my event" )
def handle_my_custom_event( json ):
  socketio.emit( "my response", json)

if __name__ == '__main__':
  socketio.run( app, debug = True, port = 8080)