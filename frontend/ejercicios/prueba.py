print("¡Hola GitHub desde VS Code!")

tareas=[]
def gestionar_tarea():
    opcion=0
    while opcion !=5:
        print("Bienvenido al gestor de tareas.\n Seleccione una opción")
        print("1. Agregar Tarea.\n2. Marcar Tarea como Completada.\n3. Eliminar Tarea.\n4. Ver Tarea.\n5. Salir.")
        opcion=int(input("Que opcion desea: "))
        if opcion ==1:
            agregar=input("Que tarea quieres añadir?: ").split()
            agregar=False
            tareas.extend(agregar)    
        elif opcion==2:
            accion=input("Que tarea quieres realizar?: ")
            if accion in tareas:
                accion=True
            else:
                print("Esa tarea no esta en la lista")
        elif opcion ==3:
            eliminar=input("Que nombre quieres eleminiar?: ")
            if eliminar in tareas:
                tareas.remove(eliminar)
            else:
                print("Esa tarea no esta en la lista")
        elif opcion==4:
            consulta=input("Que tarea desa consultar?: ")
            if consulta == True:
                print("La tarea: ",tareas[consulta], "Esta completada")
            else:
                print("La tarea: ",tareas[consulta], "No esta completada")
    print("Muchas gracias y hasta luego")   

gestionar_tarea()