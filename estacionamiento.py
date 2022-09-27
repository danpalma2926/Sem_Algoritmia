import os, time, pdb
from datetime import datetime

class Estacionamiento:
    def __init__(self):
        self.lista = []
        self.tipos_de_cambio = [200, 100, 50, 20, 10, 5, 2, 1]
        self.precio_cuarto = 20

    def agregar_vehiculo(self, vehiculo_nuevo):
        self.lista.append(vehiculo_nuevo)

    def pagar_vehiculo(self, placas_buscado, hora_salida):
        for vehiculo in self.lista:
            if vehiculo.placas == placas_buscado:
                ## IMPLEMENTAR ##
                minutos_totales = int((hora_salida - vehiculo.hora_entrada).total_seconds() // 60)
                if minutos_totales <= 0:
                    print(f"Tiempo negativo!!! Ingrese el tiempo de salida ")
                    return
                ## Calcular costo de tiempo
                costo = (minutos_totales // 15) * self.precio_cuarto
                print(f"El costo del estacionamiento es de: ${costo}\n")
                monto = input(f"Ingrese el monto a pagar\n")
                while (int(monto) < costo):
                    monto = input(f"Por favor ingrese el monto correcto")
                cambio = int(monto) - costo
                vehiculo.hora_salida = hora_salida
                vehiculo.costo_total = costo
                return cambio
                    
                

    def existe_vehiculo(self, placas_buscado):
        for vehiculo in self.lista:
            if vehiculo.placas == placas_buscado:
                return True
        return False

    def mostrar_vehiculos(self):
        if len(self.lista) == 0:
            print(f"Lista de vehiculos vacia!!")
            return
        for vehiculo in self.lista:
            print(f"Placas: {vehiculo.placas}\tHora Entrada: {vehiculo.hora_entrada.strftime('%d/%m/%Y %H:%M')}\t", end="")
            if vehiculo.hora_salida != None:
                hora_salida = vehiculo.hora_salida
                print(f"Hora Salida: {hora_salida.strftime('%d/%m/%Y %H:%M')}", end="\t")
            else:
                hora_salida = "--"
                print(f"Hora Salida: {hora_salida}", end="\t")
            if vehiculo.costo_total != None:
                costo_total = vehiculo.costo_total
            else:
                costo_total = "--" 
            print(f"Costo Total: {costo_total}")

class Vehiculo:
    def __init__(self, placas, hora_entrada):
        self.placas = placas
        self.hora_entrada = hora_entrada
        self.hora_salida = None
        self.costo_total = None
        
def agregar_vehiculo(estacionamiento):
    os.system("cls")
    print(f"Agregar vehiculo")
    
    Placas = input(f"Ingrese Placa\n")
    Hora_Entrada = datetime.now()
    estacionamiento.agregar_vehiculo(Vehiculo(Placas, Hora_Entrada))
    print(f"Vehiculo agregado!! \nPresione Enter para continuar")
    input()
    os.system("cls")

def pagar_vehiculo(estacionamiento):
    os.system("cls")
    print(f"Pagar Vehiculo")

    placas_buscar = input(f"Ingrese placas del vehiculo\n")
    if estacionamiento.existe_vehiculo(placas_buscar) == False:
        print(f"Vehiculo inexistente!!!\n")
        input()
        os.system("cls")
        return 
    str_hora_salida = input(f"Ingrese hora de salida (Formato hora:minuto)\n")

    try:
        dia_hoy = datetime.now()
        Hora_Nueva = datetime.strptime(f"{dia_hoy.day}/{dia_hoy.month}/{dia_hoy.year} {str_hora_salida}", "%d/%m/%Y %H:%M")
        cambio = estacionamiento.pagar_vehiculo(placas_buscar, Hora_Nueva)
        print(f"Su cambio es de ${cambio} pesos\n")
        posicion_vector = 0
        monedas = []
        while posicion_vector < len(estacionamiento.tipos_de_cambio):
            if cambio >= estacionamiento.tipos_de_cambio[posicion_vector]:
                cambio -= estacionamiento.tipos_de_cambio[posicion_vector]
                monedas.append(estacionamiento.tipos_de_cambio[posicion_vector])
            else:
                posicion_vector += 1
        print(monedas)

    except SyntaxError:
        print("Hora ingresada incorrectamente!!!")

    print(f"Cuota Pagada!! \nPresione Enter para continuar")
    input()
    os.system("cls")


def mostrar_vehiculos(estacionamiento):
    os.system("cls")
    print(f"Mostando {len(estacionamiento.lista)} vehiculos:")
    estacionamiento.mostrar_vehiculos()

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