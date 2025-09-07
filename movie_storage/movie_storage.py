from sqlalchemy import create_engine, text


# Define the database URL
DB_URL = "sqlite:///data/movies.db"

# Create the engine
engine = create_engine(DB_URL, echo=True)

# Create the movies table if it does not exist
with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL,
            year INTEGER NOT NULL,
            rating REAL NOT NULL,
            poster TEXT,
            country TEXT 
        )
    """))
    connection.commit()

        
def list_movies():
    """Retrieve all movies from the database."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT title, year, rating, poster, country FROM movies"))
        movies = result.fetchall()

    return {row[0]: {"year": row[1], "rating": row[2], "poster": row[3], "country": row[4]} for row in movies}


def find_movie(title):
    """Check if movie input from user exist in database."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT title, year, rating, poster, country FROM movies WHERE title = :title LIMIT 1"), {"title": title})
        movies = result.fetchall()
        if movies: 
            return {row[0]: {"year": row[1], "rating": row[2], "poster": row[3], "country": row[4]} for row in movies} 
        else:
            return [] 


def add_movie(title, year, rating, poster, flag):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """ 
    with engine.connect() as connection:
        try:
            connection.execute(text("INSERT INTO movies (Title, Year, Rating, Poster, Country) VALUES (:title, :year, :rating, :poster, :country)"),
                               {"title": title, "year": year, "rating": rating, "poster": poster, "country": flag})
            connection.commit()
            print(f"Movie '{title}' added successfully.")
        except Exception as e:
            print(f"Error: {e}")
    

def delete_movie(title):
    """Delete a movie from the database."""
    with engine.connect() as connection:
        try:
            result = connection.execute(text("DELETE FROM movies WHERE title = :title"),
                                    {"title": title})
            connection.commit()
            
            if result.rowcount > 0:
                print(f"Movie '{title}' deleted successfully.")
            else:
                print(f"No movie with title '{title}' found")
        except Exception as e:
            print(f"Error: {e}")
                  
                  
def sorted_movies(by, direction="ASC"):
    """Sort movies by year or by rating depends on user choice."""
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT title, year, rating, poster FROM movies ORDER BY {by} {direction}"))
        movies = result.fetchall()
        
        return {row[0]: {"year": row[1], "rating": row[2], "poster": row[3]} for row in movies} 
       



