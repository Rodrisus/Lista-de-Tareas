
from datetime import datetime

tareas = []

def mostrar_tareas_pendientes():
    print("tareas:")
for tarea in tareas:
    print(tarea)   
    
tarea = {}

def agregar_tarea(descripcion, fecha, hora):
    tarea = {
        "descripcion": descripcion,
        "fecha_vencimiento": datetime.strptime(fecha, "%d/%m/%Y"),
        "hora_vencimiento": datetime.strptime(hora, "%H:%M"),
        "completada": False,
    }    

    tareas.append(tarea)



def marcar_completada(indice):

    tareas[indice]["completada"] = True    

def mostrar_tareas():
    pendientes = []
    completadas = []

    for tarea in tareas:
        if tarea["completada"] == True:
            completadas.append(tarea)
        else:
            pendientes.append(tarea)

    print("Pendientes:") 
    for tarea in pendientes:
        print(f"Descripción: {tarea['descripcion']}, Fecha de vencimiento: {tarea['fecha_vencimiento'].strftime('%d/%m/%Y')}, Hora de vencimiento: {tarea['hora_vencimiento'].strftime('%H:%M')}, Completada: {tarea['completada']}")

    print("Completadas:") 
    for tarea in completadas:
        print(f"Descripción: {tarea['descripcion']}, Fecha de vencimiento: {tarea['fecha_vencimiento'].strftime('%d/%m/%Y')}, Hora de vencimiento: {tarea['hora_vencimiento'].strftime('%H:%M')}, Completada: {tarea['completada']}")

    pendientes.sort(key=obtener_vencimiento, reverse=True)

def obtener_vencimiento(tarea):
   return tarea["fecha_vencimiento"]

def eliminar_tarea(indice):
   
   tarea = tareas[indice]

   tareas.pop(indice)

   print("La tarea", indice, "ha sido eliminada")

def menu():
    while True:
        print("\nMenú de tareas:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            descripcion = input("Ingresa la descripción de la tarea: ")
            fecha = input("Ingresa la fecha de vencimiento (DD/MM/AAAA): ")
            hora = input("Ingresa la hora de vencimiento (HH:MM): ")
            agregar_tarea(descripcion, fecha, hora)

        elif opcion == "2":
            indice = int(input("Ingresa el índice de la tarea a completar: "))
            marcar_completada(indice)

        elif opcion == "3":
            mostrar_tareas()

        elif opcion == "4":
            indice = int(input("Ingresa el índice de la tarea a eliminar: "))
            eliminar_tarea(indice)

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()