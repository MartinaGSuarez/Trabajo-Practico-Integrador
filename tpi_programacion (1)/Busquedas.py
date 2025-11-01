from typing import List, Dict, Any
import unicodedata

def normalizar_texto(texto: str) -> str:
    """Elimina acentos y pasa a minúsculas para comparar textos."""
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto.lower().strip()

def buscar_pais(paises: List[Dict[str, Any]], nombre_busqueda: str) -> List[Dict[str, Any]]:
    if not nombre_busqueda.strip():
        print("Error: El nombre de búsqueda no puede estar vacío.")
        return []
    
    nombre_busqueda = normalizar_texto(nombre_busqueda)
    resultados = [
        pais for pais in paises
        if nombre_busqueda in normalizar_texto(pais['nombre'])
    ]
    
    if not resultados:
        print(f"No se encontraron países con nombre que contenga '{nombre_busqueda}'.")
    else:
        print(f"Se encontraron {len(resultados)} país(es) con nombre que contenga '{nombre_busqueda}'.")
    
    return resultados