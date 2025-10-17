from typing import List,Dict,Any

def calcular_estadisticas(paises: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calcula estadísticas básicas sobre los países.
    
    Args:
        paises (List[Dict]): Lista de países.
    
    Returns:
        Dict[str, Any]: Diccionario con estadísticas.
    """
    if not paises:
        print("Error: No hay países para calcular estadísticas.")
        return {}
    
    # Mayor y menor población
    poblaciones = [pais['poblacion'] for pais in paises]
    pais_max_pob = max(paises, key=lambda x: x['poblacion'])
    pais_min_pob = min(paises, key=lambda x: x['poblacion'])
    
    # Promedios
    promedio_poblacion = sum(poblaciones) / len(poblaciones)
    superficies = [pais['superficie'] for pais in paises]
    promedio_superficie = sum(superficies) / len(superficies)
    
    # Cantidad por continente
    continentes = {}
    for pais in paises:
        cont = pais['continente']
        continentes[cont] = continentes.get(cont, 0) + 1
    
    stats = {
        'pais_mayor_poblacion': pais_max_pob['nombre'],
        'poblacion_max': pais_max_pob['poblacion'],
        'pais_menor_poblacion': pais_min_pob['nombre'],
        'poblacion_min': pais_min_pob['poblacion'],
        'promedio_poblacion': round(promedio_poblacion, 2),
        'promedio_superficie': round(promedio_superficie, 2),
        'cantidad_por_continente': continentes
    }
    
    return stats

def mostrar_estadisticas(estadisticas: Dict[str, Any]):
    """
    Muestra las estadísticas en formato legible.
    
    Args:
        estadisticas (Dict): Diccionario de estadísticas.
    """
    if not estadisticas:
        print("No hay estadísticas disponibles.")
        return
    
    print("\n=== ESTADÍSTICAS ===")
    print(f"País con mayor población: {estadisticas['pais_mayor_poblacion']} ({estadisticas['poblacion_max']:,}) habitantes")
    print(f"País con menor población: {estadisticas['pais_menor_poblacion']} ({estadisticas['poblacion_min']:,}) habitantes")
    print(f"Promedio de población: {estadisticas['promedio_poblacion']:,} habitantes")
    print(f"Promedio de superficie: {estadisticas['promedio_superficie']:,} km²")
    print("Cantidad de países por continente:")
    for cont, cantidad in estadisticas['cantidad_por_continente'].items():
        print(f"  - {cont}: {cantidad}")
