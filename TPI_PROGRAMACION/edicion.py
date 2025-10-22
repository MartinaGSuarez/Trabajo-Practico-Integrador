from typing import List, Dict, Any
from busquedas import buscar_pais
from lectura_csv import guardar_csv
from validaciones import obtener_input_int

def editar_pais(paises: List[Dict[str, Any]], nombre_pais: str):
    resultados = buscar_pais(paises, nombre_pais)
    if not resultados:
        print("No se encontró el país para editar.")
        return
    pais = resultados[0]
    print(f"\nEditando: {pais['nombre']}")
    print(f"Población actual: {pais['poblacion']}")
    print(f"Superficie actual: {pais['superficie']} km²")

    nueva_poblacion = obtener_input_int("Nueva población (Enter para mantener igual): ", permitir_vacio=True)
    nueva_superficie = obtener_input_int("Nueva superficie (Enter para mantener igual): ", permitir_vacio=True)

    if nueva_poblacion is not None:
        pais['poblacion'] = nueva_poblacion
    if nueva_superficie is not None:
        pais['superficie'] = nueva_superficie

    guardar_csv('paises.csv', paises)
    print(f"Datos actualizados y guardados correctamente para {pais['nombre']}.")

def agregar_pais(paises: List[Dict[str, Any]]):
    nombre = input("Nombre del país: ").strip()
    continente = input("Continente: ").strip()
    poblacion = obtener_input_int("Población: ")
    superficie = obtener_input_int("Superficie (km²): ")

    if not nombre or not continente or poblacion is None or superficie is None:
        print("Error: Todos los campos son obligatorios.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "continente": continente,
        "poblacion": poblacion,
        "superficie": superficie
    }

    paises.append(nuevo_pais)
    guardar_csv('paises.csv', paises)
    print(f"País '{nombre}' agregado correctamente y guardado en el archivo.")
