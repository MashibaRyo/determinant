from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class SHotels(BaseModel):
    address: str
    name: str
    stars: int
class SHotelAtr:
    def __init__(
            self,
            location: str,
            date_in: date,
            date_out: date,
            stars: Optional[int] = Query(None, ge=1, le=5),
            has_spa: Optional[bool] = None
            ):
            self.location = location
            self.date_in = date_in
            self.date_out = date_out
            self.stars = stars
            self.has_spa = has_spa

@app.get("/hotels", response_model=SHotels)
def get_hotels(search_args: SHotelAtr = Depends()):
    # hotels = [
    #     {
    #         "address": "Ул. Примерная, 123",
    #         "name": "gdjhdj",
    #         "stars": 5,
    #     }
    # ]
    return search_args

# class SBooking(BaseModel):
#     room_id: int
#     date_in: date
#     date_out: date
#
# @app.post("/booking")
# def add_booking(Booking: SBooking):
#     pass
