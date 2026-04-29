from sqlalchemy import *
from config.db_connection import Base

class Usuario(Base):
    __tablename__ = "usuario"

    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    email = Column(String(150), unique=True)
    contrasena = Column(String(225))
    estado = Column(Boolean)
    rol_id = Column(Integer, ForeignKey("rol.rol_id"))