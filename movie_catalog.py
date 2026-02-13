# Movie catalog

from movie_class import Movie

movie1 = Movie(
    index=1,
    title_movie="The Shawshank Redemption",
    year_movie=1994,
    genre="Drama",
    director="Frank Darabont",
    duration=142,
    rating=9.3
)

movie2 = Movie(
    index=2,
    title_movie="The Godfather",
    year_movie=1972,
    genre="Crime",
    director="Francis Ford Coppola",
    duration=175,
    rating=9.2
)

movie3 = Movie(
    index=3,
    title_movie="The Dark Knight",
    year_movie=2008,
    genre="Action",
    director="Christopher Nolan",
    duration=152,
    rating=9.0
)

movie4 = Movie(
    index=4,
    title_movie="Pulp Fiction",
    year_movie=1994,
    genre="Crime",
    director="Quentin Tarantino",
    duration=154,
    rating=8.9
)

movies = [movie1, movie2, movie3, movie4]

for movie in movies:
    print(movie)
