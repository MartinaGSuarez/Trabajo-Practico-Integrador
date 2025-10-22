from typing import List, Dict, Any

def mostrar_paises(paises: List[Dict[str, Any]], titulo: str):
    if not paises:
        print("No hay países para mostrar.")
        return
    print(f"\n=== {titulo} ===")
    for p in paises:
        print(f"{p['nombre']} - {p['continente']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
