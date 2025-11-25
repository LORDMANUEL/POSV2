from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from core.database import Base
import datetime

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    permissions = Column(JSON, nullable=False) # e.g., {"pos": ["create_sale"], "inventory": ["read"]}

    users = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    role_id = Column(Integer, ForeignKey("roles.id"))
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=True)

    role = relationship("Role", back_populates="users")
    branch = relationship("Branch", back_populates="users")

class Branch(Base):
    __tablename__ = "branches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    location = Column(String)
    settings = Column(JSON, nullable=True) # e.g., {"theme": "dark", "printer_ip": "..."}

    users = relationship("User", back_populates="branch")

class SystemSettings(Base):
    __tablename__ = "system_settings"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True, nullable=False)
    config = Column(JSON, nullable=False)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    details = Column(JSON, nullable=True)

    user = relationship("User")
