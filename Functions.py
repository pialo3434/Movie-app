import conn
import random
from datetime import datetime
from prettytable import PrettyTable

mydb = conn.mydb

def insert_random_movies():
    movie_titles = {
        1: "The Shawshank Redemption",
        2: "The Godfather",
        3: "The Godfather: Part II",
        4: "The Dark Knight",
        5: "12 Angry Men",
        6: "Schindler's List",
        7: "The Lord of the Rings: The Return of the King",
        8: "Pulp Fiction",
        9: "The Lord of the Rings: The Fellowship of the Ring",
        10: "Forrest Gump",
        11: "Fight Club",
        12: "Inception",
        13: "Star Wars: Episode V - The Empire Strikes Back",
        14: "The Lord of the Rings: The Two Towers",
        15: "The Matrix",
        16: "Goodfellas",
        17: "One Flew Over the Cuckoo's Nest",
        18: "Seven Samurai",
        19: "Se7en",
        20: "It's a Wonderful Life",
        21: "The Silence of the Lambs",
        22: "City of God",
        23: "Life is Beautiful",
        24: "The Usual Suspects",
        25: "Saving Private Ryan",
        26: "Spirited Away",
        27: "The Green Mile",
        28: "Léon: The Professional",
        29: "Interstellar",
        30: "The Prestige"
    }

    movie_descriptions = {
        1: "A man is sentenced to life in prison for a crime he didn't commit and forms a bond with a fellow inmate in the process.",
        2: "A powerful mafia boss faces a series of challenges to protect his family's legacy and maintain control over his empire.",
        3: "The story of a young Vito Corleone and his rise to power in the world of organized crime.",
        4: "Batman fights against the Joker, a master criminal terrorizing Gotham City, in a battle of wits and strength.",
        5: "A jury deliberates the fate of a young man accused of murder and must confront their own biases and preconceptions.",
        6: "A German businessman saves the lives of more than a thousand Jewish refugees during the Holocaust.",
        7: "The final chapter in the epic journey of Frodo and his companions to destroy the One Ring and defeat Sauron.",
        8: "A series of interrelated stories involving the Los Angeles criminal underworld.",
        9: "A young hobbit sets out on a perilous journey to destroy the One Ring and save Middle-earth from darkness.",
        10: "The story of a simple man with a low IQ who experiences firsthand some of the major events of the 20th century.",
        11: "An insomniac office worker forms an underground fight club with a bully.",
        12: "A skilled thief is recruited to enter a dream world and plant an idea in someone's mind.",
        13: "Luke Skywalker trains with Jedi Master Yoda while his friends face off against Darth Vader and the Empire.",
        14: "The Fellowship of the Ring continues their journey to destroy the One Ring while facing new challenges and enemies.",
        15: "A hacker learns the truth about reality and joins a rebellion against intelligent machines.",
        16: "A young man rises through the ranks of the mob while trying to balance his criminal life and relationships.",
        17: "A criminal feigns insanity to serve his prison sentence in a mental institution but faces a power struggle with the head nurse.",
        18: "A samurai is hired to protect a village from bandits and trains the villagers to defend themselves.",
        19: "Two detectives hunt a serial killer who kills his victims based on the seven deadly sins.",
        20: "A man, down on his luck, is shown by a guardian angel what life would have been like if he had never been born.",
        21: "An FBI trainee seeks the help of a convicted serial killer to catch another serial killer who skins his victims.",
        22: "A young man grows up in a violent neighborhood of Rio de Janeiro and becomes a photographer.",
        23: "A Jewish father uses humor to protect his son from the reality of a concentration camp during World War II.",
        24: "A group of criminals meet in a police lineup and plan a heist together but not all is as it seems.",
        25: "A group of soldiers search for a paratrooper during World War II and face moral dilemmas along the way.",
        26: "A young girl enters a magical world to save her parents and must find a way to return home.",
        27: "A death row inmate with supernatural powers brings healing to those around him on his way to execution.",
        28: "A hitman takes in a young girl after her family is murdered and teaches her the tools of his trade.",
        29: "A group of astronauts travel through a wormhole in search of a new home for humanity.",
        30: "Two magicians engage in a rivalry to create the ultimate illusion while keeping secrets from each other."
    }

    mycursor = mydb.cursor()

    for key in sorted(movie_titles):
        title = movie_titles[key]
        description = movie_descriptions[key]
        year = random.randint(1900, 2022)
        sql = "INSERT INTO movies (movie_title, movie_description, movie_year) VALUES (%s, %s, %s)"
        val = (title, description, year)
        mycursor.execute(sql, val)
        mydb.commit()

    mycursor.close()
    print("30 filmes inseridos com sucesso!")

