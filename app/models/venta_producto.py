from sqlalchemy import *
from config.db_connection import Base

class VentaProducto(Base):
    __tablename__ = "venta_producto"

    venta_producto_id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("venta.venta_id"))
    referencia_id = Column(Integer, ForeignKey("referencia.referencia_id"))
    cantidad = Column(Integer)
    precio_unitario = Column(Numeric(10,2))