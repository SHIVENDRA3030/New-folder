from pymongo import MongoClient

# Connect to MongoDB server (assuming it's running on localhost and default port 27017)
client = MongoClient('mongodb://localhost:27017/')

# Create a new database (if it doesn't exist, MongoDB will create it when you first use it)
db = client['movieDB']  # 'movieDB' is the name of your new database

# Create a new collection (if it doesn't exist, MongoDB will create it when you first use it)
collection = db['movies']  # 'movies' is the name of your collection

# Insert a sample document (you can customize this to match your movie data)
movie_data = {
    'title': 'Inception',
    'description': 'A mind-bending thriller about dream manipulation.',
    'upload_date': '2025-01-19',
    'image_url': 'https://example.com/inception.jpg',
    'watch_links': ['https://example.com/watch/inception'],
    'download_links': {
        '480p': 'https://example.com/download/inception_480p',
        '720p': 'https://example.com/download/inception_720p',
        '1080p': 'https://example.com/download/inception_1080p',
    }
}

# Insert the movie data into the 'movies' collection
collection.insert_one(movie_data)

print("Database and collection created successfully, and data inserted!")