def insert_random_directors():
    director_names = {
        1: "Steven Spielberg",
        2: "Christopher Nolan",
        3: "Quentin Tarantino",
        4: "Martin Scorsese",
        5: "Hayao Miyazaki",
        6: "Stanley Kubrick",
        7: "Francis Ford Coppola",
        8: "Alfred Hitchcock",
        9: "Spike Lee",
        10: "David Fincher"
    }
    mycursor = mydb.cursor()
    for key in sorted(director_names):
        director_id = key
        director_name = director_names[key]
        sql = "INSERT INTO directors (director_id, director_name) VALUES (%s, %s)"
        val = (director_id, director_name)
        mycursor.execute(sql, val)
        mydb.commit()
    mycursor.close()
    print("10 diretores inseridos com sucesso!")

def insert_random_styles():
    styles = {
        1: "Action",
        2: "Comedy",
        3: "Drama",
        4: "Horror",
        5: "Thriller",
        6: "Romance",
        7: "Science Fiction",
        8: "Documentary",
        9: "Animation",
        10: "Musical",
        11: "Mystery",
        12: "Western",
        13: "Fantasy",
        14: "Adventure",
        15: "Crime"
    }
    mycursor = mydb.cursor()
    for key in sorted(styles):
        style_num = key
        style_title = styles[key]
        sql = "INSERT INTO styles (style_num, style_title) VALUES (%s, %s)"
        val = (style_num, style_title)
        mycursor.execute(sql, val)
        mydb.commit()
    mycursor.close()
    print("15 estilos inseridos na tabela com sucesso!")

def insert_movie_oscars():
    movie_oscars = {
        1: "Best Picture",
        2: "Best Director",
        3: "Best Original Screenplay",
        4: "Best Adapted Screenplay",
        5: "Best Cinematography",
        6: "Best Film Editing",
        7: "Best Production Design",
        8: "Best Costume Design",
        9: "Best Sound Mixing",
        10: "Best Original Score",
        11: "Best Visual Effects"
    }
    mycursor = mydb.cursor()
    for key in sorted(movie_oscars):
        oscar_id = key
        oscar_award = movie_oscars[key]
        sql = "INSERT INTO oscars (oscar_id, oscar_award) VALUES (%s, %s)"
        val = (oscar_id, oscar_award)
        mycursor.execute(sql, val)
        mydb.commit()
    mycursor.close()
    print("11 oscares inseridos com sucesso!")

#ADD THE RANDOM STUFF FOR THE FOREIGN KEY TABLES

def add_random_movie_styles():
    mycursor = mydb.cursor()
    mycursor.execute("USE TPSIPL1022_SQL")
    select_movies_sql = "SELECT id FROM movies"
    mycursor.execute(select_movies_sql)
    movies = mycursor.fetchall()
    select_styles_sql = "SELECT style_num FROM styles"
    mycursor.execute(select_styles_sql)
    styles = mycursor.fetchall()
    insert_sql = "INSERT INTO movie_styles (movie_id, style_id) VALUES (%s, %s)"
    for movie in movies:
        # Choose a random number of styles for the movie, up to 3
        num_styles = random.randint(1, 3)
        # Choose num_styles random styles
        movie_styles = random.sample(styles, num_styles)
        # Add the styles to the movie_styles table
        for style in movie_styles:
            val = (movie[0], style[0])
            mycursor.execute(insert_sql, val)
    mydb.commit()
    mycursor.close()
    print("Estilo de filme aleatoriamente adicionado em movie_styles.")

def add_movie_oscars():
    mycursor = mydb.cursor()
    mycursor.execute("USE TPSIPL1022_SQL")
    movie_ids = [i for i in range(1, 31)]
    oscar_ids = [i for i in range(1, 12)]
    oscars_for_movie = {}
    # Assign random oscars to each movie
    for i in range(1, 31):
        if i <= 2:
            # For first two movies, assign 8 random oscars
            oscars_for_movie[i] = random.sample(oscar_ids, 8)
        else:
            # For the rest of the movies, assign 0 to 3 random oscars
            oscars_for_movie[i] = random.sample(oscar_ids, random.randint(0, 3))
    # Insert movie oscars into the table
    for movie_id, oscar_ids in oscars_for_movie.items():
        for oscar_id in oscar_ids:
            values = (movie_id, oscar_id)
            mycursor.execute("INSERT INTO movie_oscars (movie_id, oscar_idd) VALUES (%s, %s)", values)
    mydb.commit()
    mycursor.close()
    print("Oscares atribuidos a filmes com sucesso!")


