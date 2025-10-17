from typing import List, Dict, Any


def buscar_pais(paises: List[Dict[str, Any]], nombre_busqueda: str) -> List[Dict[str, Any]]:
    """
    Busca países por nombre (coincidencia parcial o exacta, insensible a mayúsculas).
    
    Args:
        paises (List[Dict]): Lista de países.
        nombre_busqueda (str): Nombre o parte del nombre a buscar.
    
    Returns:
        List[Dict]: Lista de países que coinciden.
    """
    if not nombre_busqueda.strip():
        print("Error: El nombre de búsqueda no puede estar vacío.")
        return []
    
    nombre_busqueda = nombre_busqueda.lower().strip()
    resultados = [
        pais for pais in paises
        if nombre_busqueda in pais['nombre'].lower()
    ]
    
    if not resultados:
        print(f"No se encontraron países con nombre que contenga '{nombre_busqueda}'.")
    else:
        print(f"Se encontraron {len(resultados)} país(es) con nombre que contenga '{nombre_busqueda}'.")
    
    return resultados