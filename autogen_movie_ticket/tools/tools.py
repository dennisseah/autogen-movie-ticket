import logging

from autogen_movie_ticket.hosting import container
from autogen_movie_ticket.models.movie import Movie, MovieDate

logger = container[logging.Logger]

movies = [
    Movie(
        movie_name="The Shawshank Redemption",
        num_tickets=10,
        available_dates=[
            MovieDate(type="2D", date="03/10"),
            MovieDate(type="2D", date="03/11"),
            MovieDate(type="2D", date="03/12"),
            MovieDate(type="2D", date="03/13"),
            MovieDate(type="2D", date="03/14"),
            MovieDate(type="3D", date="03/11"),
            MovieDate(type="3D", date="03/12"),
            MovieDate(type="PG-13", date="03/10"),
            MovieDate(type="PG-13", date="03/11"),
            MovieDate(type="PG-13", date="03/12"),
            MovieDate(type="PG-13", date="03/13"),
            MovieDate(type="PG-13", date="03/14"),
        ],
    ),
    Movie(
        movie_name="The Godfather",
        num_tickets=20,
        available_dates=[
            MovieDate(type="2D", date="03/10"),
            MovieDate(type="2D", date="03/11"),
            MovieDate(type="2D", date="03/12"),
            MovieDate(type="2D", date="03/13"),
            MovieDate(type="2D", date="03/14"),
            MovieDate(type="3D", date="03/11"),
            MovieDate(type="3D", date="03/12"),
            MovieDate(type="PG-13", date="03/10"),
            MovieDate(type="PG-13", date="03/11"),
            MovieDate(type="PG-13", date="03/12"),
            MovieDate(type="PG-13", date="03/13"),
            MovieDate(type="PG-13", date="03/14"),
        ],
    ),
    Movie(
        movie_name="The Dark Knight",
        num_tickets=1,
        available_dates=[
            MovieDate(type="2D", date="03/10"),
            MovieDate(type="2D", date="03/11"),
            MovieDate(type="2D", date="03/12"),
            MovieDate(type="2D", date="03/13"),
            MovieDate(type="2D", date="03/14"),
            MovieDate(type="3D", date="03/11"),
            MovieDate(type="3D", date="03/12"),
            MovieDate(type="Rated R", date="03/12"),
            MovieDate(type="PG-13", date="03/10"),
            MovieDate(type="PG-13", date="03/11"),
            MovieDate(type="PG-13", date="03/12"),
            MovieDate(type="PG-13", date="03/13"),
            MovieDate(type="PG-13", date="03/14"),
        ],
    ),
    Movie(
        movie_name="The Lord of the Rings: The Return of the King",
        num_tickets=10,
        available_dates=[
            MovieDate(type="2D", date="03/13"),
            MovieDate(type="2D", date="03/14"),
            MovieDate(type="3D", date="03/11"),
            MovieDate(type="3D", date="03/12"),
            MovieDate(type="Rated R", date="03/12"),
            MovieDate(type="PG-13", date="03/12"),
            MovieDate(type="PG-13", date="03/13"),
            MovieDate(type="PG-13", date="03/14"),
        ],
    ),
    Movie(
        movie_name="Pulp Fiction",
        num_tickets=10,
        available_dates=[
            MovieDate(type="2D", date="03/13"),
            MovieDate(type="2D", date="03/14"),
            MovieDate(type="3D", date="03/11"),
            MovieDate(type="3D", date="03/12"),
            MovieDate(type="Rated R", date="03/12"),
            MovieDate(type="PG-13", date="03/12"),
            MovieDate(type="PG-13", date="03/13"),
            MovieDate(type="PG-13", date="03/14"),
        ],
    ),
    Movie(
        movie_name="Schindler's List",
        num_tickets=10,
        available_dates=[
            MovieDate(type="2D", date="03/13"),
            MovieDate(type="2D", date="03/14"),
            MovieDate(type="3D", date="03/11"),
            MovieDate(type="3D", date="03/12"),
            MovieDate(type="Rated R", date="03/12"),
            MovieDate(type="PG-13", date="03/12"),
            MovieDate(type="PG-13", date="03/13"),
            MovieDate(type="PG-13", date="03/14"),
        ],
    ),
]


def get_movie(name: str) -> Movie | None:
    """Get the movie object for the given movie name.

    :param name: The movie name.
    :return: The movie object for the given movie name.
    return None if the movie name is not found.
    """
    for movie in movies:
        # fuzzy matching can be implemented here
        if movie.movie_name.lower().find(name.lower()) != -1:
            return movie
    return None


def is_movie(name: str) -> str | None:
    """Verify if the given name is a movie.
    if yes, return the exact movie name.

    :param name: The name to verify.
    :return: The exact movie name if the given name is a movie.
    return None if the given name is not a movie.
    """
    movie = get_movie(name)
    return movie.movie_name if movie else None


def verify_ticket_count(movie_name: str | None, ticket_count: int) -> int | None:
    """Verify if the given ticket count is valid.
    if yes, return the exact ticket count.

    :param
    ticket_count: The ticket count to verify.
    :return: The exact ticket count if the given ticket count is valid.
    return None if the given ticket count is invalid.
    """
    if ticket_count > 0 and ticket_count < 10:
        if movie_name:
            movie = get_movie(movie_name)
            if movie:
                if ticket_count <= movie.num_tickets:
                    return ticket_count
                raise ValueError("Ticket count exceeds the available tickets.")

        # return ticket count if movie not found
        # agent will come back with the movie name
        return ticket_count

    raise ValueError("Ticket count should be between 1 and 9.")


def available_movie_types(movie_name: str) -> str | None:
    """Return the available movie types for the given movie name.
    Movie types such as 2D, 3D, PG-13, etc.

    :param movie_name: The movie name.
    :return: The available movie types for the given movie name.
    """
    movie = get_movie(movie_name)
    if movie:
        types = list({date.type for date in movie.available_dates})
        types.sort()
        return ", ".join(types)
    return None


def available_dates(movie_name: str, movie_type: str) -> str | None:
    """Return the available date for the given movie name.

    :param movie_name: The movie name.
    :param movie_type: The movie type.
    :return: The available dates for the given movie and type.
    """
    movie = get_movie(movie_name)
    if movie:
        dates = [date.date for date in movie.available_dates if date.type == movie_type]
        dates.sort()
        return ", ".join(dates)
    return None
