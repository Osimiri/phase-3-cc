class Viewer:
    
    usernames = []

    def __init__(self, username):
        self.username = username
        self.reviews = []
        self.reviewed_movies = [] 
        

    # username property goes here!
    @property
    def username(self):
        return self._username 
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 6 <= len(username) <= 16 and username not in Viewer.usernames:
            self._username = username
            Viewer.usernames.append(self)
        else:
            raise Exception("Username must be unique strings between 6 and 16 characters")


    def reviewed_movie(self, movie):
        if movie in self.reviewed_movies: 
            return True 
        else:
            return False
    
    def rate_movie(self, movie, rating):
        from lib.review import Review 
        Review(self, movie, rating)

    def reviews(self):
        return self.reviews 
        