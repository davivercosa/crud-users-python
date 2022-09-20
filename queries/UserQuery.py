from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, Integer

Base = declarative_base()

class User(Base):
    
    __tablename__ = "users"

    name = Column(String(100))
    email = Column(String(255), primary_key = True)
    age = Column(Integer)
    gender = Column(String(100))

    def __repr__(self):
       return f"User(name={self.name!r}, email={self.email!r}, age={self.age!r}, gender={self.gender!r})"
