import statistics
class Movie:
    all= []   
    
    def __init__(self, title):
        self.title = title #h
        self.reviews = []
        self.reviewers = []
        
        
    # title property goes here!
    @property 
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        # if type(title) is str and len(title) > 0:
        if isinstance (title, str) and 0 < len(title):
            self._title = title 
        else:
            print("You're gonna need more characters than that...")
            raise Exception("How did I forget this again????")


    def average_rating(self):
        total = 0

        for review in self.reviews:
            total += review
        
        return statistics.mean([review for review in self.reviews])
        

    @classmethod
    def highest_rated(cls):
        if not cls.all:
            return None

        highest_rated_movie = None
        highest_rating = 0

        for movie in cls.all:
            rating = movie.average_rating()
            if rating > highest_rating:
                highest_rating = rating
                highest_rated_movie = movie
        
        return highest_rated_movie

    @classmethod
    def set_all_movies(cls):
        return cls.all
