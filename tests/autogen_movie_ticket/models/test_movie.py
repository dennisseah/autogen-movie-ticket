from autogen_movie_ticket.models.movie import Movie


def test_movie_init():
    movie = Movie(movie_name="The Matrix", num_tickets=2)
    assert movie.movie_name == "The Matrix"
    assert movie.num_tickets == 2
