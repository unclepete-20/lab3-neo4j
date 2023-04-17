# -*-coding:utf-8 -*-
"""
@File    :   main.py
@Date    :   2022/09/21
@Author  :   Pedro Arriola (20188), Alejadro Gomez (20347) y Rodrigo Barrera (20807)
@Version :   1.0
@Desc    :   Creacion y carga de datos a Neo4j
"""


from neo4j import GraphDatabase
import os
from dotenv import load_dotenv
from Data import *
from incisoABC import *
from incisoD import *

# Loads the environment variables
load_dotenv()

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


# This part of the code creates the connection to the Neo4j database
def InsertData():
    # Connection to the Neo4j database
    with GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    ) as driver:
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
            user_movie_relationships = session.execute_read(
                find_user_and_movie_with_relationships, user_id
            )
            print("User and Movie Relationships:")
            for relationship in user_movie_relationships:
                print(relationship)

            # Session and driver are closed in order to release any resources still held by them.
            session.close()
            driver.close()


# Inciso D:
def IncisoD():
    with GraphDatabase.driver(
        NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
    ) as driver:
        with driver.session(database="neo4j") as session:
            # Create users
            for user in users2:
                session.execute_write(create_user2, user)

            # Create movies
            for movie in movies2:
                session.execute_write(create_movie2, movie)

            # Create PAD
            for pad in PAD:
                session.execute_write(create_person_actor_director, pad)

            # Create PA
            for pa in PA:
                session.execute_write(create_person_actor, pa)

            # Create PD
            for pd in PD:
                session.execute_write(create_person_director, pd)

            # Create genres
            for g in genre:
                session.execute_write(create_genre, g)

            # Create relationships
            for relationship in inGenre:
                session.execute_write(create_in_genre_relationship, relationship)

            for relationship in actedIn:
                session.execute_write(create_person_actor_relationship, relationship)

            for relationship in DIRECTED:
                session.execute_write(create_directed_relationship, relationship)

            for relationship in ACTED_IN:
                session.execute_write(create_acted_in_relationship, relationship)

            for relationship in DIRECTED2:
                session.execute_write(create_directed_relationshipPAD, relationship)

            for relationship in ACTED_IN:
                session.execute_write(create_acted_in_relationshipPAD, relationship)

            # Create ratings
            for rating in ratings2:
                session.execute_write(create_rating, rating)
        session.close()
        driver.close()


IncisoD()
