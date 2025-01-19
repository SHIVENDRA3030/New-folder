from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client.movieDB  # Your database name
movies_collection = db.movies  # Your collection name

@app.route('/')
def home():
    page = int(request.args.get('page', 1))  # Page number
    movies_per_page = 10
    movies = list(movies_collection.find().sort('upload_date', -1).skip((page - 1) * movies_per_page).limit(movies_per_page))
    
    return render_template('index.html', movies=movies, page=page)

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = movies_collection.find_one({'_id': movie_id})
    return render_template('movie_details.html', movie=movie)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = list(movies_collection.find({"title": {"$regex": query, "$options": "i"}}))
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
