"""
Lista de Tareas (CLI) - Proyecto Principiante #2
Las tareas se guardan en tareas.json para que persistan al cerrar.
"""

import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)


def mostrar_tareas(tareas):
    print("\n" + "=" * 40)
    print("        📋  LISTA DE TAREAS")
    print("=" * 40)
    if not tareas:
        print("  (sin tareas — agrega una con la opción 1)")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "✅" if tarea["completada"] else "⬜"
            print(f"  {i}. {estado}  {tarea['nombre']}")
    print("=" * 40)


def mostrar_menu():
    print("\n  1. Agregar tarea")
    print("  2. Completar tarea")
    print("  3. Eliminar tarea")
    print("  0. Salir")


def agregar_tarea(tareas):
    nombre = input("\n  Nombre de la tarea: ").strip()
    if not nombre:
        print("  ⚠️  El nombre no puede estar vacío.")
        return
    tareas.append({"nombre": nombre, "completada": False})
    guardar_tareas(tareas)
    print(f"  ✅  Tarea '{nombre}' agregada.")


def completar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        n = int(input("  Número de tarea a completar: "))
        if 1 <= n <= len(tareas):
            tareas[n - 1]["completada"] = True
            guardar_tareas(tareas)
            print(f"  ✅  '{tareas[n-1]['nombre']}' marcada como completada.")
        else:
            print("  ⚠️  Número fuera de rango.")
    except ValueError:
        print("  ⚠️  Ingresa un número válido.")


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        n = int(input("  Número de tarea a eliminar: "))
        if 1 <= n <= len(tareas):
            eliminada = tareas.pop(n - 1)
            guardar_tareas(tareas)
            print(f"  🗑️  '{eliminada['nombre']}' eliminada.")
        else:
            print("  ⚠️  Número fuera de rango.")
    except ValueError:
        print("  ⚠️  Ingresa un número válido.")


def main():
    print("\n  Bienvenido a la Lista de Tareas 📋")
    tareas = cargar_tareas()

    while True:
        mostrar_tareas(tareas)
        mostrar_menu()
        opcion = input("\n  Elige una opción: ").strip()

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            completar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "0":
            print("\n  ¡Hasta luego! 👋\n")
            break
        else:
            print("  ⚠️  Opción no válida.")


if __name__ == "__main__":
    main()
