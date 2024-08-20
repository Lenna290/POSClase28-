carrito = []
total = 0.0

def mostrar_menu():
    print("Bienvenido al POS")
    print("1. Agregar producto al carrito")
    print("2. Ver total del carrito")
    print("3. Pagar")
    print("4. Salir")
mostrar_menu()

def agregar_producto():
    global total
    
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    carrito.append({"producto": producto, "precio": precio})
    total += precio
    print(f"Has agregado {producto} al carrito por {precio}.")
    
    
agregar_producto()
print(carrito)

def ver_total():
    print(f"El total de tu carrito es: {total}")

def pagar():
    global toatal, carrito
    if total ==0:
        print("Tu carrito esta acio, no hay nada que pagar.")
    else:
        print(f"El total a pagar es: {total}")
        pago = float(input("Ingresa la cantidad con la que vas a pagar: "))
        if pago >= pago - total:
            cambio = pago - total
            print(f"Pago realizado con exito: Tu cambio es: {cambio}")
            
            carrito = []
            total =0.0
        else:
            print("No tiene4s suficiente dineroparapagar.")
            
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccion una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_total()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            ver_total()
            print("Gracias por usar al POS, Hasta Luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
            
ejecutar()
           