def add_random_director_movies():
    mycursor = mydb.cursor()
    mycursor.execute("USE TPSIPL1022_SQL")

    director_ids = list(range(1, 11))  # 10 directors
    movie_ids = list(range(1, 31))  # 30 movies
    num_relationships = random.randint(10, 30)  # add 10-30 director-movie relationships

    for i in range(num_relationships):
        director_id = random.choice(director_ids)
        movie_id = random.choice(movie_ids)
        insert_sql = "INSERT INTO director_movies (director_idd, movie_id) VALUES (%s, %s)"
        insert_vals = (director_id, movie_id)
        mycursor.execute(insert_sql, insert_vals)

    mydb.commit()
    mycursor.close()
    print(f"{num_relationships} relacionamentos diretor-filme adicionados à tabela director_movies.")

def create_database():
    while True:
        option = input("Deseja criar uma(s) nova(s) tabela(s)? Irá apagar todas a(s) tabela(s) anterior(es)... (y/n): ")
        if option =="y":

            mycursor = mydb.cursor()

            mycursor.execute("USE TPSIPL1022_SQL")

            # --------------------------------------------------------------#
            #Drop tables if they already exist
            mycursor.execute("DROP TABLE IF EXISTS movie_styles")
            mycursor.execute("DROP TABLE IF EXISTS movie_oscars")
            mycursor.execute("DROP TABLE IF EXISTS director_movies")

            #Querys to create the 4 main tables
            mycursor.execute("DROP TABLE IF EXISTS movies")
            mycursor.execute("""CREATE TABLE IF NOT EXISTS movies (
                             id INT PRIMARY KEY AUTO_INCREMENT,
                             movie_title VARCHAR(255) NOT NULL,
                             movie_description VARCHAR(255),
                             movie_year CHAR(4) NOT NULL
                            )""")

            mycursor.execute("DROP TABLE IF EXISTS styles")
            mycursor.execute("""CREATE TABLE IF NOT EXISTS styles (
                             style_num INT PRIMARY KEY,
                             style_title VARCHAR(255) NOT NULL
                            )""")

            mycursor.execute("DROP TABLE IF EXISTS directors")
            mycursor.execute("""CREATE TABLE IF NOT EXISTS directors (
                             director_id INT PRIMARY KEY,
                             director_name VARCHAR(255) NOT NULL,
                             director_description VARCHAR(255)
                            )""")

            mycursor.execute("DROP TABLE IF EXISTS oscars")
            mycursor.execute("""CREATE TABLE IF NOT EXISTS oscars (
                             oscar_id INT PRIMARY KEY,
                             oscar_award VARCHAR(255) NOT NULL,
                             oscar_description VARCHAR(255)
                            )""")

            #--------------------------------------------------------------#
            #Querys to create the 3 tables using foreign keys
            mycursor.execute("""CREATE TABLE IF NOT EXISTS movie_styles (
                                movie_id INT,
                                style_id INT,
                                FOREIGN KEY (movie_id) REFERENCES movies(id),
                                FOREIGN KEY (style_id) REFERENCES styles(style_num)
                                )""")

            mycursor.execute("""CREATE TABLE IF NOT EXISTS movie_oscars (
                                movie_id INT,
                                oscar_idd INT,
                                FOREIGN KEY (movie_id) REFERENCES movies(id),
                                FOREIGN KEY (oscar_idd) REFERENCES oscars(oscar_id)
                                )""")

            mycursor.execute("""CREATE TABLE IF NOT EXISTS director_movies (
                             director_idd INT,
                             movie_id INT,
                             FOREIGN KEY (director_idd) REFERENCES directors(director_id),
                             FOREIGN KEY (movie_id) REFERENCES movies(id)
                            )""")

            # --------------------------------------------------------------#
            print("\nTabelas criadas com sucesso! Quaisquer tabelas anteriores foram apagadas com sucesso...\n")

            #Insert data
            insert_random_movies()
            insert_random_directors()
            insert_random_styles()
            insert_movie_oscars()

            #Insert data
            add_random_movie_styles()
            add_movie_oscars()
            add_random_director_movies()

            mycursor.close()
            print("\nO programa ira iniciar!")
            break
        elif option == "n":
            print("\nO programa ira iniciar!")
            break
        else:
            print("Responda apenas 'y' ou 'n'!")

# --------------------------------------------------------------#
# #####################\.FUNCTIONS (MAIN)./#################### #
# --------------------------------------------------------------#

