from sqlalchemy import Column, Integer, String
from config.db_connection import Base

class Rol(Base):
    __tablename__ = "rol"

    rol_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    descripcion = Column(String(150))