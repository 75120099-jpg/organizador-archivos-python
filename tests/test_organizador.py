from src.organizador import obtener_categoria, organizar_directorio


def test_obtener_categoria_conocida():
    """Prueba si identifica correctamente extensiones registradas."""
    assert obtener_categoria(".jpg") == "Imagenes"
    assert obtener_categoria(".pdf") == "Documentos"
    assert obtener_categoria(".JPG") == "Imagenes"


def test_obtener_categoria_desconocida():
    """Prueba el comportamiento con extensiones no registradas."""
    assert obtener_categoria(".xyz") == "Otros"


def test_organizar_directorio(tmp_path):
    """Prueba la función principal creando un entorno simulado."""
    directorio_prueba = tmp_path / "descargas_prueba"
    directorio_prueba.mkdir()

    archivo_prueba = directorio_prueba / "foto.jpg"
    archivo_prueba.write_text("contenido falso")

    resultado = organizar_directorio(str(directorio_prueba))

    assert resultado is True

    ruta_imagenes = directorio_prueba / "Imagenes"
    assert ruta_imagenes.exists()

    archivo_movido = ruta_imagenes / "foto.jpg"
    assert archivo_movido.exists()
