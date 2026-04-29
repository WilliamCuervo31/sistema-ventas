from sqlalchemy import Column, Integer, String
from config.db_connection import Base

class Proveedor(Base):
    __tablename__ = "proveedor"

    proveedor_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120))
    telefono = Column(String(20))
    email = Column(String(150))