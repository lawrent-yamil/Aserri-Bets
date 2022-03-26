apuesta = []
monto_Apuesta = []
print("""
        *******************
        |                 |
        |$Apuestas Aserrí$|
        |                 |
        *******************
    """)
while True:
    
    bet = str(input("Ingrese el número que quiere apostar: "))
    #si el rango de bet no esta entre 0 y 99 ejecutar otra cosa
    if bet.isdigit() and int(bet.isdigit()) and int(bet) >= 0 and int(bet) <= 99:
        try:
            monto = int(input("Ingrese el monto que quiere apostar: "))
        except ValueError:
            print("!DEBE SER UN NUMERO¡")
            continue
        apuesta.append(bet)
        monto_Apuesta.append(monto)
        print("Apuesta realizada con exito")
    else:
        print("Error, ingrese un número entre 0 y 99")
        continue
    print("\n")
    print("Apuesta: ", apuesta)
    print("Monto: ", monto_Apuesta)
    print("\n")
    print("Desea seguir apostando? (S/N)")
    print("\n")

    seguir = str(input("Desa continuar S para si o N para no: "))
    if seguir == "S" or seguir == "s" or seguir == "Si" or seguir == "si":
        continue
    else:
        break