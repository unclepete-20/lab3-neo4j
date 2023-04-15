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


# All functions that will create Nodes and Relationship objects between them
def create_user(tx, name, userId):  
        result = tx.run(
            "MERGE (:User {name: $name, userId: $userId})",  
            name=name, userId=userId  
        )
        summary = result.consume()
        return summary
    
def create_movie(tx, title, movieId, year, plot):  
    result = tx.run(
        "MERGE (:Movie {title: $title, movieId: $movieId, year: $year, plot: $plot})",  
        title=title, movieId=movieId, year=year, plot=plot  
    )
    summary = result.consume()
    return summary

def create_rated_relationship(tx, user_id, movie_id, rating, timestamp):
    query = '''
    MATCH (u:User), (m:Movie)
    WHERE u.userId = $user_id AND m.movieId = $movie_id
    MERGE (u)-[r:Rated {rating: $rating, timestamp: $timestamp}]->(m)
    RETURN type(r), r.rating, r.timestamp
    '''
    result = tx.run(query, user_id=user_id, movie_id=movie_id, rating=rating, timestamp=timestamp)
    summary = result.consume()
    
    return summary

with GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)) as driver: 
    driver.verify_connectivity() 
    
    
