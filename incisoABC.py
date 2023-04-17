# create_user method creates a new user node in a Neo4j database
def create_user(tx, users):
    query = "MERGE (u:User {name: $users.name, userId: $users.userId})"
    tx.run(query, users=users)


# create_movie method creates a new movie node in a Neo4j database
def create_movie(tx, movies):
    query = "MERGE (m:Movie {title: $movies.title, movieId: $movies.movieId, year: $movies.year, plot: $movies.plot})"
    tx.run(query, movies=movies)


# create_rated_relationship creates a RATED relationship between user and movie nodes in a Neo4j database
def create_rated_relationship(tx, relationship):
    query = """
    MATCH (u:User), (m:Movie)
    WHERE u.id = $relationship['user_id'] AND m.movieId = $relationship['movie_id']
    MERGE (u)-[r:RATED {rating: $relationship['rating'], timestamp: $relationship['timestamp']}]->(m)
    RETURN type(r)
    """
    tx.run(query, relationship=relationship)


# find_user_and_movie_with_relationships method finds a user and its movie relationships in a Neo4j database
def find_user_and_movie_with_relationships(tx, user_id):
    query = """
    MATCH (u:User {userId: $user_id})-[r]->(m:Movie)
    RETURN u, r, m
    """
    result = tx.run(query, user_id=user_id)
    return result.data()
