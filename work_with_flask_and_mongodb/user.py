from song import Song

class User():
    def __init__(self, name, email):
        self.user_name = name
        self.email = email
        self.songs = []
    
    def add_song(self, song_obj):
        self.songs.append(song_obj)
