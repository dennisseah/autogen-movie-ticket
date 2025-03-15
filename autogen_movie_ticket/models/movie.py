from pydantic import BaseModel


class Movie(BaseModel):
    movie_name: str
    num_tickets: int
    available_date: list[str]
