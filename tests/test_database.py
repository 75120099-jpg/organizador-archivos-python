from src.database import guardar_registro, obtener_registros
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def test_guardar_y_obtener_registro():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    guardar_registro(session, "foto.jpg", "Imagenes")
    registros = obtener_registros(session)

    assert len(registros) == 1
    assert registros[0].nombre_archivo == "foto.jpg"
