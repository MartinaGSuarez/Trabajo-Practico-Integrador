import unicodedata
from typing import List, Dict, Any

def normalizar_texto(texto: str) -> str:
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto.lower().strip()

def buscar_pais(paises: List[Dict[str, Any]], nombre_busqueda: str) -> List[Dict[str, Any]]:
    if not nombre_busqueda or not nombre_busqueda.strip():
        return []
    nombre_busqueda = normalizar_texto(nombre_busqueda)
    return [p for p in paises if nombre_busqueda in normalizar_texto(p['nombre'])]
