from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from app.db.database import Base
import datetime

event_attendees = Table('event_attendees', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_events = relationship("Event", back_populates="organizer")
    attending_events = relationship("Event", secondary=event_attendees, back_populates="attendes")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    events = relationship("Event", back_populates="category")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String)
    start_date_time = Column(DateTime)
    end_date_time = Column(DateTime)
    location = Column(String)
    organizer_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    organizer = relationship("User", back_populates="created_events")
    category = relationship("Category", back_populates="events")
    attendes = relationship("User", secondary=event_attendees, back_populates="attending_events")
