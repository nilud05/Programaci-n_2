import random
import sys
saldo=0
print("!BIENVENIDO A MI MAQUINITA VIRTUAL¡")
print("Disfruta El Juego")
saldo=int(input("Cuanto saldo le agregaras?:" ))
saldo1= saldo-40
print(f"el precio de la maquinita es de 40 y te quedan {saldo1}")
print("----------")
print("SOLO SE GANA SI LOGRAS SACAR DOBLE 3 O DOBLE 5")
print("----------")


while saldo1>10:
    r1 = random.randint(0,7)
    print(r1)
    r2 = random.randint(0,7)
    print(r2)
    r3 = random.randint(0,7)
    print(r3)
    if (r1==3 and r2==3 and r3==3) or (r1==5 and r2==5 and r3==5):
       print("!Ganaste 200¡")
       saldo1 += 200
       print(f"Tu saldo actual es de {saldo1}")
    else:
        print("PERDISTE :c")
        saldo1 -= 40
        print(f"Tu saldo actual es de {saldo1}")

    opcion = int(input("¿Seguir jugando?: 1.SI /// 2.NO: "))
    if opcion != 1:
        sys.exit()
    
    if saldo1 == 40:
        print("Te has quedado sin saldo para seguir jugando. ¡Gracias por jugar!")
        sys.exit()