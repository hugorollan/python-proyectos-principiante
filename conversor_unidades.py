"""
Conversor de Unidades - Proyecto Principiante #4
Convierte entre unidades de longitud, peso y temperatura.
"""


def mostrar_menu():
    print("\n" + "=" * 40)
    print("      📐  CONVERSOR DE UNIDADES")
    print("=" * 40)
    print("  1. Longitud")
    print("  2. Peso")
    print("  3. Temperatura")
    print("  0. Salir")
    print("=" * 40)


def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("  ⚠️  Ingresa un número válido.")


def longitud():
    print("\n  --- Longitud ---")
    print("  1. Kilómetros → Millas")
    print("  2. Millas → Kilómetros")
    print("  3. Metros → Pies")
    print("  4. Pies → Metros")
    op = input("  Opción: ").strip()
    v = pedir_numero("  Valor: ")

    conversiones = {
        "1": f"{v} km = {v * 0.621371:.4f} millas",
        "2": f"{v} millas = {v * 1.60934:.4f} km",
        "3": f"{v} m = {v * 3.28084:.4f} pies",
        "4": f"{v} pies = {v * 0.3048:.4f} m",
    }

    if op in conversiones:
        print(f"\n  ✅  {conversiones[op]}")
    else:
        print("  ⚠️  Opción no válida.")


def peso():
    print("\n  --- Peso ---")
    print("  1. Kilogramos → Libras")
    print("  2. Libras → Kilogramos")
    print("  3. Kilogramos → Onzas")
    print("  4. Onzas → Kilogramos")
    op = input("  Opción: ").strip()
    v = pedir_numero("  Valor: ")

    conversiones = {
        "1": f"{v} kg = {v * 2.20462:.4f} libras",
        "2": f"{v} libras = {v * 0.453592:.4f} kg",
        "3": f"{v} kg = {v * 35.274:.4f} onzas",
        "4": f"{v} onzas = {v * 0.0283495:.4f} kg",
    }

    if op in conversiones:
        print(f"\n  ✅  {conversiones[op]}")
    else:
        print("  ⚠️  Opción no válida.")


def temperatura():
    print("\n  --- Temperatura ---")
    print("  1. Celsius → Fahrenheit")
    print("  2. Fahrenheit → Celsius")
    print("  3. Celsius → Kelvin")
    print("  4. Kelvin → Celsius")
    op = input("  Opción: ").strip()
    v = pedir_numero("  Valor: ")

    conversiones = {
        "1": f"{v}°C = {v * 9/5 + 32:.2f}°F",
        "2": f"{v}°F = {(v - 32) * 5/9:.2f}°C",
        "3": f"{v}°C = {v + 273.15:.2f} K",
        "4": f"{v} K = {v - 273.15:.2f}°C",
    }

    if op in conversiones:
        print(f"\n  ✅  {conversiones[op]}")
    else:
        print("  ⚠️  Opción no válida.")


def main():
    print("\n  Bienvenido al Conversor de Unidades 📐")

    while True:
        mostrar_menu()
        op = input("  Elige una opción: ").strip()

        if op == "1":
            longitud()
        elif op == "2":
            peso()
        elif op == "3":
            temperatura()
        elif op == "0":
            print("\n  ¡Hasta luego! 👋\n")
            break
        else:
            print("  ⚠️  Opción no válida.")


if __name__ == "__main__":
    main()
