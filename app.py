# Blockbuster catalog

# count title year genre director duration rating

import movie_catalog


def add_movie():
    print("Add a new movie to the catalog")

    title_movie = input("Insert the title: ")
    year_movie = input("Inser the year: ")
    genre = input("Inser the genre: ")
    director = input("Inser the director: ")
    duration = input("Inser the duration (minutes): ")
    rating = input("Inser the rating (1.0-10.0): ")

    length_catalog = len(movie_catalog.movies.items())
    movie_catalog.movies[length_catalog + 1] = {
        "title": title_movie,
        "year": year_movie,
        "genre": genre,
        "director": director,
        "duration": duration,
        "rating": rating
    }

    for film in movie_catalog.movies.items():
        print(film)

    # print(f"Length catalog: {length_catalog}")


def show_catalog(movie_catalog):
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Movie catalog")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    for movie in movie_catalog.movies:
        print(movie)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    while True:
        exit_from_catalot = input("Type 'q' to quit: ")

        if exit_from_catalot.lower() == 'q':
            break
        else:
            print("Invalid value")


def search_movie():
    pass


def remove_movie():
    pass


def show_analytics():
    pass


def main():

    main_menu = {1: 'Add a movie to the catalog',
                 2: 'Show catalog',
                 3: 'Seach',
                 4: 'Remove a movie from the catalog',
                 5: 'Analytics',
                 6: 'Exit'}

    sub_menu = {}

    is_running = True

    while is_running:

        for key, value in main_menu.items():
            print(f"{key} - {value}")

        choice = input("What do you want to do? Choose (1-6): ")

        if choice.isdigit():
            choice = int(choice)

            if choice in main_menu.keys():
                if choice == 1:
                    add_movie()
                elif choice == 2:
                    show_catalog(movie_catalog)
                elif choice == 3:
                    search_movie()
                elif choice == 4:
                    remove_movie()
                elif choice == 5:
                    show_analytics()
                elif choice == 6:
                    print("Have a nice day!")
                    is_running = False
                else:
                    print("Invalid value")
            else:
                print("Invalid value")
        else:
            print("Invalid value")


if __name__ == '__main__':
    main()
