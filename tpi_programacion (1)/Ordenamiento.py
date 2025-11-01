from typing import List, Dict, Any
from Busquedas import normalizar_texto  # Importar normalización

def ordenar_paises(paises: List[Dict[str, Any]], criterio: str, ascendente: bool = True) -> List[Dict[str, Any]]:
    """
    Ordena la lista de países por un criterio específico.
    
    Args:
        paises (List[Dict]): Lista de países.
        criterio (str): 'nombre', 'poblacion' o 'superficie'.
        ascendente (bool): True para ascendente, False para descendente.
    
    Returns:
        List[Dict]: Lista ordenada.
    
    Raises:
        ValueError: Si el criterio es inválido.
    """
    if not paises:
        print("Error: No hay países para ordenar.")
        return []
    
    if criterio not in ['nombre', 'poblacion', 'superficie']:
        print(f"Error: Criterio '{criterio}' inválido. Use 'nombre', 'poblacion' o 'superficie'.")
        return paises
    
    reverse = not ascendente
    if criterio == 'nombre':
        paises_ordenados = sorted(paises, key=lambda x: normalizar_texto(x['nombre']), reverse=reverse)
    elif criterio == 'poblacion':
        paises_ordenados = sorted(paises, key=lambda x: x['poblacion'], reverse=reverse)
    else:  # superficie
        paises_ordenados = sorted(paises, key=lambda x: x['superficie'], reverse=reverse)
    
    direccion = "ascendente" if ascendente else "descendente"
    print(f"Países ordenados por {criterio} en orden {direccion}.")
    return paises_ordenados