def display_table(table_name):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table_name}")
    rows = mycursor.fetchall()
    mycursor.close()
    if not rows:
        print(f"A tabela {table_name} está vazia.")
        return
    headers = [i[0] for i in mycursor.description]
    table = PrettyTable(headers)
    for row in rows:
        table.add_row(row)
    table.max_width = 65  # set the max width of columns to 30 characters
    print(f"Tabela {table_name}:")
    print(table)


def add_movie():
    title = input("Digite o título do filme: ")
    print("Caso não queiras adicionar uma descrição, deixe em branco.")
    description = input("Digite a descrição do filme: ")
    year = input("Digite o ano do filme: ")

    # Retrieve the list of available movie styles
    mycursor = mydb.cursor()
    mycursor.execute("SELECT style_num, style_title FROM styles")
    style_rows = mycursor.fetchall()

    # Print the available movie styles as a menu
    print("Selecione um estilo (número):")
    for style_row in style_rows:
        print(f"{style_row[0]}. {style_row[1]}")

    # Ask the user to select a movie style
    style_num = int(input("Escolha o número do estilo: "))

    # Insert the movie into the movies table
    sql = "INSERT INTO movies (movie_title, movie_description, movie_year) VALUES (%s, %s, %s)"
    val = (title, description, year)
    mycursor.execute(sql, val)
    mydb.commit()

    # Get the ID of the newly added movie
    movie_id = mycursor.lastrowid

    # Associate the movie with the selected movie style
    sql = "INSERT INTO movie_styles (movie_id, style_id) VALUES (%s, %s)"
    val = (movie_id, style_num)
    mycursor.execute(sql, val)
    mydb.commit()

    # Ask the user how many Oscars the movie won (max 6)
    num_oscars = int(input("Digite o número de Oscars que o filme ganhou (máximo 6): "))
    num_oscars = min(num_oscars, 6)  # Ensure num_oscars <= 6

    # Add random Oscars won to the movie_oscars table
    oscar_ids = random.sample(range(1, 12), num_oscars)  # There are 11 oscars (IDs from 1 to 11)
    for oscar_id in oscar_ids:
        sql = "INSERT INTO movie_oscars (movie_id, oscar_idd) VALUES (%s, %s)"
        val = (movie_id, oscar_id)
        mycursor.execute(sql, val)
        mydb.commit()

    # Ask the user how many directors the movie had (max 2)
    num_directors = int(input("Digite o número de diretores que o filme teve (máximo 2): "))
    num_directors = min(num_directors, 2)  # Ensure num_directors <= 2

    # Add random directors to the director_movies table
    director_ids = random.sample(range(1, 11), num_directors)  # There are 10 directors (IDs from 1 to 10)
    for director_id in director_ids:
        sql = "INSERT INTO director_movies (director_idd, movie_id) VALUES (%s, %s)"
        val = (director_id, movie_id)
        mycursor.execute(sql, val)
        mydb.commit()

    mycursor.close()
    print(f"{title} adicionado à tabela de filmes.")
    display_table("movies")


def remove_movie():
    movie_id = input("Digite o ID do filme para remover: ")
    mycursor = mydb.cursor()
    mycursor.execute("USE TPSIPL1022_SQL")

    # Remove related rows in movie_oscars table
    sql = "DELETE FROM movie_oscars WHERE movie_id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)

    # Remove related rows in director_movies table
    sql = "DELETE FROM director_movies WHERE movie_id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)

    # Remove related rows in movie_styles table
    sql = "DELETE FROM movie_styles WHERE movie_id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)

    # Remove movie row in movies table
    sql = "DELETE FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    print(f"Filme com ID {movie_id} removido da tabela de filmes.")
    display_table("movies")


# Asks for movie information to update
def edit_movie():
    movie_id = input("Insira o ID do filme: ")
    print("Deixe os campos em branco para permanecerem inalterados.")
    title = input(f"Insira um novo titulo para o filme: ")
    description = input(f"Insira uma nova descrição: ")
    year = input(f"Insira um novo ano para o filme: ")

    # Establishes connection with database and sets schema to be used
    mycursor = mydb.cursor()

    # Constructs the SQL statement to update the movie information
    update_sql = "UPDATE movies SET "
    update_vals = []
    if title:
        update_sql += "movie_title = %s, "
        update_vals.append(title)
    if description:
        update_sql += "movie_description = %s, "
        update_vals.append(description)
    if year:
        update_sql += "movie_year = %s, "
        update_vals.append(year)
    if not (title or description or year):
        print("Para editar este filme, porfavor introduza o titulo e o ano.")
        return
    update_sql = update_sql.rstrip(", ")
    update_sql += " WHERE id = %s"
    update_vals.append(movie_id)

    # Executes the SQL statement to update the movie information
    mycursor.execute(update_sql, tuple(update_vals))
    mydb.commit()
    mycursor.close()

    # Displays the updated movies table
    print(f"Filme com o ID {movie_id} atualizado na tabela movies!.")
    display_table("movies")


