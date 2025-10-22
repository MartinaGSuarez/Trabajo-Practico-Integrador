# Proyecto Final Integrador - Programación

## Descripción del Programa

El presente proyecto corresponde a un **Sistema de Gestión de Países**, desarrollado en lenguaje **Python**. El sistema permite administrar, consultar y analizar información sobre diversos países a partir de un archivo de datos denominado `paises.csv`.

El programa implementa conceptos fundamentales de la programación estructurada, incluyendo:

* Estructuras secuenciales, condicionales y repetitivas.
* Uso de funciones y modularización del código.
* Manejo de listas y diccionarios.
* Validación de datos ingresados por el usuario.
* Lectura y escritura de archivos CSV para la persistencia de datos.
* Generación de estadísticas y visualización de resultados por consola.

El sistema se compone de diversos módulos que cumplen funciones específicas, tales como **búsqueda**, **filtrado**, **ordenamiento**, **edición de registros**, **validaciones** y **estadísticas**. El punto de acceso principal es el archivo `main.py`, el cual presenta un menú interactivo que permite al usuario seleccionar la operación deseada.

---

## Instrucciones de Uso

1. Asegúrese de que el archivo `paises.csv` se encuentre en la misma carpeta que los módulos del proyecto.
2. Ejecute el programa principal:

   ```bash
   python main.py
   ```
3. En consola se desplegará un menú principal con las siguientes opciones:

   ```
   === MENÚ PRINCIPAL ===
   1. Buscar país por nombre
   2. Filtrar por continente
   3. Filtrar por rango de población
   4. Filtrar por rango de superficie
   5. Ordenar países
   6. Mostrar estadísticas
   7. Mostrar todos los países
   8. Editar país
   9. Agregar país
   0. Salir
   ```
4. Seleccione una opción ingresando el número correspondiente.
5. Siga las instrucciones que aparecen en pantalla. Algunos comandos solicitarán datos adicionales (por ejemplo, el nombre del país o los rangos de población).

El sistema mostrará los resultados directamente por consola y, en caso de editar o agregar registros, actualizará automáticamente el archivo `paises.csv`.

---

## Ejemplos de Entradas y Salidas

### Ejemplo 1: Búsqueda de un país

**Entrada:**

```
1
Argentina
```

**Salida:**

```
=== RESULTADOS DE BÚSQUEDA ===
Argentina - América | Población: 45376763 | Superficie: 2780400 km²
```

### Ejemplo 2: Filtrado por continente

**Entrada:**

```
2
Europa
```

**Salida:**

```
=== PAISES DE EUROPA ===
Francia - Europa | Población: 67413000 | Superficie: 551695 km²
Italia - Europa | Población: 59554023 | Superficie: 301340 km²
```

### Ejemplo 3: Estadísticas generales

**Entrada:**

```
6
```

**Salida:**

```
=== ESTADÍSTICAS ===
País con mayor población: China (1,412,600,000 habitantes)
País con menor población: Islandia (343,599 habitantes)
Promedio de población: 45,280,934.5
Promedio de superficie: 612,374.8 km²
Cantidad de países por continente: {'América': 25, 'Europa': 30, 'Asia': 20, 'Oceanía': 10, 'África': 40}
```

---

## Requisitos del Sistema

* Python 3.8 o superior.
* Archivo `paises.csv` con los campos: `nombre`, `continente`, `poblacion`, `superficie`.
* Librerías utilizadas: `csv`, `typing`, `unicodedata` (todas parte de la biblioteca estándar de Python).

---

## Autores

* **Martina Suárez**
* **Yoselie Aquino**

---

## Observaciones Finales

El desarrollo de este sistema permite aplicar en conjunto los principales conceptos de la programación modular y la manipulación de datos estructurados. Su diseño facilita la extensión y mantenimiento del código, promoviendo buenas prácticas de desarrollo y la reutilización de funciones en distintos contextos.

