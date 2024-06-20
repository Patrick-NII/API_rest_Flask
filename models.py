from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

db = SQLAlchemy(model_class=Base)

class Product(Base):
    
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=False, nullable=False)
    description = Column(String, index=False, nullable=False)
    price = Column(Float, nullable=False)