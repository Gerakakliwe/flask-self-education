# 1 - imports
from datetime import date
from actor import Actor
from base import Session

from contact_details import ContactDetails
from movie import Movie

# 2 - extract a session
session = Session()

# 3 - extract all movies
movies = session.query(Movie).all()

# 4 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

# 5 - get movies after 15-01-01
movies_after_2015 = session.query(Movie) \
    .filter(Movie.release_date > date(2015, 1, 1)) \
    .all()

print('### Recent movies (2015 and after):')
for movie in movies_after_2015:
    print(f'{movie.title} was released after 2015')
print('')

# 6 - movies that Dwayne Johnson participated
movies_w_dwayne = session.query(Movie) \
    .join(Actor, Movie.actors) \
    .filter(Actor.name == "Dwayne Johnson") \
    .all()

print('### Movies with Rock:')
for movie in movies_w_dwayne:
    print(f'The Rock starred in {movie.title}')
print('')

# 7 - get actors that have house in Glendale
glendale_stars = session.query(Actor) \
    .join(ContactDetails) \
    .filter(ContactDetails.address.ilike('%glendale%')) \
    .all()

print('### Actors that live in Glendale:')
for actor in glendale_stars:
    print(f'{actor.name} has a house in Glendale')
print('')