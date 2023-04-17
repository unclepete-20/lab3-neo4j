# create_user2 method creates a new user node in a Neo4j database
def create_user2(tx, user):
    query = "MERGE (u:User {name: $name, userId: $userId})"
    tx.run(query, name=user["name"], userId=user["userId"])


# create_movie method creates a new movie node in a Neo4j database
def create_movie2(tx, movie):
    query = """
        MERGE (m:Movie {title: $title, released: $released, tmdbId: $tmdbId, imdbRating: $imdbRating, 
                        movieId: $movieId, year: $year, imdbId: $imdbId, runtime: $runtime, 
                        countries: $countries, imdbVotes: $imdbVotes, url: $url, revenue: $revenue, 
                        plot: $plot, poster: $poster, budget: $budget, languages: $languages})
    """
    tx.run(
        query,
        title=movie["title"],
        released=movie["released"],
        tmdbId=movie["tmdbId"],
        imdbRating=movie["imdbRating"],
        movieId=movie["movieId"],
        year=movie["year"],
        imdbId=movie["imdbId"],
        runtime=movie["runtime"],
        countries=movie["countries"],
        imdbVotes=movie["imdbVotes"],
        url=movie["url"],
        revenue=movie["revenue"],
        plot=movie["plot"],
        poster=movie["poster"],
        budget=movie["budget"],
        languages=movie["languages"],
    )


# create_in_genre_relationship creates an IN_GENRE relationship between a movie and a genre node in a Neo4j database
def create_in_genre_relationship(tx, relationship):
    query = """
    MATCH (m:Movie {movieId: $movieId}), (g:Genre {name: $genre})
    MERGE (m)-[r:IN_GENRE]->(g)
    RETURN type(r)
    """
    tx.run(query, movieId=relationship["movieId"], genre=relationship["genre"])


# create_person_actor_relationship creates an ACTED_IN relationship between a person actor and a movie node in a Neo4j database
def create_person_actor_relationship(tx, relationship):
    query = """
    MATCH (m:Movie {movieId: $movieId}), (pa:PersonActor {tmdbId: $personId})
    MERGE (pa)-[r:ACTED_IN {role: $role}]->(m)
    RETURN type(r)
    """
    tx.run(
        query,
        movieId=relationship["movieId"],
        personId=relationship["personId"],
        role=relationship["role"],
    )


def create_person_director_relationship(tx, relationship):
    query = (
        "MATCH (p:Person {id: $personId}), (m:Movie {id: $movieId}) "
        "CREATE (p)-[:DIRECTED]->(m)"
    )
    tx.run(query, movieId=relationship["movieId"], personId=relationship["personId"])


# create_acted_in_relationship creates an ACTED_IN relationship between person and movie nodes in a Neo4j database
def create_acted_in_relationship(tx, relationship):
    query = """
    MATCH (p:PersonActor {tmdbId: $personId}), (m:Movie {movieId: $movieId})
    MERGE (p)-[r:ACTED_IN {role: $role}]->(m)
    RETURN type(r)
    """
    tx.run(
        query,
        personId=relationship["personId"],
        movieId=relationship["movieId"],
        role=relationship["role"],
    )


def create_rating(tx, relationship):
    query = """
    MATCH (u:User {userId: $user_id}), (m:Movie {movieId: $movie_id})
    MERGE (u)-[r:RATED]->(m)
    SET r.rating = $rating, r.timestamp = $timestamp
    RETURN type(r)
"""
    tx.run(
        query,
        user_id=relationship["user_id"],
        movie_id=relationship["movie_id"],
        rating=relationship["rating"],
        timestamp=relationship["timestamp"],
    )


def create_directed_relationship(tx, relationship):
    query = """
    MATCH (p:PersonDirector {tmdbId: $personId}), (m:Movie {movieId: $movieId})
    MERGE (p)-[r:DIRECTED {role: $role}]->(m)
    RETURN type(r)
    """
    tx.run(
        query,
        personId=relationship["personId"],
        movieId=relationship["movieId"],
        role=relationship["role"],
    )


# create_genre method creates a new genre node in a Neo4j database
def create_genre(tx, genre):
    query = "MERGE (g:Genre {name: $genre['name']})"
    tx.run(query, genre=genre)


# create_person_actor method creates a new person actor node in a Neo4j database
def create_person_actor(tx, person_actor):
    query = """
    MERGE (pa:PersonActor {name: $person_actor['name'], tmdbId: $person_actor['tmdbId'], 
                            born: $person_actor['born'], died: $person_actor['died'], bornIn: $person_actor['bornIn'], 
                            url: $person_actor['url'], imdbId: $person_actor['imdbId'], bio: $person_actor['bio'], 
                            poster: $person_actor['poster']})
    SET pa.roles = $person_actor['roles']
    """
    tx.run(query, person_actor=person_actor)


# create_person_director method creates a new person director node in a Neo4j database
def create_person_director(tx, person_director):
    query = """
    MERGE (pd:PersonDirector {name: $person_director['name'], tmdbId: $person_director['tmdbId'], 
                               born: $person_director['born'], died: $person_director['died'], bornIn: $person_director['bornIn'], 
                               url: $person_director['url'], imdbId: $person_director['imdbId'], bio: $person_director['bio'], 
                               poster: $person_director['poster']})
    SET pd.directed = $person_director['directed']
    """
    tx.run(query, person_director=person_director)


# create_person_actor_director method creates a new person actor director node in a Neo4j database
def create_person_actor_director(tx, person_actor_director):
    query = """
    MERGE (pad:PersonActorDirector {name: $person_actor_director['name'], tmdbId: $person_actor_director['tmdbId'], 
                               born: $person_actor_director['born'], died: $person_actor_director['died'], bornIn: $person_actor_director['bornIn'], 
                               url: $person_actor_director['url'], imdbId: $person_actor_director['imdbId'], bio: $person_actor_director['bio'], 
                               poster: $person_actor_director['poster']})
    SET pad.acted_in = $person_actor_director['acted_in'], pad.directed = $person_actor_director['directed']
    """
    tx.run(query, person_actor_director=person_actor_director)


# create_acted_in_relationship method creates an ACTED_IN relationship between a person actor director and a movie node in a Neo4j database
def create_acted_in_relationshipPAD(tx, relationship):
    query = """
    MATCH (p:PersonActorDirector {tmdbId: $personId}), (m:Movie {movieId: $movieId})
    MERGE (p)-[r:ACTED_IN {role: $role}]->(m)
    RETURN type(r)
    """
    tx.run(
        query,
        personId=relationship["personId"],
        movieId=relationship["movieId"],
        role=relationship["role"],
    )


def create_directed_relationshipPAD(tx, relationship):
    query = """
    MATCH (p:PersonActorDirector {tmdbId: $personId}), (m:Movie {movieId: $movieId})
    MERGE (p)-[r:DIRECTED {role: $role}]->(m)
    RETURN type(r)
    """
    tx.run(
        query,
        personId=relationship["personId"],
        movieId=relationship["movieId"],
        role=relationship["role"],
    )
