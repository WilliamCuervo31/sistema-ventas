from sqlalchemy import *
from config.db_connection import Base
from datetime import *

class Producto(Base):
    __tablename__ = "producto"

    producto_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120))
    descripcion = Column(Text)
    estado = Column(Boolean)
    fecha_creacion = Column(DateTime, default=lambda: datetime.now(timezone.utc))