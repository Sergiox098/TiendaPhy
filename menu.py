print("                 Bienvenido a la tienda Phyton\n                  ¡Tenemos nuevos descuentos!\n")
print("Sí compras 5 elementos iguales te damos un descuento del 5%"" a esos 5 elementos")
print("Sí compras 10 elementos iguales te damos un descuento del 10%"" a esos 10 elementos")
print("Sí compras 20 elementos iguales te damos un descuento del 20%"" a esos 20 elementos\n")
print("                         Tienda Phyton")
print("1. Gaseosa: $2000\n2. Galletas: $1000\n3. Botella de Agua: $500\n4. Chocorramo: $2500\n5. Empanada: $3000")
gaseosa=2000
gase=0
galletas=1000
galle=0
agua=500
ag=0
chocoramo=2500
choco=0
empanada=3000
empa=0
def fac(x,y):
    factura=(x*y)
    return factura
def fac5(x,y):
    factura=(x*y)-(x*y)*0.05
    return factura
def fac10(x,y):
    factura=(x*y)-(x*y)*0.1
    return factura
def fac20(x,y):
    factura=(x*y)-(x*y)*0.2
    return factura
def carrito(x,y,z,a,b):
    if(x>0):
        print("Compraste",x,"gaseosas")
    if(y>0):
        print("Compraste",y,"galletas")
    if(z>0):
        print("Compraste",z,"botellas de agua")
    if(a>0):
        print("Compraste",a,"chocoramos")
    if(b>0):
        print("Compraste",b,"empanadas")
facturatotal=0
salir=1
while(salir==1):
    produ=int(input("Seleccione el producto que deseas comprar: "))
    if(produ == 1):
        cant=int(input("¿Qué cantidad de gaseosas deseas comprar?: "))
        gase=gase+cant
        if(cant>=5 and cant<10):
            print("¡Obtuviste un descuento del 5%!")
            facturatotal=facturatotal+fac5(gaseosa,cant)
        if(cant>=10 and cant<20):
            print("¡Obtuviste un descuento del 10%!")
            facturatotal=facturatotal+fac10(gaseosa,cant)
        if(cant>=20):
            print("¡Obtuviste un descuento del 20%!")
            facturatotal=facturatotal+fac20(gaseosa,cant)
        if (cant<5):
            facturatotal=facturatotal+fac(gaseosa,cant)
    if(produ == 2):
        cant=int(input("¿Qué cantidad de galletas deseas comprar?: "))
        galle=galle+cant
        if(cant>=5 and cant<10):
            print("¡Obtuviste un descuento del 5%!")
            facturatotal=facturatotal+fac5(galletas,cant)
        if(cant>=10 and cant<20):
            print("¡Obtuviste un descuento del 10%!")
            facturatotal=facturatotal+fac10(galletas,cant)
        if(cant>=20):
            print("¡Obtuviste un descuento del 20%!")
            facturatotal=facturatotal+fac20(galletas,cant)
        if(cant<5):
            facturatotal=facturatotal+fac(galletas,cant)
    if(produ == 3):
        cant=int(input("¿Qué cantidad de botellas de agua deseas comprar?: "))
        ag=ag+cant
        if(cant>=5 and cant<10):
            print("¡Obtuviste un descuento del 5%!")
            facturatotal=facturatotal+fac5(agua,cant)
        if(cant>=10 and cant<20):
            print("¡Obtuviste un descuento del 10%!")
            facturatotal=facturatotal+fac10(agua,cant)
        if(cant>=20):
            print("¡Obtuviste un descuento del 20%!")
            facturatotal=facturatotal+fac20(agua,cant)
        if(cant<5):
            facturatotal=facturatotal+fac(agua,cant)
    if(produ == 4):
        cant=int(input("¿Qué cantidad de chocoramos deseas comprar?: "))
        choco=choco+cant
        if(cant>=5 and cant<10):
            print("¡Obtuviste un descuento del 5%!")
            facturatotal=facturatotal+fac5(chocoramo,cant)
        if(cant>=10 and cant<20):
            print("¡Obtuviste un descuento del 10%!")
            facturatotal=facturatotal+fac10(chocoramo,cant)
        if(cant>=20):
            print("¡Obtuviste un descuento del 20%!")
            facturatotal=facturatotal+fac20(chocoramo,cant)
        if(cant<5):
            facturatotal=facturatotal+fac(chocoramo,cant)
    if(produ == 5):
        cant=int(input("¿Qué cantidad de empanadas deseas comprar?: "))
        empa=empa+cant
        if(cant>=5 and cant<10):
            print("¡Obtuviste un descuento del 5%!")
            facturatotal=facturatotal+fac5(empanada,cant)
        if(cant>=10 and cant<20):
            print("¡Obtuviste un descuento del 10%!")
            facturatotal=facturatotal+fac10(empanada,cant)
        if(cant>=20):
            print("¡Obtuviste un descuento del 20%!")
            facturatotal=facturatotal+fac20(empanada,cant)
        if(cant<5):
            facturatotal=facturatotal+fac(empanada,cant)
    salir=int(input("\n¿Quieres comprar algo más?\n1. Sí \n0. No "))
print("\n")
print(carrito(gase,galle,ag,choco,empa))
print ("Gracias por tu compra, tu factura fue de:",facturatotal )