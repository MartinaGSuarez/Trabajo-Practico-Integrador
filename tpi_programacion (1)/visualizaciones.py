from typing import List,Dict, Any

def mostrar_paises(paises: List[Dict[str, Any]], titulo: str = "Lista de Países"):
    """
    Muestra una lista de países en formato tabular simple.
    
    Args:
        paises (List[Dict]): Lista de países.
        titulo (str): Título para la lista.
    """
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print(f"\n=== {titulo} ({len(paises)} países) ===")
    print(f"{'Nombre':<20} {'Población':<12} {'Superficie (km²)':<15} {'Continente'}")
    print("-" * 70)
    for pais in paises:
        print(f"{pais['nombre']:<20} {pais['poblacion']:<12,} {pais['superficie']:<15,} {pais['continente']}")
