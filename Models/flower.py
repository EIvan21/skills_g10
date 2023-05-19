from Config.database import Base 
from sqlalchemy import Column, Integer, Float

class Flower(Base):
    __tablename__ = "Flowers"
    id =  Column(Integer, primary_key=True)
    sepalLength = Column(Float)
    sepalWidth = Column(Float)
    petalLength = Column(Float)
    petalWidth = Column(Float)
    