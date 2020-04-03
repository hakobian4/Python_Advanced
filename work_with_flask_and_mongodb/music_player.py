class Player():
    def __init__(self, mongo):
        self.mongo = mongo


    def get_player(self):
        
        try:
            playlist = self.mongo.db.user.find()
            result = []

            for info in playlist:
                result.append({'user_name' : info['user_name'], 'email' : info['email'], 'playlist' : info['playlist']})
        except Exception as exception:
            result = exception

        return result

    def add_user(self, user):
        
        try:
            if self.mongo.db.user.find_one({'email' : user.email}):
                message = "There already exists user with {} e-mail".format(user.email)
            else:
                self.mongo.db.user.insert({'user_name' : user.user_name, 'email' : user.email, 'playlist' : user.songs})
                message = "Added {} user".format(user.user_name)
        except Exception as exception:
            message = exception

        return message
    

    def add_song(self, email, song):

        try:
            if self.mongo.db.user.find_one({'email' : email}):
                self.mongo.db.user.update(
                    {'email' : email},
                    {
                        '$addToSet': { 'playlist': {'singer' : song.singer, 'name' : song.name, 'url' : song.url}}
                    } 
                    )
                message = "Song added in playlist of {} user".format(email)
            else: 
                message = "No user with email {}".format(email)
        except Exception as exception:
            message = exception

        return message 


    def remove_song(self, email, url):

        try:
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
        except Exception as exception:
            message = exception

        return message


    def remove_user(self, email):

        try:
            if self.mongo.db.user.find_one({'email' : email}):
                self.mongo.db.user.delete_one({'email' : email})
                message = "Deleted user {}".format(email)
            else:
                message = "Given user doesn't exist."
        except Exception as exception:
            message = exception
            
        return message