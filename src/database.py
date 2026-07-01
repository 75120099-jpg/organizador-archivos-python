from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
import datetime


Base = declarative_base()


class HistorialMovimiento(Base):
    __tablename__ = 'historial_archivos'

    id = Column(Integer, primary_key=True)
    nombre_archivo = Column(String)
    categoria_destino = Column(String)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)


def guardar_registro(session, nombre, categoria):
    """Guarda un registro en la base de datos."""
    Base.metadata.create_all(session.get_bind())

    nuevo_registro = (
        HistorialMovimiento(nombre_archivo=nombre, categoria_destino=categoria)
    )
    session.add(nuevo_registro)
    session.commit()


def obtener_registros(session):
    """Obtiene todos los registros."""
    return session.query(HistorialMovimiento).all()
