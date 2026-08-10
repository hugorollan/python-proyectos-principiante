"""
Generador de Contraseñas - Proyecto Principiante #3
Genera contraseñas seguras con opciones configurables.
"""

import random
import string


def mostrar_menu():
    print("\n" + "=" * 40)
    print("     🔐  GENERADOR DE CONTRASEÑAS")
    print("=" * 40)


def pedir_longitud():
    while True:
        try:
            n = int(input("  Longitud de la contraseña (8-64): "))
            if 8 <= n <= 64:
                return n
            print("  ⚠️  Debe estar entre 8 y 64.")
        except ValueError:
            print("  ⚠️  Ingresa un número válido.")


def pedir_si_no(mensaje):
    while True:
        respuesta = input(f"  {mensaje} (s/n): ").strip().lower()
        if respuesta in ("s", "n"):
            return respuesta == "s"
        print("  ⚠️  Responde 's' o 'n'.")


def generar_contrasena(longitud, mayusculas, numeros, simbolos):
    caracteres = string.ascii_lowercase
    obligatorios = []

    if mayusculas:
        caracteres += string.ascii_uppercase
        obligatorios.append(random.choice(string.ascii_uppercase))

    if numeros:
        caracteres += string.digits
        obligatorios.append(random.choice(string.digits))

    if simbolos:
        simbolos_lista = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        caracteres += simbolos_lista
        obligatorios.append(random.choice(simbolos_lista))

    resto = longitud - len(obligatorios)
    contrasena = obligatorios + [random.choice(caracteres) for _ in range(resto)]
    random.shuffle(contrasena)
    return "".join(contrasena)


def evaluar_fortaleza(longitud, mayusculas, numeros, simbolos):
    puntos = 0
    if longitud >= 12:
        puntos += 1
    if longitud >= 16:
        puntos += 1
    if mayusculas:
        puntos += 1
    if numeros:
        puntos += 1
    if simbolos:
        puntos += 1

    if puntos <= 2:
        return "🔴 Débil"
    elif puntos <= 3:
        return "🟡 Media"
    else:
        return "🟢 Fuerte"


def main():
    print("\n  Bienvenido al Generador de Contraseñas 🔐")

    while True:
        mostrar_menu()

        longitud = pedir_longitud()
        mayusculas = pedir_si_no("¿Incluir mayúsculas?")
        numeros = pedir_si_no("¿Incluir números?")
        simbolos = pedir_si_no("¿Incluir símbolos?")

        contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
        fortaleza = evaluar_fortaleza(longitud, mayusculas, numeros, simbolos)

        print(f"\n  {'─' * 36}")
        print(f"  🔑  {contrasena}")
        print(f"  Fortaleza: {fortaleza}")
        print(f"  {'─' * 36}")

        otra = pedir_si_no("\n  ¿Generar otra contraseña?")
        if not otra:
            print("\n  ¡Hasta luego! 👋\n")
            break


if __name__ == "__main__":
    main()
