from flask import request, jsonify, Flask
from flask_pymongo import PyMongo
from music_player import Player

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["MONGO_URI"] = "mongodb://localhost:27017/playlists"
app.config['MONGO_DBNAME'] = 'playlists'
mongo = PyMongo(app)
player = Player(mongo)

@app.route('/api/v1/playlist', methods = ['GET'])
def get_all():

    playlist = mongo.db.user.find()
    result = []

    for info in playlist:
        result.append({'user_name' : info['user_name'], 'email' : info['email'], 'playlist' : info['playlist']})

    return jsonify({'result' : result})


@app.route('/api/v1/playlist/add/user', methods = ['POST'])
def add_user():

    response = request.get_json()
    message = player.add_user(response['user_name'], response['email'])

    return message

@app.route('/api/v1/playlist/add/song', methods = ['POST'])
def add_song():
    
    response = request.get_json()
    if len(response['email']) == 0 or len(response['name']) == 0 or len(response['singer']) == 0 or len(response['url']) == 0:
        message = "Your parameters are incompleted. Please enter all valid parameters."
    else:
        message = player.add_song(response['email'], response['singer'], response['name'], response['url'])

    return message


@app.route('/api/v1/playlist/remove/song', methods = ['DELETE'])
def remove_song():

    response = request.get_json()
    if len(response['email']) == 0 or len(response['url']) == 0:
        message = "Your parameters are incompleted. Please enter all valid parameters."
    else:
        message = player.remove_song(response['email'], response['url'])

    return message


@app.route('/api/v1/playlist/remove/user/<name>', methods = ['DELETE'])
def remove_user(name):
    
    message = player.remove_user(name)
    
    return message

if __name__ == '__main__':
    app.run()