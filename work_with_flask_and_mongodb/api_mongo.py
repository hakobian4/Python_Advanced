from flask import request, jsonify, Flask
from flask_pymongo import PyMongo
from music_player import Player
from user import User
from song import Song

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["MONGO_URI"] = "mongodb://localhost:27017/playlists"
app.config['MONGO_DBNAME'] = 'playlists'
mongo = PyMongo(app)
player = Player(mongo)

@app.route('/api/v1/playlist', methods = ['GET'])
def get_all():

    result = player.get_player()

    return jsonify({'result' : result})


@app.route('/api/v1/playlist/add/user', methods = ['POST'])
def add_user():

    response = request.get_json()
    user_name = response['user_name']
    email = response['email']
    user_obj = User(user_name, email)
    message = player.add_user(user_obj)

    return message

@app.route('/api/v1/playlist/add/song', methods = ['POST'])
def add_song():
    
    response = request.get_json()
    if len(response['email']) == 0 or len(response['name']) == 0 or len(response['singer']) == 0 or len(response['url']) == 0:
        message = "Your parameters are incompleted. Please enter all valid parameters."
    else:
        email = response['email']
        singer = response['singer']
        url =response['url']
        song_name = response['name']
        song_object = Song(song_name, singer, url)
        message = player.add_song(email, song_object)

    return message


@app.route('/api/v1/playlist/remove/song', methods = ['PUT', 'DELETE'])
def remove_song():

    response = request.get_json()
    if len(response['email']) == 0 or len(response['url']) == 0:
        message = "Your parameters are incompleted. Please enter all valid parameters."
    else:
        email = response['email']
        url =response['url']
        message = player.remove_song(email, url)

    return message


@app.route('/api/v1/playlist/remove/user/<email>', methods = ['DELETE'])
def remove_user(email):
    
    message = player.remove_user(email)
    
    return message

if __name__ == '__main__':
    app.run()