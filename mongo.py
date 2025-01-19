from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create or access the 'movieDB' database
db = client['movieDB']

# Create or access the 'movies' collection
collection = db['movies']

# Movie data to be inserted
movies_data = [
    {
        "id": 58,
        "title": "Yennai Arindhaal (2015)",
        "links": [
            {"name": "Yennai Arindhaal 2015 1080p AMZN WEB-DL DDP5.1 H.264-PMI.mkv [11.04 GB]", "url": "https://new.gdflix.dad/file/fIwuihcZtw"},
            {"name": "Yennai Arindhaal 2015 720p AMZN WEB-DL DDP5.1 H.264-PMI.mkv [6.03 GB]", "url": "https://new.gdflix.dad/file/cS2GaYHMW8"},
            {"name": "Yennai Arindhaal 2015 1080p AMZN WEB-DL DDP5.1 H.265-PMI.mkv [4.95 GB]", "url": "https://new.gdflix.dad/file/oey9VTyNDt"},
            {"name": "Yennai Arindhaal 2015 720p AMZN WEB-DL DDP5.1 H.265-PMI.mkv [1.8 GB]", "url": "https://new.gdflix.dad/file/tvSuZ1hFRD"}
        ]
    },
    {
        "id": 57,
        "title": "The Calendar Killer (2025)",
        "links": [
            {"name": "The Calendar Killer 2025 1080p AMZN WEB-DL DDP5.1 HEVC - Saon [2.82 GB]", "url": "https://new3.filepress.top/file/67891ce086bd132cd0b7aa54"},
            {"name": "The Calendar Killer 2025 1080p AMZN WEB-DL DDP5.1 HEVC - Saon [2.82 GB]", "url": "https://new10.gdtot.dad/file/3026040725"}
        ]
    },
    {
        "id": 56,
        "title": "Flower Crew: Joseon Marriage Agency S01",
        "links": [
            {"name": "Flower Crew Joseon Marriage Agency S01 1080p AMZN WEB-DL DDP2.0 HEVC - Saon [28.38 GB]", "url": "https://new.gdflix.dad/file/qaLWMDWh9D"},
            {"name": "Flower Crew Joseon Marriage Agency S01 1080p AMZN WEB-DL DDP2.0 HEVC - Saon [28.38 GB]", "url": "https://new10.gdtot.dad/file/30474793191"}
        ]
    },
    {
        "id": 54,
        "title": "XO, Kitty Season 1",
        "links": [
            {"name": "XO Kitty S01 1080p NF WEB-DL DDP5.1 Atmos HEVC - Saon [7.47 GB]", "url": "https://new.gdflix.dad/file/1otGzX4c2q"},
            {"name": "XO Kitty S01 1080p NF WEB-DL DDP5.1 Atmos HEVC - Saon [7.47 GB]", "url": "https://new10.gdtot.dad/file/8019219291"}
        ]
    },
    {
        "id": 55,
        "title": "XO, Kitty Season 2",
        "links": [
            {"name": "XO Kitty S02 1080p NF WEB-DL DDP5.1 Atmos HEVC - Saon [6.19 GB]", "url": "https://new.gdflix.dad/file/OiuOA7au8O"},
            {"name": "XO Kitty S02 1080p NF WEB-DL DDP5.1 Atmos HEVC - Saon [6.19 GB]", "url": "https://new10.gdtot.dad/file/6649449091"}
        ]
    },
    {
        "id": 52,
        "title": "XO, Kitty Season 1",
        "links": [
            {"name": "XO Kitty S01 1080p NF WEB-DL AAC5.1 AV1 - Saon [3.34 GB]", "url": "https://new.gdflix.dad/file/BmCNTGWhiW"},
            {"name": "XO Kitty S01 1080p NF WEB-DL AAC5.1 AV1 - Saon [3.34 GB]", "url": "https://new10.gdtot.dad/file/3587905950"}
        ]
    },
    {
        "id": 53,
        "title": "XO, Kitty Season 2",
        "links": [
            {"name": "XO Kitty S02 1080p NF WEB-DL AAC5.1 AV1 - Saon [2.98 GB]", "url": "https://new.gdflix.dad/file/Ugd7HfNRhQ"},
            {"name": "XO Kitty S02 1080p NF WEB-DL AAC5.1 AV1 - Saon [2.98 GB]", "url": "https://new10.gdtot.dad/file/3196057176"}
        ]
    }
]

# Insert the data into the 'movies' collection
collection.insert_many(movies_data)

print("Data inserted successfully!")
