from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create or access the 'movieDB' database
db = client['movieDB']

# Create or access the 'movies' collection
collection = db['movies']

@app.route('/')
def index():
    movies = collection.find()  # Fetch all movies from MongoDB
    return render_template('index.html', movies=movies)

@app.route('/movie/<int:id>')
def movie_details(id):
    # Fetch the movie details by ID
    movie = collection.find_one({"id": id})  # Find the movie by its unique 'id'
    
    if movie is None:
        return "Movie not found", 404  # Return a 404 if movie is not found
    
<<<<<<< Updated upstream
    return render_template('movie_details.html', movie=movie)
=======
    return render_template('index.html', movies=movies, page=page)
@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    # Fetch movie details and download links from the database
    movie = get_movie_by_id(movie_id)
    download_links = get_download_links(movie_id)
    
    return render_template('movie_details.html', movie=movie, download_links=download_links)
>>>>>>> Stashed changes

if __name__ == '__main__':
    app.run(debug=True)