# Fetches all movies and styles from the database and displays them in a table
def list_movies_by_style():
    # Establishes connection with database
    mycursor = mydb.cursor()

    # Constructs the SQL statement to fetch all movies and styles
    mycursor.execute("""
        SELECT s.style_title, m.movie_title, m.movie_year
        FROM movie_styles ms
        INNER JOIN movies m ON ms.movie_id = m.id
        INNER JOIN styles s ON ms.style_id = s.style_num
        ORDER BY s.style_title
    """)

    # Fetches all rows returned by the SQL statement
    rows = mycursor.fetchall()
    mycursor.close()

    if not rows:
        print("Não há filmes cadastrados.")
        return

    # Formats the rows as a table and displays it
    table = PrettyTable()
    table.field_names = ["Estilo", "Título", "Ano"]
    table.align["Estilo"] = "l"
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.max_width = 140

    current_style = None
    for row in rows:
        style_title = row[0]
        movie_title = row[1]
        movie_year = row[2]

        if current_style != style_title:
            current_style = style_title
            table.add_row([style_title, "", ""])

        table.add_row(["", movie_title, movie_year])

    print(table)



def list_movies_by_director():
    # Connect to the database
    mycursor = mydb.cursor()

    # Select the director name, movie title, and movie year from the tables
    mycursor.execute("""
        SELECT d.director_name, m.movie_title, m.movie_year
        FROM director_movies dm
        INNER JOIN movies m ON dm.movie_id = m.id
        INNER JOIN directors d ON dm.director_idd = d.director_id
        ORDER BY d.director_name
    """)

    # Fetch all the rows from the result set
    rows = mycursor.fetchall()

    # Close the cursor
    mycursor.close()

    # If there are no rows, print a message and return
    if not rows:
        print("Não há filmes cadastrados.")
        return

    # Create a pretty table to display the data
    table = PrettyTable()
    table.field_names = ["Diretor", "Título", "Ano"]
    table.align["Diretor"] = "l"
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.max_width = 140

    # Keep track of the current director name
    current_director = None

    # Iterate through the rows and add them to the table
    for row in rows:
        director_name = row[0]
        movie_title = row[1]
        movie_year = row[2]

        # If the director name has changed, add a row with the new director name
        if current_director != director_name:
            current_director = director_name
            table.add_row([director_name, "", ""])

        # Add a row for the movie title and year
        table.add_row(["", movie_title, movie_year])

    # Print the table
    print(table)


# Define a function to list movies by year
def list_movies_by_year():
    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # Execute a query to select movie year and title, ordered by year
    mycursor.execute("""
        SELECT movie_year, movie_title
        FROM movies
        ORDER BY movie_year
    """)

    # Fetch all the results from the query
    rows = mycursor.fetchall()

    # Close the cursor object
    mycursor.close()

    # If there are no rows returned from the query, print a message and return
    if not rows:
        print("Não há filmes cadastrados.")
        return

    # Create a PrettyTable object to display the results in a nice format
    table = PrettyTable()

    # Set the column names for the table
    table.field_names = ["Ano", "Título"]

    # Set the alignment of the columns
    table.align["Ano"] = "l"
    table.align["Título"] = "l"

    # Set the maximum width of the table
    table.max_width = 140

    # Initialize a variable to keep track of the current year being displayed
    current_year = None

    # Loop through the rows returned from the query
    for row in rows:
        # Get the movie year and title from the row
        movie_year = row[0]
        movie_title = row[1]

        # If the current year being displayed is different from the movie year,
        # add a new row to the table with the year and an empty string for the title
        if current_year != movie_year:
            current_year = movie_year
            table.add_row([movie_year, ""])

        # Add a new row to the table with an empty string for the year and the movie title
        table.add_row(["", movie_title])

    # Print the table to the console
    print(table)


