from lectura_csv import leer_csv
from Busquedas import buscar_pais
from filtros import (
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie
)
from Ordenamiento import ordenar_paises
from Estadisticas import calcular_estadisticas, mostrar_estadisticas
from visualizaciones import mostrar_paises
from edicion import editar_pais
from validaciones import obtener_input_int

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("8. Editar país")
    print("0. Salir")

def menu_principal():
    paises = leer_csv('paises.csv')
    if not paises:
        return
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '0':
            print("¡Gracias por usar el programa!")
            break
        elif opcion == '1':
            nombre = input("Ingrese el nombre o parte del nombre del país: ")
            mostrar_paises(buscar_pais(paises, nombre), "Resultados de Búsqueda")
        elif opcion == '2':
            cont = input("Ingrese el continente: ")
            mostrar_paises(filtrar_por_continente(paises, cont), "Países Filtrados por Continente")
        elif opcion == '3':
            min_p = obtener_input_int("Población mínima: ")
            max_p = obtener_input_int("Población máxima: ")
            if min_p is not None and max_p is not None:
                mostrar_paises(filtrar_por_rango_poblacion(paises, min_p, max_p), "Países Filtrados por Población")
        elif opcion == '4':
            min_s = obtener_input_int("Superficie mínima: ")
            max_s = obtener_input_int("Superficie máxima: ")
            if min_s is not None and max_s is not None:
                mostrar_paises(filtrar_por_rango_superficie(paises, min_s, max_s), "Países Filtrados por Superficie")
        elif opcion == '5':
            criterio = input("Ingrese criterio (nombre/poblacion/superficie): ").lower()
            asc = input("Orden ascendente (s/n)? ").strip().lower() == 's'
            mostrar_paises(ordenar_paises(paises, criterio, asc), "Países Ordenados")
        elif opcion == '6':
            mostrar_estadisticas(calcular_estadisticas(paises))
        elif opcion == '7':
            mostrar_paises(paises, "Todos los Países")
        elif opcion == '8':
            nombre = input("Ingrese el país que desea editar: ")
            editar_pais(paises,nombre)
        else:
            print("Opción inválida.")
        
        input("\nPresione Enter para continuar...")

# Punto de entrada.
if __name__ == "__main__":
    menu_principal()