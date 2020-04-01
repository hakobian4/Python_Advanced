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

    if mongo.db.user.find_one({'email' : response['email']}):
        message = "Ther exists user with {} e-mail".format(response['email'])
    else:
        user_obj = User(response['user_name'], response['email'])
        mongo.db.user.insert({'user_name' : user_obj.user_name, 'email' : user_obj.email, 'playlist' : user_obj.songs})
        message = "added {} user".format(user_obj.user_name)
    
    return message

@app.route('/api/v1/playlist/add/song', methods = ['POST'])
def add_song():
    
    response = request.get_json()
    if len(response['user_name']) == 0 or len(response['name']) == 0 or len(response['singer']) == 0 or len(response['url']) == 0:
        message = "Your parameters are incompleted. Please enter all true parameters."
    else:
        if mongo.db.user.find_one({'user_name' : response['user_name']}):
            song_obj = Song(response['name'], response['singer'], response['url'])
            mongo.db.user.update(
                {'user_name' : response['user_name']},
                {
                    '$addToSet': { 'playlist': {'singer' : song_obj.singer, 'name' : song_obj.name, 'url' : song_obj.url}}
                }
                )
            message = "Song added in playlist of {} user".format(response['user_name'])
        else: 
            message = "No user with {} name".format(response['user_name'])

    return message


@app.route('/api/v1/playlist/remove/song', methods = ['DELETE'])
def remove_song():

    response = request.get_json()
    if len(response['user_name']) == 0 or len(response['url']) == 0:
        message = "Your parameters are incompleted. Please enter all true parameters."
    else:
        if mongo.db.user.find_one({'user_name' : response['user_name']}):
            mongo.db.user.update(
                {'user_name' : response['user_name']},
                {
                    '$pull': { 'playlist': {'url' : response['url']}}
                }
                )
            message = "This song removed in playlist of {} user".format(response['user_name'])
        else:
            message = "No user with {} name".format(response['user_name'])

    return message


@app.route('/api/v1/playlist/remove/user/<name>', methods = ['DELETE'])
def remove_user(name):

    if mongo.db.user.find_one({'user_name' : name}):
        mongo.db.user.delete_one({'user_name' : name})
        message = "deleted user {}".format(name)
    else:
        message = " no this user"
    
    return message

if __name__ == '__main__':
    app.run()