# define a function to filter movies by year
def filter_movies_by_year():
    # create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # execute a SQL query to get all distinct years from the movies table
    mycursor.execute("""
        SELECT DISTINCT movie_year
        FROM movies
        ORDER BY movie_year
    """)

    # fetch all the results and create a list of years as strings
    years = [str(row[0]) for row in mycursor.fetchall()]

    # if there are no years available, print a message and return
    if not years:
        print("Não há filmes cadastrados.")
        return

    # print the available years
    print("Anos disponíveis:")
    for year in years:
        print(year)

    # loop until a valid year is entered by the user
    while True:
        try:
            # ask the user to enter a year
            selected_year = int(input("Digite o ano para filtrar: "))

            # check if the entered year is available
            if str(selected_year) not in years:
                raise ValueError

            # if the year is available, break out of the loop
            break
        except ValueError:
            # if an invalid year is entered, print an error message and continue looping
            print("Ano inválido. Tente novamente.")

    # execute a SQL query to get all movies for the selected year, sorted by title
    mycursor.execute(f"""
        SELECT movie_title, movie_year
        FROM movies
        WHERE movie_year = '{selected_year}'
        ORDER BY movie_title
    """)

    # fetch all the results
    rows = mycursor.fetchall()

    # close the cursor object
    mycursor.close()

    # if there are no movies available for the selected year, print a message and return
    if not rows:
        print(f"Não há filmes cadastrados para o ano {selected_year}.")
        return

    # create a table object to display the results
    table = PrettyTable()
    table.field_names = ["Título", "Ano"]
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.max_width = 140

    # add each movie to the table
    for row in rows:
        movie_title = row[0]
        movie_year = row[1]
        table.add_row([movie_title, movie_year])

    # print the table
    print(table)



# This function filters movies by style.
def filter_movies_by_style():
    # Retrieve the available styles from the database.
    mycursor = mydb.cursor()
    mycursor.execute("SELECT DISTINCT style_title FROM styles ORDER BY style_title")
    style_rows = mycursor.fetchall()
    mycursor.close()

    # If no styles are available, print a message and return.
    if not style_rows:
        print("Não há estilos cadastrados.")
        return

    # Store the available styles in a list.
    styles = [row[0] for row in style_rows]

    # Print the available styles.
    print("Estilos disponíveis:")
    for i, style in enumerate(styles):
        print(f"{i + 1}. {style}")

    # Prompt the user to select a style by number.
    selected_style = input("Selecione um estilo (número): ")

    # Validate the user's input.
    try:
        selected_style = int(selected_style)
        if not 1 <= selected_style <= len(styles):
            raise ValueError
    except ValueError:
        print("Opção inválida.")
        return

    # Retrieve the movies that match the selected style from the database.
    selected_style = styles[selected_style - 1]
    mycursor = mydb.cursor()
    mycursor.execute(f"""
        SELECT s.style_title, m.movie_title, m.movie_year
        FROM movie_styles ms
        INNER JOIN movies m ON ms.movie_id = m.id
        INNER JOIN styles s ON ms.style_id = s.style_num
        WHERE s.style_title = %s
        ORDER BY m.movie_year DESC
    """, (selected_style,))
    rows = mycursor.fetchall()
    mycursor.close()

    # If no movies are found, print a message and return.
    if not rows:
        print("Não há filmes cadastrados com este estilo.")
        return

    # Display the movies that match the selected style.
    table = PrettyTable()
    table.field_names = ["Estilo", "Título", "Ano"]
    table.align["Estilo"] = "l"
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.max_width = 140

    for row in rows:
        style_title = row[0]
        movie_title = row[1]
        movie_year = row[2]
        table.add_row([style_title, movie_title, movie_year])

    print(table)


def filter_movies_by_style():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT style_title FROM styles")
    style_rows = mycursor.fetchall()

    # Present the available styles
    available_styles = [row[0] for row in style_rows]
    print("Estilos disponíveis:")
    print(", ".join(available_styles))

    # Prompt the user to enter the name of the style they want to filter the movies by
    style_name = input("Digite o nome do estilo: ")

    # Validate the input
    while style_name not in available_styles:
        style_name = input("Estilo inválido. Digite novamente: ")

    # Retrieve the movies filtered by style
    mycursor.execute("""
        SELECT s.style_title, m.movie_title, m.movie_year
        FROM movie_styles ms
        INNER JOIN movies m ON ms.movie_id = m.id
        INNER JOIN styles s ON ms.style_id = s.style_num
        WHERE s.style_title = %s
        ORDER BY m.movie_title
    """, (style_name,))
    rows = mycursor.fetchall()
    mycursor.close()

    if not rows:
        print(f"Não há filmes cadastrados com o estilo {style_name}.")
        return

    # Display the filtered movies
    table = PrettyTable()
    table.field_names = ["Estilo", "Título", "Ano"]
    table.align["Estilo"] = "l"
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.max_width = 140

    for row in rows:
        style_title = row[0]
        movie_title = row[1]
        movie_year = row[2]

        table.add_row([style_title, movie_title, movie_year])

    print(table)


