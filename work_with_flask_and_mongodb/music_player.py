from user import User
from song import Song

class Player():
    def __init__(self, mongo):
        self.mongo = mongo

    def add_user(self, user_name, email):

        if self.mongo.db.user.find_one({'email' : email}):
            message = "There already exists user with {} e-mail".format(email)
        else:
            user_obj = User(user_name, email)
            self.mongo.db.user.insert({'user_name' : user_obj.user_name, 'email' : user_obj.email, 'playlist' : user_obj.songs})
            message = "Added {} user".format(user_obj.user_name)
        
        return message
    

    def add_song(self, email, singer, song_name, url):

        if self.mongo.db.user.find_one({'email' : email}):
            song_obj = Song(song_name, singer, url)
            self.mongo.db.user.update(
                {'email' : email},
                {
                    '$addToSet': { 'playlist': {'singer' : song_obj.singer, 'name' : song_obj.name, 'url' : song_obj.url}}
                }
                )
            message = "Song added in playlist of {} user".format(email)
        else: 
            message = "No user with email {}".format(email)
        
        return message 


    def remove_song(self, email, url):
        if self.mongo.db.user.find_one({'playlist' : {'$elemMatch' : {'url' : url}}}) and self.mongo.db.user.find_one({'email' : email}):
            self.mongo.db.user.update(
                {'email' : email},
                {
                    '$pull': { 'playlist': {'url' : url}}
                }
                )
            message = "This song removed from playlist of {} user".format(email)
        else:
            message = "User {} doesn't exist or current user doesn't have such a song in his/her playlist".format(email)
        
        return message


    def remove_user(self, user_name):

        if self.mongo.db.user.find_one({'user_name' : user_name}):
            self.mongo.db.user.delete_one({'user_name' : user_name})
            message = "Deleted user {}".format(user_name)
        else:
            message = "Given user doesn't exist."

        return message