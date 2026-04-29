from sqlalchemy import *
from config.db_connection import Base
from datetime import *

class AuditoriaProducto(Base):
    __tablename__ = "auditoria_producto"

    auditoria_producto_id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("producto.producto_id"))
    accion = Column(String(50))
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    usuario = Column(String(100))
    detalle = Column(Text)