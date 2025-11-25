from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Screen(Base):
    __tablename__ = "signage_screens"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    branch_id = Column(Integer, ForeignKey("branches.id"))
    branch = relationship("Branch")

class SignageContent(Base):
    __tablename__ = "signage_content"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    content_data = Column(JSON) # e.g., {"type": "image", "url": "..."}

class Playlist(Base):
    __tablename__ = "signage_playlists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    schedule = Column(JSON) # e.g., {"days": ["mon", "tue"], "time": "09:00-17:00"}
