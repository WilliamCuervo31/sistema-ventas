from sqlalchemy import *
from config.db_connection import Base

class Referencia(Base):
    __tablename__ = "referencia"

    referencia_id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("producto.producto_id"))
    talla = Column(String(10))
    cantidad = Column(Integer)
    precio_compra = Column(Numeric(10,2))
    precio_venta = Column(Numeric(10,2))
    proveedor_id = Column(Integer, ForeignKey("proveedor.proveedor_id"))