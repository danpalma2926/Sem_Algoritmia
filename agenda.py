import os, time

class Agenda:
    def __init__(self):
        self.lista = []

    def insertar_contacto(self, contacto_nuevo):
        self.lista.append(contacto_nuevo)

    def eliminar_contacto(self, ID):
        for contacto in self.lista:
            if contacto.ID == ID:
                self.lista.remove(contacto)
                return True
        return False
        

    def buscar_contacto(self, ID):
        for contacto in self.lista:
            if contacto.ID == ID:
                print(f"ID: {contacto.ID}\tNombre: {contacto.nombre}\tApellido: {contacto.apellido}\t", end="")
                print(f"Telefono: {contacto.telefono}\tCelular: {contacto.celular}")
                return True
        return False

    def mostrar_contactos(self):
        if len(self.lista) == 0:
            print(f"Lista de contactos vacia!!")
            return
        for contacto in self.lista:
            print(f"ID: {contacto.ID}\tNombre: {contacto.nombre}\tApellido: {contacto.apellido}\t", end="")
            print(f"Telefono: {contacto.telefono}\tCelular: {contacto.celular}")

class Contacto:
    def __init__(self, ID, nombre, apellido, telefono, celular):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.celular = celular

def buscar_contacto(agenda):
    os.system("cls")
    print("Eliminar contacto:")
    buscar_ID = input("Ingrese la ID del contacto que desea eliminar\n")

    esEncontrado = agenda.buscar_contacto(buscar_ID)

    if esEncontrado:
        print(f"Contacto con ID {buscar_ID} ha sido encontrado!!\tPresione Enter para continuar")
    else:
        print(f"Contacto con ID {buscar_ID} no encontrado!!\tPresione Enter para continuar")
    input()
    os.system("cls")

def eliminar_contacto(agenda):
    os.system("cls")
    print("Eliminar contacto:")
    buscar_ID = input("Ingrese la ID del contacto que desea eliminar\n")

    esEliminado = agenda.eliminar_contacto(buscar_ID)

    if esEliminado:
        print(f"Contacto con ID {buscar_ID} ha sido eliminado!!\tPresione Enter para continuar")
    else:
        print(f"Contacto con ID {buscar_ID} no encontrado!!\tPresione Enter para continuar")
    input()
    os.system("cls")


def mostrar_contactos(agenda):
    os.system("cls")
    print(f"Mostando {len(agenda.lista)} contactos:")
    agenda.mostrar_contactos()

    print(f"\nPresione Enter para continuar")
    input()
    os.system("cls")

def insertar_contacto(agenda):
    os.system("cls")
    print(f"Agregar contacto")
    
    ID = input(f"Ingrese ID\n")
    Nombre = input(f"Ingrese Nombre\n")
    Apellido = input(f"Ingresar Apellido\n")
    Telefono = input(f"Ingresar Telefono\n")
    Celular = input(f"Ingresar Celular\n")

    agenda.insertar_contacto(Contacto(ID, Nombre, Apellido, Telefono, Celular))
    print(f"Contacto agregado!! \nPresione Enter para continuar")
    input()
    os.system("cls")


def main():
    loop = True
    agenda = Agenda()
    while(loop):
        print(f"Actividad 1 Agenda")
        print(f"1. Mostrar Contactos")
        print(f"2. Insertar Contacto")
        print(f"3. Eliminar Contacto")
        print(f"4. Buscar Contacto")
        print(f"0. Salir")
        opcion = input(f"Por favor seleccione una operacion\n")
        if opcion == "0":
            print(f"Saliendo...")
            time.sleep(2)
            os.system("cls")
            return
        if opcion == "1":
            mostrar_contactos(agenda)
        elif opcion == "2":
            insertar_contacto(agenda)
        elif opcion == "3":
            eliminar_contacto(agenda)
        elif opcion == "4":
            buscar_contacto(agenda)
        else:
            print(f"Seleccione una opcion valida...")
            time.sleep(2)
            os.system("cls")
            continue

if __name__ == "__main__":
    main()