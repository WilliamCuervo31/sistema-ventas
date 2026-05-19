from sqlalchemy import *
from config.db_connection import Base
from datetime import *

class Venta(Base):
    __tablename__ = "venta"

    venta_id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    usuario_id = Column(Integer, ForeignKey("usuario.usuario_id"))
    cliente_id = Column(Integer, ForeignKey("cliente.cliente_id"))
    total = Column(Numeric(12,2))