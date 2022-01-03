#!/usr/bin/python3

import os

#Calculadora con sus funciones básicas: suma, resta, multiplicación y división.
class calculator(object):
    def __init__(self):
        pass

    #Recibe dos números e imprime en pantalla el resultado de sumarlos entre sí    
    def suma():
        n1, n2 = solicitarValores()
        print(f"Resultado: {n1} + {n2} = {n1 + n2}")
    
    #Recibe dos números e imprime en pantalla el resultado de restarle el 2do al 1ero
    def resta():
        n1, n2 = solicitarValores()
        print(f"Resultado: {n1} - {n2} = {n1 - n2}")

    #Recibe dos números e imprime en pantalla el resultado de multiplicarlos entre sí
    def multiplicacion():
        n1, n2 = solicitarValores()
        print(f"Resultado: {n1} * {n2} = {n1 * n2}")

    #Recibe dos números e imprime en pantalla el resultado de dividir el 1ero entre el 2
    def division():
        n1, n2 = solicitarValores()
        print(f"Resultado: {n1} / {n2} = {n1 / n2}")


#Imprime en pantalla una lista de opciones disponibles para el usuario
def menu():
    print("╔═════════╗")
    print("║  Calc:  ║")
    print("╚═════════╝")
    print("  1.Suma")
    print("  2.Resta")
    print("  3.Multiplicación")
    print("  4.División")
    print("  5.Salir\n")

    opcion = input("Ingrese una opción(1..5): ")
    return opcion

#Retorna True si la variable recibida es un float y en caso contrario retorna False
def es_flotante(variable):
	try:
		float(variable)
		return True
	except:
		return False

#Pide al usuario el ingreso de dos números
def solicitarValores():
    centinela = True
    while centinela:
        n1 = input("\nIngrese el primer valor: ")
        n2 = input("Ingrese el segundo valor: ")
        
        #Si los dos números ingresados por el usuario son válidos, se termina el ciclo while
        if es_flotante(n1) and es_flotante(n2):
            centinela = False
        else:
            print("\nNo has ingresado valores válidos. Intenta nuevamente.")
            
    print()
    return (float(n1), float(n2))

def main():
    while True:
        opcion = menu()

        if opcion == '1':
            calculator.suma()

        elif opcion == '2':
            calculator.resta()

        elif opcion == '3':
            calculator.multiplicacion()

        elif opcion == '4':
            calculator.division()

        elif opcion == '5':
            print("¡Has decidido salir. Gracias por usar la calculadora!")
            exit()
        
        else:
            print("Opción inválida.")

        input("\nPresione ENTER para continuar...")
        os.system("cls")

if __name__ == '__main__':
    main()