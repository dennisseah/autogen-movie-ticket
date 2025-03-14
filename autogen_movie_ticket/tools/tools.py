import logging

from autogen_movie_ticket.hosting import container
from autogen_movie_ticket.models.movie import Movie

logger = container[logging.Logger]

movies = [
    Movie(movie_name="The Shawshank Redemption", num_tickets=10),
    Movie(movie_name="The Godfather", num_tickets=20),
    Movie(movie_name="The Dark Knight", num_tickets=10),
    Movie(movie_name="The Lord of the Rings: The Return of the King", num_tickets=10),
    Movie(movie_name="Pulp Fiction", num_tickets=10),
    Movie(movie_name="Schindler's List", num_tickets=10),
]


def get_movie(name: str) -> Movie | None:
    """Get the movie object for the given movie name.

    :param name: The movie name.
    :return: The movie object for the given movie name.
    return None if the movie name is not found.
    """
    for movie in movies:
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


def verify_ticket_count(movie_name: str | None, ticket_count: str) -> int | None:
    """Verify if the given ticket count is valid.
    if yes, return the exact ticket count.

    :param
    ticket_count: The ticket count to verify.
    :return: The exact ticket count if the given ticket count is valid.
    return None if the given ticket count is invalid.
    """
    try:
        count = int(ticket_count)
        if count > 0 and count < 10:
            if movie_name:
                movie = get_movie(movie_name)
                if movie:
                    if count > movie.num_tickets:
                        return count
                    raise ValueError("Ticket count exceeds the available tickets.")
            return count

    except ValueError:
        raise ValueError("Invalid ticket count.")
