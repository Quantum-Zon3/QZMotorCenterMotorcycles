from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from src.database import Base

class Motorcycle(Base):
    __tablename__ = "motorcycles"

    placa = Column(String(6), primary_key=True, nullable=False)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    precio = Column(DECIMAL(10,2), nullable=False)
    cilindraje = Column(Integer)
    image_url = Column(String(255))
    creada_el = Column(DateTime)

    def to_dict(self):
        return {
            "placa": self.placa,
            "marca": self.marca,
            "modelo": self.modelo,
            "year": self.year,
            "precio": float(self.precio),
            "cilindraje": self.cilindraje,
            "image_url": self.image_url,
            "creada_el": str(self.creada_el)
        }