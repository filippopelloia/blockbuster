# Blockbuster catalog

# count title year genre director duration rating

import movie_catalog
import movie_class


def ask_rating():
    while True:
        try:
            rating = float(input("Insert the rating (1.0-10.0): "))
            if 1.0 <= rating <= 10.0:
                return rating
            else:
                print("Rating must be between 1.0 and 10.0.")
        except ValueError:
            print("Please insert a valid integer.")


def add_movie():
    print("Add a new movie to the catalog")

    title_movie = input("Insert the title: ").capitalize()
    year_movie = input("Inser the year: ")
    genre = input("Inser the genre: ").capitalize()
    director = input("Inser the director: ").capitalize()
    duration = input("Inser the duration (minutes): ")
    rating = ask_rating()

    new_index = len(movie_catalog.movies) + 1
    new_movie = movie_class.Movie(
        index=new_index,
        title_movie=title_movie,
        year_movie=year_movie,
        genre=genre,
        director=director,
        duration=duration,
        rating=rating
    )

    movie_catalog.movies.append(new_movie)

    for film in movie_catalog.movies:
        print(film)


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

    while True:
        search = input("Search for a movie by title: ").lower()

        print(f"Result value: {search}")
        print(movie_catalog.movies)

        if search:
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Result:")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
            for movie in movie_catalog.movies:
                if search in movie.title_movie.lower():
                    print(movie)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        else:

            while True:
                for movie in movie_catalog.movies:
                    print(movie)

                action = input("'q' to quit: ")

                if action == 'q':
                    print("Have a nice day")
                    break
                else:
                    continue

        break


def remove_movie():

    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Remove a movie from the catalog")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    for movie in movie_catalog.movies:
        print(movie)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")

    while True:
        exit_from_catalot = input(
            "Insert the index number to remove a movie. Type 'q' to quit: ")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")

        if exit_from_catalot.lower() == 'q':
            break
        elif exit_from_catalot.isdigit():
            num_chosen = int(exit_from_catalot) - 1
            if 0 > num_chosen or num_chosen > len(movie_catalog.movies):
                print("Invalid number")
            else:

                while True:
                    second_question = input(
                        f"Do you want to remove '{movie_catalog.movies[num_chosen].title_movie}' from catalog? (Y/N): ").lower()

                    if second_question == 'y':
                        del movie_catalog.movies[num_chosen]
                        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Successfully deleted!")
                        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("Catalog updated:")
                        for movie in movie_catalog.movies:
                            print(movie)
                        break
                    else:
                        print("Nothing happened")
                        break
        else:
            print("Invalid value")


def show_analytics(analytics_menu):
    # media voti, classifica voti, voto più basso, voto più alto,
    # media durata, classifica durata, più breve, più lungo
    # più vecchio. più recente, film per anno
    # raccolta film per regista
    # film per genere
    # ordine alfabetico titoli film

    for key, value in analytics_menu.items():
        print(f"{key} - {value}")

    while True:
        analytics_action = input(
            "What do you want to do? Choose a number (1-7): ")

        if analytics_action.isdigit():
            analytics_action = int(analytics_action)

            if 1 >= analytics_action and analytics_action >= 7:
                print("Invalid value, choose a number (1-7): ")
            else:
                if analytics_action == 1:
                    pass
                elif analytics_action == 2:
                    pass
                elif analytics_action == 3:
                    pass
                elif analytics_action == 4:
                    pass
                elif analytics_action == 5:
                    pass
                elif analytics_action == 6:
                    pass
                elif analytics_action == 7:
                    print("Have a nice day!")
                    break
                else:
                    print("Something went wrong")
        else:
            print("Invalid value, choose a number (1-7): ")


def main():

    main_menu = {1: 'Add a movie to the catalog',
                 2: 'Show catalog',
                 3: 'Seach by title',
                 4: 'Remove a movie from the catalog',
                 5: 'Analytics',
                 6: 'Exit'}

    analytics_menu = {1: 'Ratings',
                      2: 'Duration',
                      3: 'Years',
                      4: 'Directors',
                      5: 'Genres',
                      6: 'Titles',
                      7: 'Exit'}

    rating_menu = {1: 'Average rating',
                   2: 'Highest rated movie',
                   3: 'Lowest rated movie',
                   4: 'Rating ranking',
                   5: 'Exit'}

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
                    # show_analytics(analytics_menu)
                    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Work in progress, stay tuned!")
                    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                    pass
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
