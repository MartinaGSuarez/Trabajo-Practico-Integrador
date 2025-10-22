from typing import List, Dict, Any
from busquedas import normalizar_texto

def ordenar_paises(paises: List[Dict[str, Any]], criterio: str, ascendente: bool = True) -> List[Dict[str, Any]]:
    if not paises:
        return []
    if criterio not in ['nombre', 'poblacion', 'superficie']:
        return paises
    reverse = not ascendente
    if criterio == 'nombre':
        return sorted(paises, key=lambda x: normalizar_texto(x['nombre']), reverse=reverse)
    elif criterio == 'poblacion':
        return sorted(paises, key=lambda x: x['poblacion'], reverse=reverse)
    else:
        return sorted(paises, key=lambda x: x['superficie'], reverse=reverse)
