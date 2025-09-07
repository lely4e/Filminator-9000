from app.movies import header_displayed_on_the_screen, displayed_on_the_screen, choose_the_option
#from data import movies_web_generator


def main():
    """
    Initialize the movie database and run the interactive
    menu-driven program.

    This function sets up a list of movies, shows the header and menu,
    lets user interact with the database by choosing options.
    """
    header_displayed_on_the_screen()
    displayed_on_the_screen()
    choose_the_option()


if __name__ == "__main__":
    main()