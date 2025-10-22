from typing import List, Dict, Any

def calcular_estadisticas(paises: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not paises:
        return {}
    poblaciones = [p['poblacion'] for p in paises]
    superficies = [p['superficie'] for p in paises]
    pais_max = max(paises, key=lambda x: x['poblacion'])
    pais_min = min(paises, key=lambda x: x['poblacion'])

    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1

    return {
        'pais_mayor_poblacion': pais_max['nombre'],
        'poblacion_max': pais_max['poblacion'],
        'pais_menor_poblacion': pais_min['nombre'],
        'poblacion_min': pais_min['poblacion'],
        'promedio_poblacion': round(sum(poblaciones) / len(poblaciones), 2),
        'promedio_superficie': round(sum(superficies) / len(superficies), 2),
        'cantidad_por_continente': continentes
    }

def mostrar_estadisticas(estadisticas: Dict[str, Any]):
    if not estadisticas:
        print("No hay estadísticas disponibles.")
        return
    print("\n=== ESTADÍSTICAS ===")
    print(f"País con mayor población: {estadisticas['pais_mayor_poblacion']} ({estadisticas['poblacion_max']:,})")
    print(f"País con menor población: {estadisticas['pais_menor_poblacion']} ({estadisticas['poblacion_min']:,})")
    print(f"Promedio de población: {estadisticas['promedio_poblacion']:,}")
    print(f"Promedio de superficie: {estadisticas['promedio_superficie']:,} km²")
    print("Cantidad por continente:")
    for c, cant in estadisticas['cantidad_por_continente'].items():
        print(f"  - {c}: {cant}")
