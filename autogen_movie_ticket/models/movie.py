from pydantic import BaseModel


class Movie(BaseModel):
    movie_name: str
    num_tickets: int
    available_dates: list[str]
    available_times: list[str]
    theaters: list[str] = ["AMC", "Regal", "Cinemark"]
