from typing import List, Dict, Any
from Busquedas import buscar_pais
from validaciones import obtener_input_int

def editar_pais(paises: List[Dict[str, Any]], nombre_pais: str):
    """
    Permite modificar la población o superficie de un país existente.
    """
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
    
    print(f"Datos actualizados correctamente para {pais['nombre']}.")