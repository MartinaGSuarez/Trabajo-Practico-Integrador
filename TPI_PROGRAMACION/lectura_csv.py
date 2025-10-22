import csv
from typing import List, Dict, Any

def leer_csv(ruta_archivo: str) -> List[Dict[str, Any]]:
    paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['poblacion'] = int(row['poblacion'])
                    row['superficie'] = int(row['superficie'])
                    row['nombre'] = row['nombre'].strip()
                    row['continente'] = row['continente'].strip()
                    paises.append(row)
                except Exception:
                    # Salta filas con formato inválido
                    continue
        return paises
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        return []
    except Exception as e:
        print(f"Error al leer el CSV: {e}")
        return []

def guardar_csv(ruta_archivo: str, paises: List[Dict[str, Any]]):
    try:
        with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['nombre', 'continente', 'poblacion', 'superficie']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(paises)
    except Exception as e:
        print(f"Error al guardar el CSV: {e}")
