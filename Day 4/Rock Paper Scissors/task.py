import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

piedra=0
papel=1
tijeras=2

opcion= int(input ("Escoja 0 para Roca, 1 para Papel y 2 Tijeras "))
compu=random.randint(0,2)
if opcion==0:
    print("Roca")
    print(rock)
elif opcion==1:
    print ("Papel ")
    print (paper)
elif opcion==2:
    print ("Tijeras")
    print (scissors)
else:
    print( "opcion invalida corra el programa de nuevo")

#imprimir la seleccion de la compu
print ("La computadora escogio: ")
if compu==0:
    print("Roca")
    print(rock)
elif compu==1:
    print ("Papel ")
    print (paper)
elif compu==2:
    print ("Tijeras")
    print (scissors)

    #definir el ganador

if (compu==tijeras and opcion==tijeras) or (compu==papel and opcion==papel) or (compu==piedra and opcion==piedra):
    print ("Empate")
#compu gana cuando
elif (compu==piedra and opcion==tijeras) or (compu==tijeras and opcion==papel) or (compu==papel and opcion==piedra):
    print ("humano pierde!")
# humano gana cuando
elif  (opcion==tijeras and compu==papel) or (opcion==papel and compu==piedra) or (opcion==piedra and compu==tijeras):
    print ("Humano Gana!!")
else:
    print ("seleccion incorrecta, run otra vez")


