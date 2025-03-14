import pytest

from autogen_movie_ticket.tools.tools import get_movie, is_movie, verify_ticket_count


def test_get_movie():
    movie = get_movie("godfather")
    assert movie
    assert movie.movie_name == "The Godfather"

    movie = get_movie("godfather 2")
    assert not movie


def test_is_movie():
    assert is_movie("godfather")
    assert not is_movie("godfather 2")


def test_verify_ticket_count():
    assert verify_ticket_count("godfather 2", 5) == 5  # movie not found
    assert verify_ticket_count("godfather", 5) == 5

    with pytest.raises(ValueError, match="Ticket count should be between 1 and 9."):
        verify_ticket_count("godfather", 20)

    with pytest.raises(ValueError, match="Ticket count exceeds the available tickets."):
        verify_ticket_count("dark knight", 3)
