"""
Calculadora - Proyecto Principiante #1
Operaciones: suma, resta, multiplicación, división, potencia, raíz cuadrada
"""

import math


def mostrar_menu():
    print("\n" + "=" * 36)
    print("        🧮  CALCULADORA PYTHON")
    print("=" * 36)
    print("  1. Suma              (+)")
    print("  2. Resta             (-)")
    print("  3. Multiplicación    (×)")
    print("  4. División          (÷)")
    print("  5. Potencia          (^)")
    print("  6. Raíz cuadrada     (√)")
    print("  0. Salir")
    print("=" * 36)


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠️  Ingresa un número válido.")


def calcular(opcion):
    if opcion == "1":
        a = pedir_numero("  Número 1: ")
        b = pedir_numero("  Número 2: ")
        resultado = a + b
        expresion = f"{a} + {b}"

    elif opcion == "2":
        a = pedir_numero("  Número 1: ")
        b = pedir_numero("  Número 2: ")
        resultado = a - b
        expresion = f"{a} - {b}"

    elif opcion == "3":
        a = pedir_numero("  Número 1: ")
        b = pedir_numero("  Número 2: ")
        resultado = a * b
        expresion = f"{a} × {b}"

    elif opcion == "4":
        a = pedir_numero("  Número 1: ")
        b = pedir_numero("  Número 2: ")
        if b == 0:
            print("  ❌  Error: no se puede dividir entre cero.")
            return
        resultado = a / b
        expresion = f"{a} ÷ {b}"

    elif opcion == "5":
        a = pedir_numero("  Base: ")
        b = pedir_numero("  Exponente: ")
        resultado = a ** b
        expresion = f"{a} ^ {b}"

    elif opcion == "6":
        a = pedir_numero("  Número: ")
        if a < 0:
            print("  ❌  Error: no existe raíz cuadrada de un número negativo.")
            return
        resultado = math.sqrt(a)
        expresion = f"√{a}"

    else:
        print("  ⚠️  Opción no válida.")
        return

    # Mostrar resultado — entero si no tiene decimales
    if resultado == int(resultado):
        resultado_fmt = int(resultado)
    else:
        resultado_fmt = round(resultado, 10)

    print(f"\n  ✅  {expresion} = {resultado_fmt}")


def main():
    print("\n  Bienvenido a la Calculadora Python 🐍")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción: ").strip()

        if opcion == "0":
            print("\n  ¡Hasta luego! 👋\n")
            break
        else:
            calcular(opcion)


if __name__ == "__main__":
    main()
