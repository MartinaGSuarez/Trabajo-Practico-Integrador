from typing import Optional

def obtener_input_int(mensaje: str, permitir_vacio: bool = False):
    while True:
        valor = input(mensaje)
        if permitir_vacio and valor.strip() == "":
            return None
        try:
            return int(valor)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")