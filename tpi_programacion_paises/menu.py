from typing import Optional


from lectura_csv import leer_csv
from Busquedas import buscar_pais
from filtro import (
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie
)
from Ordenamiento import ordenar_paises
from Estadisticas import calcular_estadisticas, mostrar_estadisticas
from visualizaciones import mostrar_paises


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("0. Salir")

def obtener_input_int(mensaje: str, min_val: int = 0) -> Optional[int]:
    """
    Obtiene un entero válido del usuario.
    
    Args:
        mensaje (str): Mensaje para el input.
        min_val (int): Valor mínimo permitido.
    
    Returns:
        Optional[int]: Entero válido o None si inválido.
    """
    try:
        valor = int(input(mensaje))
        if valor < min_val:
            print(f"Error: El valor debe ser >= {min_val}.")
            return None
        return valor
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return None

def menu_principal():
    """
    Función principal que maneja el menú interactivo.
    """
    # Cargar datos al inicio
    paises = leer_csv('paises.csv')  # Asumir que el CSV se llama 'paises.csv'
    if not paises:
        print("No se pudieron cargar los datos. Saliendo del programa.")
        return
    
    paises_actuales = paises.copy()  # Copia para no modificar la original en filtros/ordenamientos
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '0':
            print("¡Gracias por usar el programa!")
            break
        
        elif opcion == '1':
            # Búsqueda por nombre
            nombre = input("Ingrese el nombre o parte del nombre del país: ")
            resultados = buscar_pais(paises_actuales, nombre)
            mostrar_paises(resultados, "Resultados de Búsqueda")
        
        elif opcion == '2':
            # Filtro por continente
            continente = input("Ingrese el continente: ")
            resultados = filtrar_por_continente(paises_actuales, continente)
            mostrar_paises(resultados, "Países Filtrados por Continente")
        
        elif opcion == '3':
            # Filtro por rango de población
            print("Ingrese el rango de población (inclusive):")
            min_pob = obtener_input_int("Población mínima: ")
            if min_pob is None:
                continue
            max_pob = obtener_input_int("Población máxima: ")
            if max_pob is None:
                continue
            resultados = filtrar_por_rango_poblacion(paises_actuales, min_pob, max_pob)
            mostrar_paises(resultados, "Países Filtrados por Población")
        
        elif opcion == '4':
            # Filtro por rango de superficie
            print("Ingrese el rango de superficie en km² (inclusive):")
            min_sup = obtener_input_int("Superficie mínima: ")
            if min_sup is None:
                continue
            max_sup = obtener_input_int("Superficie máxima: ")
            if max_sup is None:
                continue
            resultados = filtrar_por_rango_superficie(paises_actuales, min_sup, max_sup)
            mostrar_paises(resultados, "Países Filtrados por Superficie")
        
        elif opcion == '5':
            # Ordenamiento
            criterio = input("Ingrese criterio de ordenamiento (nombre/poblacion/superficie): ").strip().lower()
            if criterio not in ['nombre', 'poblacion', 'superficie']:
                print("Criterio inválido.")
                continue
            asc = input("Orden ascendente (s/n)? ").strip().lower() == 's'
            paises_ordenados = ordenar_paises(paises_actuales, criterio, asc)
            mostrar_paises(paises_ordenados, "Países Ordenados")
        
        elif opcion == '6':
            # Estadísticas
            stats = calcular_estadisticas(paises_actuales)
            mostrar_estadisticas(stats)
        
        elif opcion == '7':
            # Mostrar todos
            mostrar_paises(paises_actuales, "Todos los Países")
        
        else:
            print("Opción inválida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()

