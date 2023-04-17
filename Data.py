# ISO 8601 formatted timestamp
timestamp = 34901204396

users = [
    {"name": "Alice", "userId": "1"},
    {"name": "Bob", "userId": "2"},
    {"name": "Peter", "userId": "3"},
    {"name": "Anna", "userId": "4"},
    {"name": "Jake", "userId": "5"},
]

movies = [
    {
        "title": "The Shawshank Redemption",
        "movieId": 1,
        "year": 1994,
        "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
    },
    {
        "title": "The Godfather",
        "movieId": 2,
        "year": 1972,
        "plot": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
    },
    {
        "title": "The Dark Knight",
        "movieId": 3,
        "year": 2008,
        "plot": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "movieId": 4,
        "year": 2001,
        "plot": "A meek hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
    },
    {
        "title": "Pulp Fiction",
        "movieId": 5,
        "year": 1994,
        "plot": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
    },
]

ratings = [
    {"user_id": "1", "movie_id": 1, "rating": 5, "timestamp": timestamp},
    {"user_id": "1", "movie_id": 2, "rating": 3, "timestamp": timestamp},
    {"user_id": "2", "movie_id": 1, "rating": 4, "timestamp": timestamp},
    {"user_id": "2", "movie_id": 3, "rating": 4, "timestamp": timestamp},
    {"user_id": "3", "movie_id": 2, "rating": 2, "timestamp": timestamp},
    {"user_id": "3", "movie_id": 4, "rating": 3, "timestamp": timestamp},
    {"user_id": "4", "movie_id": 3, "rating": 4, "timestamp": timestamp},
    {"user_id": "4", "movie_id": 5, "rating": 2, "timestamp": timestamp},
    {"user_id": "5", "movie_id": 4, "rating": 3, "timestamp": timestamp},
    {"user_id": "5", "movie_id": 5, "rating": 4, "timestamp": timestamp},
]

# Inciso D:
# Label User
users2 = [
    {"name": "Alice", "userId": "1"},
    {"name": "Bob", "userId": "2"},
    {"name": "Charlie", "userId": "3"},
]

# Label Movie
movies2 = [
    {
        "title": "The Godfather",
        "tmdbId": 238,
        "releaseDate": "1972-03-14",
        "imdbRating": 9.2,
        "movieId": 100,
        "year": 1972,
        "imdbId": "68646",
        "runtime": 175,
        "countries": ["USA"],
        "imdbVotes": "1588438",
        "url": "https://www.imdb.com/title/tt0068646/",
        "revenue": 245066411,
        "plot": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "budget": 6000000,
        "languages": ["English", "Italian", "Latin"],
    },
    {
        "title": "The Shawshank Redemption",
        "tmdbId": 278,
        "releaseDate": "1994-09-23",
        "imdbRating": 8.7,
        "movieId": 101,
        "year": 1994,
        "imdbId": "1005",
        "runtime": 142,
        "countries": ["USA", "Canada"],
        "imdbVotes": "2324",
        "url": "https://www.imdb.com/23232",
        "revenue": 100,
        "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "budget": 100,
        "languages": ["English", "Spanish"],
    },
]

# Label PersonActorDirector
PAD = [
    {
        "name": "Francis Ford Coppola",
        "tmdbId": 120,
        "born": "1939-04-07",
        "died": "2003-04-16",
        "bornIn": "USA",
        "url": "https://www.imdb.com/name/nm0000338/",
        "imdbId": "0000338",
        "bio": "Director, Producer, Writer",
        "poster": "https://www.imdb.com/name/nm0000338/mediaviewer/rm2517040896",
    },
    {
        "name": "Marlon Brando",
        "tmdbId": 223,
        "born": "1924-04-03",
        "died": "2004-07-01",
        "bornIn": "USA",
        "url": "https://www.imdb.com/name/nm0000008/",
        "imdbId": "0000008",
        "bio": "Actor, Director, Producer",
        "poster": "https://www.imdb.com/name/nm0000008/mediaviewer/rm1246499072",
    },
    {
        "name": "Bobby",
        "tmdbId": 1000,
        "born": "1990-01-01",
        "died": "2010-01-01",
        "bornIn": "USA",
        "url": "https://www.imdb.com/2000",
        "imdbId": "2000",
        "bio": "Actor and director",
        "poster": "https://www.imdb.com/2000/POSTER",
    },
]