#This function lists movies within a user-specified year interval
def list_movies_by_year_interval():
    # Get the minimum and maximum year from the database
    mycursor = mydb.cursor()
    mycursor.execute("""
    SELECT DISTINCT movie_year FROM movies ORDER BY movie_year ASC
    """)
    rows = mycursor.fetchall()
    mycursor.close()

    # If there are no movies in the database, print a message and return
    if not rows:
        print("Não há filmes cadastrados.")
        return

    # Get the minimum and maximum years
    min_year = rows[0][0]
    max_year = rows[-1][0]

    # Prompt the user to enter a start year and end year
    while True:
        start_year = input(f"Digite o ano de início (entre {min_year} e {max_year}): ")
        end_year = input(f"Digite o ano de fim (entre {min_year} e {max_year}): ")

        # Validate the input
        if not start_year.isdigit() or not end_year.isdigit():
            print("Por favor, digite apenas números.")
            continue

        start_year = int(start_year)
        end_year = int(end_year)

        if start_year > end_year:
            print("O ano de início não pode ser maior que o ano de fim.")
            continue

        if start_year < int(min_year) or end_year > int(max_year):
            print(f"Por favor, digite um ano entre {min_year} e {max_year}.")
            continue

        break

    # Retrieve the movies within the specified year interval
    mycursor = mydb.cursor()
    mycursor.execute(f"""
        SELECT movie_title, movie_year
        FROM movies
        WHERE movie_year BETWEEN {start_year} AND {end_year}
        ORDER BY movie_year ASC
    """)
    rows = mycursor.fetchall()
    mycursor.close()

    # If there are no movies within the specified year interval, print a message and return
    if not rows:
        print(f"Não há filmes cadastrados entre {start_year} e {end_year}.")
        return

    # Display the filtered movies
    table = PrettyTable()
    table.field_names = ["Título", "Ano"]
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.max_width = 140

    for row in rows:
        movie_title = row[0]
        movie_year = row[1]

        table.add_row([movie_title, movie_year])

    print(table)




def list_movies_by_director_and_year_range():
    mycursor = mydb.cursor()

    # Get a list of all available directors
    mycursor.execute("""
        SELECT director_id, director_name
        FROM directors
        ORDER BY director_id
    """)
    director_rows = mycursor.fetchall()

    # Print the list of available directors
    print("Diretores disponíveis:")
    for row in director_rows:
        print(f"{row[0]} - {row[1]}")
    print()

    # Get user input for director ID
    director_id = input("Digite o ID do diretor: ")
    while not director_id.isdigit():
        director_id = input("ID inválido. Por favor, digite um ID numérico: ")

    # Get user input for start year
    start_year = input("Digite o ano inicial: ")
    while not (start_year.isdigit() and len(start_year) == 4):
        start_year = input("Ano inválido. Por favor, digite um ano válido no formato yyyy: ")

    # Get user input for end year
    end_year = input("Digite o ano final: ")
    while not (end_year.isdigit() and len(end_year) == 4):
        end_year = input("Ano inválido. Por favor, digite um ano válido no formato yyyy: ")

    # Make sure start year is before end year
    if start_year > end_year:
        print("Ano inicial deve ser menor que ano final.")
        return

    # Execute the SQL query to get the list of movies
    mycursor.execute("""
        SELECT m.movie_title, m.movie_year
        FROM movies m
        INNER JOIN director_movies dm ON m.id = dm.movie_id
        WHERE dm.director_idd = %s AND m.movie_year BETWEEN %s AND %s
        ORDER BY m.movie_year
    """, (director_id, start_year, end_year))
    rows = mycursor.fetchall()
    mycursor.close()

    if not rows:
        print(f"Não há filmes do diretor {director_id} no período de {start_year} a {end_year}.")
        return

    # Print the list of movies
    table = PrettyTable()
    table.field_names = ["Título", "Ano"]
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.max_width = 140

    for row in rows:
        table.add_row([row[0], row[1]])

    print(table)


