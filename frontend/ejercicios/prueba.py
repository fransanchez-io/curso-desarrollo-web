tareas=[]
def gestionar_tarea():
    opcion=0
    while opcion !=5:
        print("Bienvenido al gestor de tareas.\n Seleccione una opción")
        print("1. Agregar Tarea.\n2. Marcar Tarea como Completada.\n3. Eliminar Tarea.\n4. Ver Tarea.\n5. Salir.")
        opcion=int(input("Que opcion desea: "))
        if opcion ==1:
            tareas.append(input("Que tarea quieres añadir?: "))
  
        elif opcion==2:
            marcar=int(input("Que tarea quieres marcar como completada?: "))
            if marcar < len(tareas):
                tareas[marcar] = True
            else:
                print("Esa tarea no esta en la lista")
        elif opcion ==3:
            eliminar=input("Que nombre quieres eleminiar?: ")
            if eliminar in tareas:
                tareas.remove(eliminar)
            else:
                print("Esa tarea no esta en la lista")
        elif opcion==4:
            consulta=int(input("Que tarea quieres ver?: "))
            if consulta < len(tareas):
                print(tareas[consulta])
            else:
                print("Esa tarea no esta en la lista")
gestionar_tarea()