# Label PersonActor
PA = [
    {
        "name": "Al Pacino",
        "tmdbId": 113,
        "born": "1940-04-25",
        "died": "2010-01-01",
        "bornIn": "USA",
        "url": "https://www.imdb.com/name/nm0000199/",
        "imdbId": "0000199",
        "bio": "Actor, Producer, Director",
        "poster": "https://www.imdb.com/name/nm0000199/mediaviewer/rm538839296",
    },
    {
        "name": "Johnny",
        "tmdbId": 3000,
        "born": "2000-01-01",
        "died": "2030-01-01",
        "bornIn": "USA",
        "url": "https://www.imdb.com/2300",
        "imdbId": "2300",
        "bio": "Actor",
        "poster": "https://www.imdb.com/2000/POSTER",
    },
]

# Label PersonDirector
PD = [
    {
        "name": "Frank Darabont",
        "tmdbId": 38,
        "born": "1959-01-28",
        "died": "2010-01-01",
        "bornIn": "France",
        "url": "https://www.imdb.com/name/nm0001104/",
        "imdbId": "0001104",
        "bio": "Director, Writer, Producer",
        "poster": "https://www.imdb.com/name/nm0001104/mediaviewer/rm3090468352",
    },
    {
        "name": "Juan",
        "tmdbId": 3100,
        "born": "2001-01-01",
        "died": "2040-01-01",
        "bornIn": "USA",
        "url": "https://www.imdb.com/2350",
        "imdbId": "2350",
        "bio": "Director",
        "poster": "https://www.imdb.com/2000/POSTER",
    },
]

# Label Genre
genre = [{"name": "Drama"}, {"name": "Crime"}, {"name": "Thriller"}]

# Relaciones
inGenre = [
    {"movieId": 100, "genre": "Drama"},
    {"movieId": 100, "genre": "Crime"},
    {"movieId": 100, "genre": "Thriller"},
    {"movieId": 101, "genre": "Drama"},
    {"movieId": 102, "genre": "Comedy"},
    {"movieId": 102, "genre": "Romance"},
]

ratings2 = [
    {"user_id": "1", "movie_id": 100, "rating": 5, "timestamp": timestamp},
    {"user_id": "1", "movie_id": 101, "rating": 4, "timestamp": timestamp},
    {"user_id": "2", "movie_id": 100, "rating": 4, "timestamp": timestamp},
    {"user_id": "2", "movie_id": 101, "rating": 5, "timestamp": timestamp},
    {"user_id": "3", "movie_id": 100, "rating": 3, "timestamp": timestamp},
    {"user_id": "3", "movie_id": 101, "rating": 3, "timestamp": timestamp},
    {"user_id": "3", "movie_id": 102, "rating": 4, "timestamp": timestamp},
]

actedIn = [
    {"movieId": 100, "personId": 223, "role": "Actor"},
    {"movieId": 100, "personId": 113, "role": "Actor"},
    {"movieId": 100, "personId": 3000, "role": "Actor"},
    {"movieId": 100, "personId": 3100, "role": "Actor"},
    {"movieId": 101, "personId": 1, "role": "Actor"},
    {"movieId": 101, "personId": 2888, "role": "Actor"},
    {"movieId": 101, "personId": 223, "role": "Actor"},
    {"movieId": 101, "personId": 3100, "role": "Actor"},
    {"movieId": 102, "personId": 223, "role": "Actor"},
    {"movieId": 102, "personId": 113, "role": "Actor"},
    {"movieId": 102, "personId": 1, "role": "Actor"},
    {"movieId": 101, "personId": 1000, "role": "Actor"},
    {"movieId": 100, "personId": 120, "role": "Director"},
]


DIRECTED = [
    {"movieId": 100, "personId": 120, "role": "Director"},
    {"movieId": 102, "personId": 3100, "role": "Director"},
]

DIRECTED2 = [
    {"movieId": 101, "personId": 38, "role": "Director"},
    {"movieId": 102, "personId": 223, "role": "Director"},
]


ACTED_IN = [
    {"movieId": 100, "personId": 1, "role": "Actor"},
    {"movieId": 102, "personId": 3000, "role": "Actor"},
]
