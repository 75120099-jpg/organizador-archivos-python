import os
import shutil
from src.mapeo import EXTENSIONES


def obtener_categoria(extension):
    """Devuelve la carpeta correspondiente a la extensión."""
    return EXTENSIONES.get(extension.lower(), "Otros")


def organizar_directorio(ruta_directorio):
    """Organiza los archivos del directorio especificado."""
    if not os.path.exists(ruta_directorio):
        return False

    for archivo in os.listdir(ruta_directorio):
        ruta_archivo = os.path.join(ruta_directorio, archivo)

        if os.path.isdir(ruta_archivo):
            continue

        nombre, extension = os.path.splitext(archivo)

        if not extension:
            continue

        categoria = obtener_categoria(extension)
        ruta_categoria = os.path.join(ruta_directorio, categoria)

        if not os.path.exists(ruta_categoria):
            os.makedirs(ruta_categoria)

        shutil.move(ruta_archivo, os.path.join(ruta_categoria, archivo))

    return True
