
class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie 
        self.rating = rating
        
        self.add_review_to_movie()
        self.add_review_to_viewer()
        self.add_viewer_to_movie()
        self.add_movie_to_viewer()

    # rating property goes here!
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if isinstance(rating,int) and 1 <= rating <= 5:
            self._rating = rating
        else:
            print ("rating must be  integers between 1 and 5, inclusive")
            raise Exception("Invalid rating") 
    
    # viewer property goes here!
    @property 
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        from lib.viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer 
        else:
            print ("viewer must be an instance of Viewer")
            raise Exception ("viewer is NOT an instance of Viewer")
    
    # movie property goes here!
    @property 
    def movie (self):
        return self._movie

    @movie.setter
    def movie(self,movie):
        from lib.movie import Movie 
        if isinstance(movie, Movie):
            self._movie = movie 
        else:
            print ("the movie isn't an instance of movie now is it?")
            raise Exception("Thats the thing about it... this movie ain't an instance of movie")

    def add_review_to_movie(self):
        self._movie.reviews.append(self)
    
    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)
    
    def add_viewer_to_movie(self):
        if self._viewer not in self._movie.reviewers:
            self._movie.reviewers.append(self._viewer)
   
    def add_movie_to_viewer(self):
        if self._movie not in self._viewer.reviewed_movies:
            self._viewer.reviewed_movies.append(self._movie)
