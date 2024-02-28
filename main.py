import sys
import Functions
import drawings

f = Functions
d = drawings

f.create_database()

while True:

    d.main_menu()

    option = int(input("Digite a opção desejada: "))
    if option == 1:
        f.add_movie()
    elif option == 2:
        f.edit_movie()
    elif option == 3:
        f.remove_movie()
    elif option == 4:
        while True:

            d.consult_movies_menu()

            option = int(input("Digite a opção desejada: "))
            if option == 1:
                f.list_movies_by_style()
            elif option == 2:
                f.list_movies_by_director()
            elif option == 3:
                f.list_movies_by_year()
            elif option == 4:
                f.filter_movies_by_year()
            if option == 5:
                f.filter_movies_by_style()
            elif option == 6:
                f.list_movies_by_year_interval()
            elif option == 7:
                f.list_movies_by_director_and_year_range()
            elif option == 8:
                f.oscar_winner_movies()
            if option == 9:
                f.list_movies_with_age()
            elif option == 10:
                f.display_oscars_by_movie()
            elif option == 11:
                f.display_oscars_by_movie_id()
            elif option == 12:
                f.display_oscars_by_genre()
            elif option == 0:
                break
            else:
                print("\nSelecione uma opção válida...")
    elif option == 0:
        sys.exit("A sair do programa...")
        break
    else:
        print("\nSelecione uma opção válida...")



