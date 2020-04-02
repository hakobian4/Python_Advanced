from song import Song

class User():
    def __init__(self, name, email):
        self.user_name = name
        self.email = email
        self.songs = []