#This function lists all movies that have won more than 5 Oscars
def oscar_winner_movies():
    # Create a cursor to execute SQL queries
    mycursor = mydb.cursor()

    # Execute the SQL query to get the list of movies with more than 5 Oscar wins
    mycursor.execute("""
        SELECT m.movie_title, COUNT(*) as oscar_wins
        FROM movies m
        INNER JOIN movie_oscars mo ON m.id = mo.movie_id
        INNER JOIN oscars o ON mo.oscar_idd = o.oscar_id
        GROUP BY m.movie_title
        HAVING oscar_wins > 5
        ORDER BY oscar_wins DESC
    """)

    # Fetch all the rows returned by the SQL query
    rows = mycursor.fetchall()

    # Close the cursor
    mycursor.close()

    # Check if any rows were returned
    if not rows:
        print("Não há filmes vencedores de Oscar.")
        return

    # Print the list of movies with their number of Oscar wins
    table = PrettyTable()
    table.field_names = ["Título", "Quantidade de Oscars"]
    table.align["Título"] = "l"
    table.align["Quantidade de Oscars"] = "r"
    table.max_width = 120

    for row in rows:
        movie_title = row[0]
        oscar_wins = row[1]
        table.add_row([movie_title, oscar_wins])

    print(table)


#This function lists all movies with their release year and age in years
def list_movies_with_age():
    # Create a cursor to execute SQL queries
    mycursor = mydb.cursor()

    # Execute the SQL query to get the list of all movies with their release year
    mycursor.execute("""
        SELECT movie_title, movie_year
        FROM movies
    """)

    # Fetch all the rows returned by the SQL query
    rows = mycursor.fetchall()

    # Close the cursor
    mycursor.close()

    # Check if any rows were returned
    if not rows:
        print("Não há filmes cadastrados.")
        return

    # Print the list of movies with their release year and age in years
    table = PrettyTable()
    table.field_names = ["Título", "Ano", "Idade (Anos)"]
    table.align["Título"] = "l"
    table.align["Ano"] = "l"
    table.align["Idade"] = "l"
    table.max_width = 140

    current_year = datetime.now().year
    for row in rows:
        movie_title = row[0]
        movie_year = row[1]
        movie_age = current_year - int(movie_year)

        table.add_row([movie_title, movie_year, movie_age])

    print(table)


# This function displays the number of Oscars won by each movie.
# It retrieves the data from three tables: 'oscars', 'movie_oscars',
# and 'movies'. It groups the results by the Oscar award and uses
# GROUP_CONCAT() to concatenate the movie titles for each award.
# Finally, it prints the results to the console.
def display_oscars_by_movie():
    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT oscar_award, GROUP_CONCAT(movie_title SEPARATOR ', ') AS movies
        FROM oscars
        JOIN movie_oscars ON oscars.oscar_id = movie_oscars.oscar_idd
        JOIN movies ON movies.id = movie_oscars.movie_id
        GROUP BY oscar_award
    """)
    rows = mycursor.fetchall()
    mycursor.close()

    print("Oscars por filme:")
    for row in rows:
        print(row[0] + " - " + row[1])


# This function displays the number of Oscars won by a movie
# specified by the user's input of its ID. It retrieves the
# data from the 'oscars' and 'movie_oscars' tables and counts
# the number of rows returned. It then prints the results to
# the console.
def display_oscars_by_movie_id():
    # get user input for movie ID
    movie_id = input("Digite o ID do filme: ")

    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT COUNT(oscars.oscar_award) AS num_oscars
        FROM oscars
        JOIN movie_oscars ON oscars.oscar_id = movie_oscars.oscar_idd
        WHERE movie_oscars.movie_id = %s
    """, (movie_id,))
    rows = mycursor.fetchall()
    mycursor.close()

    if rows:
        print("O filme com ID " + movie_id + " ganhou " + str(rows[0][0]) + " Oscars.")
    else:
        print("Não foi encontrado um filme com o ID informado.")


# This function displays the number of Oscars won by each genre.
# It retrieves the data from four tables: 'styles', 'movie_styles',
# 'movies', and 'movie_oscars'. It groups the results by genre and
# uses COUNT() to count the number of Oscars won by each genre.
# Finally, it prints the results to the console.
def display_oscars_by_genre():
    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT styles.style_title, COUNT(movie_oscars.oscar_idd) AS num_oscars
        FROM styles
        JOIN movie_styles ON styles.style_num = movie_styles.style_id
        JOIN movies ON movies.id = movie_styles.movie_id
        JOIN movie_oscars ON movies.id = movie_oscars.movie_id
        GROUP BY styles.style_title
    """)
    rows = mycursor.fetchall()
    mycursor.close()

    print("Oscars por género:")
    for row in rows:
        print(row[0] + " - " + str(row[1]) + " Oscars")
