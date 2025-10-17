import csv
from typing import List, Dict, Any, Optional

# PARTE 1: LECTURA DE DATOS DESDE CSV


def leer_csv(ruta_archivo: str) -> List[Dict[str, Any]]:
    """
    Lee el archivo CSV y retorna una lista de diccionarios representando los países.
    
    Args:
        ruta_archivo (str): Ruta al archivo CSV.
    
    Returns:
        List[Dict[str, Any]]: Lista de países como diccionarios.
    
    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el formato del CSV es inválido.
    """
    paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Validar y convertir tipos de datos
                try:
                    row['poblacion'] = int(row['poblacion'])
                    row['superficie'] = int(row['superficie'])
                    # Limpiar strings (quitar espacios extra)
                    row['nombre'] = row['nombre'].strip()
                    row['continente'] = row['continente'].strip()
                    paises.append(row)
                except ValueError as e:
                    print(f"Error en formato de datos en fila: {row}. Error: {e}")
                    continue  # Saltar fila inválida
        if not paises:
            raise ValueError("El archivo CSV está vacío o no contiene datos válidos.")
        print(f"Archivo CSV leído exitosamente. Cargados {len(paises)} países.")
        return paises
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return []