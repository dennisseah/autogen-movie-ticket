from typing import Literal

from pydantic import BaseModel

MOVIE_TYPE = Literal["2D", "3D", "Rated R", "PG-13", "PG", "G"]


class MovieDate(BaseModel):
    type: MOVIE_TYPE
    date: str


class Movie(BaseModel):
    movie_name: str
    num_tickets: int
    available_dates: list[MovieDate]
