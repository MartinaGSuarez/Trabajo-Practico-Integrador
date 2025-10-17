from typing import List,Dict, Any

def filtrar_por_continente(paises: List[Dict[str, Any]], continente: str) -> List[Dict[str, Any]]:
    """
    Filtra países por continente (insensible a mayúsculas).
    
    Args:
        paises (List[Dict]): Lista de países.
        continente (str): Nombre del continente.
    
    Returns:
        List[Dict]: Lista de países filtrados.
    """
    if not continente.strip():
        print("Error: El continente no puede estar vacío.")
        return []
    
    continente = continente.lower().strip()
    resultados = [
        pais for pais in paises
        if continente in pais['continente'].lower()
    ]
    
    if not resultados:
        print(f"No se encontraron países en el continente '{continente}'.")
    else:
        print(f"Se encontraron {len(resultados)} países en el continente '{continente}'.")
    
    return resultados

def filtrar_por_rango_poblacion(paises: List[Dict[str, Any]], min_pob: int, max_pob: int) -> List[Dict[str, Any]]:
    """
    Filtra países por rango de población (inclusive).
    
    Args:
        paises (List[Dict]): Lista de países.
        min_pob (int): Población mínima.
        max_pob (int): Población máxima.
    
    Returns:
        List[Dict]: Lista de países filtrados.
    """
    if min_pob < 0 or max_pob < min_pob:
        print("Error: Rango de población inválido (mínimo >= 0 y máximo >= mínimo).")
        return []
    
    resultados = [
        pais for pais in paises
        if min_pob <= pais['poblacion'] <= max_pob
    ]
    
    if not resultados:
        print(f"No se encontraron países con población entre {min_pob} y {max_pob}.")
    else:
        print(f"Se encontraron {len(resultados)} países con población entre {min_pob} y {max_pob}.")
    
    return resultados

def filtrar_por_rango_superficie(paises: List[Dict[str, Any]], min_sup: int, max_sup: int) -> List[Dict[str, Any]]:
    """
    Filtra países por rango de superficie (inclusive).
    
    Args:
        paises (List[Dict]): Lista de países.
        min_sup (int): Superficie mínima en km².
        max_sup (int): Superficie máxima en km².
    
    Returns:
        List[Dict]: Lista de países filtrados.
    """
    if min_sup < 0 or max_sup < min_sup:
        print("Error: Rango de superficie inválido (mínimo >= 0 y máximo >= mínimo).")
        return []
    
    resultados = [
        pais for pais in paises
        if min_sup <= pais['superficie'] <= max_sup
    ]
    
    if not resultados:
        print(f"No se encontraron países con superficie entre {min_sup} y {max_sup} km².")
    else:
        print(f"Se encontraron {len(resultados)} países con superficie entre {min_sup} y {max_sup} km².")
    
    return resultados