from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    is_active = Column(Boolean, default=True)

    role = relationship('Role', back_populates='users')

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship('User', order_by=User.id, back_populates='role')

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String(200), nullable=False)
    timestamp = Column(String(20), default='2026-02-17 19:43:50')

    user = relationship('User')

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    session_token = Column(String(256), unique=True, nullable=False)
    expiration = Column(String(20), nullable=False)

    user = relationship('User')
