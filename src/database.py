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


def inicializar_base_datos(engine):
    """Crea las tablas en la base de datos si no existen (Ejecutar solo una vez)."""
    Base.metadata.create_all(engine)


def guardar_registro(session, nombre, categoria):
    """Guarda un registro en la base de datos de forma segura."""
    try:
        nuevo_registro = HistorialMovimiento(
            nombre_archivo=nombre, 
            categoria_destino=categoria
        )
        session.add(nuevo_registro)
        session.commit()
    except Exception as e:
        session.rollback() # Si falla, revertir para no corromper la BD
        print(f"Error al guardar en base de datos: {e}")
        raise # Relanzar el error para que las pruebas lo detecten


def obtener_registros(session):
    """Obtiene todos los registros."""
    return session.query(HistorialMovimiento).all()
