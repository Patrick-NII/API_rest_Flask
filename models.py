from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

db = SQLAlchemy(model_class=base)

class product(base):
    id = Column(Integer, primary_key=True, index=True)