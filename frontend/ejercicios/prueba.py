tareas = []

def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for idx, tarea in enumerate(tareas):
            estado = "✔" if tarea["completada"] else "⏳"
            print(f"{idx}. {tarea['descripcion']} [{estado}]")

def gestionar_tarea():
    while True:
        print("\nBienvenido al gestor de tareas. Selecciona una opción:")
        print("1. Agregar Tarea")
        print("2. Marcar Tarea como Completada")
        print("3. Eliminar Tarea")
        print("4. Ver Tarea")
        print("5. Ver todas las tareas")
        print("6. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            desc = input("Descripción de la tarea: ").strip()
            if desc:
                tareas.append({"descripcion": desc, "completada": False})
                print("Tarea añadida.")
        elif opcion == "2":
            mostrar_tareas()
            try:
                idx = int(input("Número de tarea a marcar como completada: "))
                if 0 <= idx < len(tareas):
                    tareas[idx]["completada"] = True
                    print("Tarea marcada como completada.")
                else:
                    print("Número inválido.")
            except:
                print("Introduce un número válido.")
        elif opcion == "3":
            mostrar_tareas()
            try:
                idx = int(input("Número de tarea a eliminar: "))
                if 0 <= idx < len(tareas):
                    tareas.pop(idx)
                    print("Tarea eliminada.")
                else:
                    print("Número inválido.")
            except:
                print("Introduce un número válido.")
        elif opcion == "4":
            mostrar_tareas()
            try:
                idx = int(input("Número de tarea a ver: "))
                if 0 <= idx < len(tareas):
                    tarea = tareas[idx]
                    estado = "Completada" if tarea["completada"] else "Pendiente"
                    print(f"{tarea['descripcion']} - {estado}")
                else:
                    print("Número inválido.")
            except:
                print("Introduce un número válido.")
        elif opcion == "5":
            mostrar_tareas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

gestionar_tarea()