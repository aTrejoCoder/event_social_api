from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str



class UserCreate(UserBase):
    password: str  



class User(UserBase):
    created_events: List[int] = []
    attending_events: List[int] = []

    class Config:
        orm_mode = True



class CategoryBase(BaseModel):
    name: str



class CategoryCreate(CategoryBase):
    pass



class Category(CategoryBase):
    id: int
    events: List[int] = []

    class Config:
        orm_mode = True



class EventBase(BaseModel):
    title: str
    description: str
    start_date_time: datetime
    end_date_time: datetime
    location: str
    organizer_id: int
    category_id: int



class EventCreate(EventBase):
    pass



class Event(EventBase):
    attendees: List[int] = []

    class Config:
        orm_mode = True
