from flask import request, jsonify, Flask
from flask_pymongo import PyMongo
from user import User
from song import Song

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["MONGO_URI"] = "mongodb://localhost:27017/playlists"
app.config['MONGO_DBNAME'] = 'playlists'
mongo = PyMongo(app)

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

    user_obj = User(response['user_name'], response['email'])
    mongo.db.user.insert({'user_name' : user_obj.user_name, 'email' : user_obj.email, 'playlist' : user_obj.songs})

    return "added {} user".format(user_obj.user_name)
 

@app.route('/api/v1/playlist/add/song', methods = ['POST'])
def add_song():
    
    response = request.get_json()
    mongo.db.user.update(
        {'user_name' : response['user_name']},
        {
            '$addToSet': { 'playlist': {'singer' : response['singer'], 'name' : response['name'], 'url' : response['url']}}
        }
        )

    return "Song added in playlist of {}".format(response['user_name'])


@app.route('/api/v1/playlist/remove/song/<name>', methods = ['DELETE'])
def remove_song(name):
    mongo.db.user.delete_one({'singer' : name})
    return "deleted"

if __name__ == '__main__':
    app.run()