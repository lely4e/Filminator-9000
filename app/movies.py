import sys
import statistics
import random
from termcolor import colored
from utils.color import COLOR_PROMPT, COLOR_SUCCESS, COLOR_WARNING, COLOR_MENU, COLOR_ERROR, COLOR_INPUT
import movie_storage.movie_storage as storage
import movie_storage.movie_fetcher as fetcher
from utils.movies_web_generator import new_html_data, FILE_NAME
from utils.flag import fetch_flag


def header_displayed_on_the_screen():
    """
    Displays the header on the screen.
    """
    print(colored("***** MY MOVIES DATABASE *****", COLOR_MENU))


def displayed_on_the_screen():
    """
    Displays the main menu options from 0 to 9 on the screen.
    """
    print(colored("""
Menu:
0. Exit
1. Movie Database
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Movies sorted by year
10. Generate website
""", COLOR_MENU))


def choose_the_option():
    """
    Allows the user to select an action from the menu
    and execute the corresponding function.
    """
    choices = {
        "0": exit_the_program,
        "1": list_movies,
        "2": add_movie,
        "3": delete_movie,
        "4": update_movie_rating,
        "5": stats,
        "6": random_movie,
        "7": search_movie,
        "8": movies_sorted_by_rating,
        "9": movies_sorted_by_year,
        "10": generate_website
    }
    while True:
        user_choice = input(colored("\nEnter choice (1-9): ", COLOR_INPUT)).strip()
        print()
        action = choices.get(user_choice)

        if action:
            action()
        else:
            print(colored("Invalid choice!", COLOR_ERROR))

        continue_action = input(colored(
                                "\nPress enter to continue"
                                "(or type 'exit' to quit): ", COLOR_PROMPT)).strip()

        if continue_action == "exit":
            exit_the_program()
        print()
        displayed_on_the_screen()


def list_movies():
    """
    Displays the full list of movies with their title, year and rating.
    """
    movies = storage.list_movies()
    if not movies:
        print(colored("Movies database is empty", COLOR_WARNING))
    print(f"{len(movies)} movies in total\n")
    for movie, data in movies.items():
        print(f"{movie} ({data['year']}): {data['rating']}")


def find_movie(movie_name):
    """
    Search for the movie name in movies database.

    Args:
        movie_name (str): The partial or full movie name to search for.

    Returns:
        dict or None: The matched movie dictionary if found, None otherwise.
    """
    movies = storage.find_movie(movie_name) 
    return movies


def check_integer_year(user_input):
    """
    Check if the user input is an integer year.

    Args:
        user_input (str): The user input.

    Returns:
        int: Valid positive year integer for movie.
    """
    while True:
        try:
            number = int(input(colored(user_input, COLOR_INPUT)))
            if number < 0:
                print(colored("Invalid input! Year must be a number > 0 (e.g. 1994)", COLOR_ERROR))
                continue
            return number
        except ValueError:
            print(colored("Invalid input! Year must be a number (e.g. 1994)", COLOR_ERROR))


def check_float_rating(user_input):
    """
    Check if the user input is a float rating.

    Arg:
        user_input (str): The user input.

    Returns:
        float: Valid positive float rating for movie.
    """
    while True:
        try:
            number = float(input(colored(user_input, COLOR_INPUT)))
            if number > 10 or number < 0:
                print(colored("Invalid input! Rating must be a number between 0-10", COLOR_ERROR))
                continue
            return number
        except ValueError:
            print(colored("Invalid input! Rating must be a number", COLOR_ERROR))


def add_movie():
    """
    Ask the user to add a new movie to the movie's database.
    """
    new_movie_name = input(colored("Enter new movie name: ", COLOR_INPUT)).strip()
    
    # API database
    movies = fetcher.fetch_movie(new_movie_name) 
    
    if movies: 
        if new_movie_name: 
            # check if movie in database
            movie_found = find_movie(new_movie_name) 
            if not movie_found:
                flag = fetch_flag(*movies["Country"]) 
                storage.add_movie(new_movie_name, movies["Year"], movies["imdbRating"], movies["Poster"], flag)
                print(colored(f"Movie '{new_movie_name}' successfully added!", COLOR_SUCCESS))
            else:
                print(colored(f"Movie '{new_movie_name}' already exists!", COLOR_WARNING))
        else:
            print(colored("Movie title is empty", COLOR_ERROR))
            
    else:
        print(colored("Movie doesnt exist in API", COLOR_ERROR))


