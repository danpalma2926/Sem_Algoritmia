import os, time

class Estacionamiento:
    def __init__(self):
        self.lista = []

    def agregar_vehiculo(self, vehiculo_nuevo):
        self.lista.append(vehiculo_nuevo)

    def pagar_vehiculo(self, placas_buscado, hora_salida, monto):
        for vehiculo in self.lista:
            if vehiculo.placas == placas_buscado:
                ## IMPLEMENTAR ##
                pass

    def mostrar_vehiculos(self):
        if len(self.lista) == 0:
            print(f"Lista de vehiculos vacia!!")
            return
        for vehiculo in self.lista:
            if vehiculo.hora_salida != None:
                hora_salida = vehiculo.hora_salida
            else:
                hora_salida = "--"
            if vehiculo.costo_total != None:
                costo_total = vehiculo.costo_total
            else:
                costo_total = "--" 
            print(f"Placas: {vehiculo.placas}\tHora Entrada: {vehiculo.hora_entrada}\t", end="")
            print(f"Hora Salida: {hora_salida}\tCosto Total: {costo_total}")

class Vehiculo:
    def __init__(self, placas, hora_entrada):
        self.placas = placas
        self.hora_entrada = hora_entrada
        self.hora_salida = None
        self.costo_total = None
        
def agregar_vehiculo(estacionamiento):
    os.system("cls")
    print(f"Agregar contacto")
    
    Placas = input(f"Ingrese Placa\n")
    Hora_Entrada = input(f"Ingrese Hora de Entrada\n")

    estacionamiento.insertar_vehiculo(Vehiculo(Placas, Hora_Entrada))
    print(f"Vehiculo agregado!! \nPresione Enter para continuar")
    input()
    os.system("cls")

def pagar_vehiculo(estacionamiento):
    pass

def mostrar_vehiculos(estacionamiento):
    os.system("cls")
    print(f"Mostando {len(estacionamiento.lista)} vehiculos:")
    estacionamiento.vehiculos()

    print(f"\nPresione Enter para continuar")
    input()
    os.system("cls")

def main():
    loop = True
    estacionamiento = Estacionamiento()
    while (loop):
        print(f"Actividad 3 Estacionamiento")
        print(f"1. Agregar Vehiculo")
        print(f"2. Pagar Vehiculo")
        print(f"3. Mostrar Vehiculos")
        print(f"0. Salir")
        opcion = input(f"Por favor seleccione una operacion\n")
        if opcion == "0":
            print(f"Saliendo...")
            time.sleep(2)
            os.system("cls")
            return
        if opcion == "1":
            agregar_vehiculo(estacionamiento)
        elif opcion == "2":
            pagar_vehiculo(estacionamiento)
        elif opcion == "3":
            mostrar_vehiculos(estacionamiento)
        else:
            print(f"Seleccione una opcion valida...")
            time.sleep(2)
            os.system("cls")
            continue

if __name__ == "__main__":
    main()