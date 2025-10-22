from typing import List, Dict, Any
from busquedas import normalizar_texto

def filtrar_por_continente(paises: List[Dict[str, Any]], continente: str) -> List[Dict[str, Any]]:
    if not continente or not continente.strip():
        return []
    cont_norm = normalizar_texto(continente)
    return [p for p in paises if cont_norm in normalizar_texto(p['continente'])]

def filtrar_por_rango_poblacion(paises: List[Dict[str, Any]], min_pob: int, max_pob: int) -> List[Dict[str, Any]]:
    if min_pob is None or max_pob is None or min_pob < 0 or max_pob < min_pob:
        return []
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

def filtrar_por_rango_superficie(paises: List[Dict[str, Any]], min_sup: int, max_sup: int) -> List[Dict[str, Any]]:
    if min_sup is None or max_sup is None or min_sup < 0 or max_sup < min_sup:
        return []
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]
