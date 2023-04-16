# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188), Alejadro Gomez (20347) y Rodrigo Barrera (20807)
@Version :   1.0
@Desc    :   Creacion y carga de datos a Neo4j
'''


from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Loads the environment variables
load_dotenv()

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

# ISO 8601 formatted timestamp
timestamp = 34901204396

users = [
    {"name": "Alice", "userId": "1"},
    {"name": "Bob", "userId": "2"},
    {"name": "Peter", "userId": "3"},
    {"name": "Anna", "userId": "4"},
    {"name": "Jake", "userId": "5"}
]

movies = [
    {
        "title": "The Shawshank Redemption",
        "movieId": 1,
        "year": 1994,
        "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    },
    {
        "title": "The Godfather",
        "movieId": 2,
        "year": 1972,
        "plot": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
    },
    {
        "title": "The Dark Knight",
        "movieId": 3,
        "year": 2008,
        "plot": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "movieId": 4,
        "year": 2001,
        "plot": "A meek hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron."
    },
    {
        "title": "Pulp Fiction",
        "movieId": 5,
        "year": 1994,
        "plot": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."
    }
]

ratings = [
    {
        "user_id": "1",
        "movie_id": 1,
        "rating": 5,
        "timestamp": timestamp
    },
    {
        "user_id": "1",
        "movie_id": 2,
        "rating": 3,
        "timestamp": timestamp
    },
    {
        "user_id": "2",
        "movie_id": 1,
        "rating": 4,
        "timestamp": timestamp
    },
    {
        "user_id": "2",
        "movie_id": 3,
        "rating": 4,
        "timestamp": timestamp
    },
    {
        "user_id": "3",
        "movie_id": 2,
        "rating": 2,
        "timestamp": timestamp
    },
    {
        "user_id": "3",
        "movie_id": 4,
        "rating": 3,
        "timestamp": timestamp
    },
    {
        "user_id": "4",
        "movie_id": 3,
        "rating": 4,
        "timestamp": timestamp
    },
    {
        "user_id": "4",
        "movie_id": 5,
        "rating": 2,
        "timestamp": timestamp
    },
    {
        "user_id": "5",
        "movie_id": 4,
        "rating": 3,
        "timestamp": timestamp
    },
    {
        "user_id": "5",
        "movie_id": 5,
        "rating": 4,
        "timestamp": timestamp
    }
]



# create_user method creates a new user node in a Neo4j database
def create_user(tx, users):
    query = "MERGE (u:User {name: $users.name, userId: $users.userId})"
    tx.run(query, users=users)

# create_movie method creates a new movie node in a Neo4j database
def create_movie(tx, movies):  
    query = "MERGE (m:Movie {title: $movies.title, movieId: $movies.movieId, year: $movies.year, plot: $movies.plot})"
    tx.run(query, movies=movies)

# create_rated_relationship creates a RATED relationship between user and movie nodes in a Neo4j database
def create_rated_relationship(tx, ratings):
    query = '''
    MATCH (u:User), (m:Movie)
    WHERE u.userId = $ratings.user_id AND m.movieId = $ratings.movie_id
    MERGE (u)-[r:RATED {rating: $ratings.rating, timestamp: $ratings.timestamp}]->(m)
    RETURN type(r), r.rating, r.timestamp
    '''
    tx.run(query, ratings=ratings)

# find_user_and_movie_with_relationships method finds a user and its movie relationships in a Neo4j database
def find_user_and_movie_with_relationships(tx, user_id):
    query = '''
    MATCH (u:User {userId: $user_id})-[r]->(m:Movie)
    RETURN u, r, m
    '''
    result = tx.run(query, user_id=user_id)
    return result.data()

# This part of the code creates the connection to the Neo4j database
with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)) as driver: 
    with driver.session(database="neo4j") as session:
        

        # User nodes are inserted into the database
        for user in users:
            session.execute_write(create_user, user)

        # User nodes are inserted into the database
        for movie in movies:
            session.execute_write(create_movie, movie)
        
        # RATED relationships are created between User and Movie nodes
        for rating in ratings:
            session.execute_write(create_rated_relationship, rating)
        
        # Query to get the user relationships
        user_id = "1"
        user_movie_relationships = session.execute_read(find_user_and_movie_with_relationships, user_id)
        print("User and Movie Relationships:")
        for relationship in user_movie_relationships:
            print(relationship)
        
        # Session and driver are closed in order to release any resources still held by them.
        session.close()
        driver.close()
