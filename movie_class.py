# Movie class

class Movie:
    def __init__(self, index, title_movie, year_movie, genre, director, duration, rating):
        self.index = index
        self.title_movie = title_movie
        self.year_movie = year_movie
        self.genre = genre
        self.director = director
        self.duration = duration
        self.rating = rating

    def __str__(self):
        return f"Id: {self.index}, Title: {self.title_movie}, Year: {self.year_movie}, Genre: {self.genre}, Director: {self.director}, Duration: {self.duration}, Rating: {self.rating}"
