from pathlib import Path


FILE_NAME = "Filminator_9000.html"

# path to directory with 'index_template.html'
project_root = Path(__file__).resolve().parent.parent
html_path = project_root / 'static' / 'index_template.html'


def read_html(file_path):
    """ 
    Read an HTML file.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def serialize_movie(movie, info):
    """ 
    Serialization of a single movie object. 
    """
    output = ''
    output += '<li>\n'
    output += '<div class="movie">\n'
    output += '<img class="movie-poster"\n'
    output += f'src="{info.get("poster")}"\n'
    output += 'title=""/>\n'
    output += '<div class="movie-rating-country">\n'
    output += f'<div class="movie-rating">⭐ {info.get("rating")}</div>\n'
    output += '<div class="movie-country">\n' 
    output += f'<img src="{info.get("country")}" width="100%" />\n'
    output += '</div>'
    output += '</div>'
    output += f'<div class="movie-title">{movie}</div>\n'
    output += f'<div class="movie-year">{info.get("year")}</div>\n'
    output += '</div>'
    output += '</li>\n'
    return output

    
def get_movie_info(data):
    """ 
    Displays poster, title, year, rating, country flag from the database.
    """
    output = ""
    for movie, info in data.items():   
        output += serialize_movie(movie, info) 
    return output


def new_html_data(file_path, movie_data): 
    """ 
    Create a new HTML file with the necessery information.
    """
    with open(file_path, "w", encoding="utf-8") as handle:
        html_data = read_html(html_path)
        movies_info = get_movie_info(movie_data)
        new = html_data.replace("__TEMPLATE_MOVIE_GRID__", movies_info)
        return handle.write(new)

