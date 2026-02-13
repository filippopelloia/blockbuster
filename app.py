# Blockbuster catalog

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
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    pass
                elif choice == 5:
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