def delete_movie():
    """
    Delete a movie from the movie's database by title.
    """
    delete_movie_name = input(colored("Enter movie name to delete: ", COLOR_INPUT)).strip()
    if delete_movie_name:
        movie = find_movie(delete_movie_name)

        if movie:
            storage.delete_movie(delete_movie_name)
            print(colored(f"Movie '{delete_movie_name}' successfully deleted!", COLOR_SUCCESS))
        else:
            print(colored(f"Movie '{delete_movie_name}' doesn't exist!", COLOR_ERROR))
    else:
        print(colored("Movie title is empty", COLOR_ERROR))


def update_movie_rating():
    """
    Update the rating and year of a movie from the movie's database.
    """
    update_movie_name = input(colored("Enter movie name: ", COLOR_INPUT)).strip()
    if update_movie_name:
        movie_for_update = find_movie(update_movie_name)

        if movie_for_update:
            update_year = check_integer_year("Enter new movie year (e.g. 1994): ")
            update_rating = check_float_rating("Enter new movie rating (0-10): ")
            storage.update_movie(update_movie_name, update_year, update_rating)
            print(colored(f"Movie '{update_movie_name}' successfully updated", COLOR_SUCCESS))
        else:
            print(colored(f"Movie '{update_movie_name}' doesn't exist!", COLOR_ERROR))

    else:
        print(colored("Movie title is empty", COLOR_ERROR))


def stats():
    """
    Displays the statistics about the movies, including average
    rating, median rating, best and worst movies.
    """
    movies = storage.list_movies()
    if movies:
        movies_rating_list = []
        for movie, data in movies.items():
            movies_rating_list.append(data["rating"])

        average_rating = statistics.mean(movies_rating_list)
        print(f"Average rating: {average_rating:.2f}")

        median_rating = statistics.median(movies_rating_list)
        print(f"Median rating: {median_rating:.2f}")

        max_rating_movie = max(movies.items(), key=lambda m: m[1]["rating"])
        print(f'Best movie: {max_rating_movie[0]}, {max_rating_movie[1]["rating"]}')

        min_rating_movie = min(movies.items(), key=lambda m: m[1]["rating"])
        print(f'Worst movie: {min_rating_movie[0]}, {min_rating_movie[1]["rating"]}')
    else:
        print(colored("Movies database is empty", COLOR_WARNING))


def random_movie():
    """
    Selects and displays a random movie from the movie's database.
    """
    movies = storage.list_movies()
    title, data = random.choice(list(movies.items()))
    print(f'Your movie for tonight: {title}, '
          f'it\'s rated {data["rating"]}')


def search_movie():
    """
    Ask user for the movie name and search for matching
    movies by title.
    """
    movies = storage.list_movies()
    part_movie_name = input(colored("Enter part of movie name: ", COLOR_INPUT)).lower().strip()
    if not part_movie_name:
        print(colored("Movie title is empty", COLOR_ERROR))

    matches_movies = {}

    for movie, data in movies.items():
        if part_movie_name in movie.lower():
            matches_movies[movie] = data
  
    if matches_movies:
        for movie, data in matches_movies.items():
            print(f'{movie}, {data["rating"]}')
    else:
        print(colored(f"The movie '{part_movie_name}' doesn't exist.", COLOR_ERROR))


def movies_sorted_by_rating():
    """
    Displays movies sorted by rating in descending order.
    """
    movies = storage.sorted_movies("rating")
    print(f"{len(movies)} movies in total\n")
    for movie, data in movies.items():
        print(f'{movie}: {data["rating"]}')


def movies_sorted_by_year():
    """
    Displays movies sorted by year in descending or
    not descending order by user choice.
    """
    user_choice = input(colored("Do you want the latest movies first? (Y/N)", COLOR_INPUT)).upper()
    if user_choice in ["Y", "N"]:
        if user_choice == "Y":
            direction = "DESC"
        else:
            direction = "ASC"
            
        movies = storage.sorted_movies("year", direction)
        print(f"{len(movies)} movies in total\n")
        for movie, data in movies.items():
            print(f'{movie} ({data["year"]}): {data["rating"]}')
    else:
        print(colored('Invalid choice, please enter "Y" or "N"', COLOR_ERROR))
        
        
def generate_website():
    """ 
    Generate the website with movies in database.
    """
    movies = storage.list_movies()
    if movies:
        new_html_data(FILE_NAME, movies)
        print(f"Website was successfully generated")


def exit_the_program():
    """
    Exit the program.
    """
    print("Bye!")
    sys.exit()



