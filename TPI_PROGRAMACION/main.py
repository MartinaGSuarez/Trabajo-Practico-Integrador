from lectura_csv import leer_csv
from busquedas import buscar_pais
from filtros import (
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie
)
from ordenamiento import ordenar_paises
from estadisticas import calcular_estadisticas, mostrar_estadisticas
from visualizaciones import mostrar_paises
from edicion import editar_pais, agregar_pais
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
    print("9. Agregar país")
    print("0. Salir")

def menu_principal():
    paises = leer_csv('paises.csv')
    if not paises:
        print("No se cargaron países. Asegurate de tener 'paises.csv' en la misma carpeta que este proyecto.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '0':
            print("¡Gracias por usar el programa!")
            break
        elif opcion == '1':
            nombre = input("Ingrese el nombre o parte del nombre del país: ")
            resultados = buscar_pais(paises, nombre)
            if resultados:
                mostrar_paises(resultados, "Resultados de Búsqueda")
            else:
                print("No se encontraron países con ese nombre.")
        elif opcion == '2':
            cont = input("Ingrese el continente: ")
            resultados = filtrar_por_continente(paises, cont)
            if resultados:
                mostrar_paises(resultados, f"Países de {cont}")
            else:
                print("No se encontraron países en ese continente.")
        elif opcion == '3':
            min_p = obtener_input_int("Población mínima: ")
            max_p = obtener_input_int("Población máxima: ")
            if min_p is None or max_p is None:
                print("Rango inválido.")
            else:
                resultados = filtrar_por_rango_poblacion(paises, min_p, max_p)
                if resultados:
                    mostrar_paises(resultados, "Países filtrados por población")
                else:
                    print("No se encontraron países en ese rango de población.")
        elif opcion == '4':
            min_s = obtener_input_int("Superficie mínima: ")
            max_s = obtener_input_int("Superficie máxima: ")
            if min_s is None or max_s is None:
                print("Rango inválido.")
            else:
                resultados = filtrar_por_rango_superficie(paises, min_s, max_s)
                if resultados:
                    mostrar_paises(resultados, "Países filtrados por superficie")
                else:
                    print("No se encontraron países en ese rango de superficie.")
        elif opcion == '5':
            criterio = input("Ingrese criterio (nombre/poblacion/superficie): ").lower()
            asc = input("Orden ascendente (s/n)? ").strip().lower() == 's'
            ordenados = ordenar_paises(paises, criterio, asc)
            mostrar_paises(ordenados, "Países ordenados")
        elif opcion == '6':
            mostrar_estadisticas(calcular_estadisticas(paises))
        elif opcion == '7':
            mostrar_paises(paises, "Todos los países")
        elif opcion == '8':
            nombre = input("Ingrese el país que desea editar: ")
            editar_pais(paises, nombre)
        elif opcion == '9':
            agregar_pais(paises)
        else:
            print("Opción inválida.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
