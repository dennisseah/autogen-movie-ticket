from autogen_movie_ticket.models.movie import Movie


def test_movie_init():
    movie = Movie(
        movie_name="The Matrix",
        num_tickets=2,
        available_dates=["02/25"],
        available_times=["11:00 AM", "2:30 PM", "4:00 PM", "8:00 PM"],
    )
    assert movie.movie_name == "The Matrix"
    assert movie.num_tickets == 2
    assert movie.available_dates == ["02/25"]
    assert movie.available_times == ["11:00 AM", "2:30 PM", "4:00 PM", "8:00 PM"]
