from pydantic import BaseModel

class AddToPayload(BaseModel):
    media_type: str
    media_id: int

class AddToFavoritesPayload(AddToPayload):
    favorite: bool

class AddToWatchlistPayload(AddToPayload):
    watchlist: bool
