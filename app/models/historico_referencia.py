from sqlalchemy import *
from config.db_connection import Base
from datetime import *

class HistoricoReferencia(Base):
    __tablename__ = "historico_referencia"

    historico_referencia_id = Column(Integer, primary_key=True, index=True)
    referencia_id = Column(Integer, ForeignKey("referencia.referencia_id"))
    precio_anterior = Column(Numeric(10,2))
    precio_nuevo = Column(Numeric(10,2))
    cantidad_anterior = Column(Integer)
    cantidad_nueva = Column(Integer)
    #lambda se ejecuta cada vez que se inserta un regsitro
    fecha = Column(DateTime, default=lambda: datetime.now(timezone.utc))