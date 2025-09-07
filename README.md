![This is an alt text.](Filminator_9000.png "Filminator 9000")

# 🎬 FILMINATOR 9000 – Movie Management and Website Generator
FilmFinder 9000 is a Python-based command-line tool that allows users to manage their own movie database with a futuristic twist. It connects to an external movie API (OMDb) to fetch movie data, which is then stored in a local SQL database for easy access, updates, and offline use.
Through an interactive menu, users can add, delete, search, and sort movies; view statistics; and even generate a full HTML website that displays the movies as posters also fetched from API. Whether you're a film buff or a coding newbie, this tool puts the power of a blockbuster database at your fingertips.


# 💡 What Problem Does It Solve?
Manually managing a movie collection can be tedious, especially when dealing with inconsistent data and formats. FilmFinder 9000 solves this by:
* Automatically fetching and storing movie data from a public API by title
* Letting users interact with their movie collection through a structured menu
* Generating a full website that displays movie information in card format
* Allowing sorting, searching, and statistical insights in seconds
* Persistently storing all data using an SQL database (SQLite)


# 👥 Intended Audience
* Python beginners exploring API usage and database storage
* Students working on film, media, or programming projects
* Hobbyists looking to build a digital movie shelf
* Developers learning full CRUD operations and HTML generation in Python


# 🚀 Usage
*✅ Prerequisites*
* Python 3.8 or higher
* requests, python-dotenv, sqlalchemy, statistics, random, termcolor libraries (included in requirements.txt)

*📦 Installation*
* Clone the repository:
```
git clone https://github.com/your-username/Filminator9000.git
cd Filminator9000
```
* Install dependencies:
```
pip install -r requirements.txt
```
* Create a .env file in the project root:
```
API_KEY=your_api_key_here
```

⚠️ Do not commit your .env file — it should be added to .gitignore to keep credentials secure.



# 💻 How to Run
You will be prompted to enter the name of an animal:
```
Menu:
0. Exit
1. Movie Database (view all movies)
2. Add movie (fetch from API and store)
3. Delete movie
4. Update movie (e.g., title or rating)
5. Stats (average, median, max and min ratings)
6. Random movie
7. Search movie by title
8. Movies sorted by rating
9. Movies sorted by year
10. Generate website (HTML with movie posters)
```

🟢 If movies are found:
* Data is fetched from the API and saved into your local SQL database.
* HTML page is generated with cards showing movie title, poster, year.
* The site can be opened in any browser.

🔴 If the movie is not found:
* An HTML page is still generated, showing a message like: 
```
Movie doesnt exist in API.
```


# ⚙️ Configuration
All API-related values (e.g., keys and endpoints) are stored in the .env file.
The script uses:
* requests – Used to fetch movie data from an external API.
* os – Handles environment variables and file paths securely.
* dotenv (python-dotenv) – Loads sensitive values like API keys from a .env file.
* sqlalchemy – Manages database operations using an object-relational mapping (ORM).
* sys – Enables clean program exits and system-level operations.
* statistics – Calculates average ratings and other statistical insights.
* random – Picks a random movie from the database for fun features.
* termcolor – Adds color to terminal output for a more user-friendly interface.

