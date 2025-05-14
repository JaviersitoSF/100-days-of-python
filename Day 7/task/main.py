import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = r'''   mm   #                                      #        
   ##   # mm    mmm    m mm   mmm    mmm    mmm#   mmm  
  #  #  #"  #  #" "#   #"  " #"  "  "   #  #" "#  #" "# 
  #mm#  #   #  #   #   #     #      m"""#  #   #  #   # 
 #    # #   #  "#m#"   #     "#mm"  "mm"#  "#m##  "#m#"'''

print (logo)

word_list = [
    "casa", "arbol", "perro", "gato", "pez", "sol", "luna", "rio", "mar", "cielo",
    "pan", "leche", "agua", "carne", "fruta", "mesa", "silla", "cama", "puerta", "ventana",
    "libro", "papel", "lapiz", "pluma", "clase", "escuela", "juego", "canto", "baile", "salto",
    "rojo", "azul", "verde", "amarillo", "blanco", "negro", "gris", "rosa", "naranja", "morado",
    "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"
]
#probando git

lives=6
atino=False
used_letters=""
print (stages [lives])

chosen_word = random.choice(word_list)
#print(chosen_word)
#una forma mas pythonica de  placeholder
placeHolder=['_']*len(chosen_word)
print (f"La palabra tiene '{len(chosen_word)}' letras de largo\n" )
print (" ".join(placeHolder))
#print (placeHolder)

while "".join(placeHolder) != chosen_word and lives>0:
    print (" \n")
    #print (" ")
    guess = input("Guess a letter: ").lower()
    atino=False

    for position, letter in enumerate(chosen_word):
        if letter == guess:
            placeHolder[position] =guess
            atino=True
    if atino==True:
        print("--------* CORRECTO *--------")
    #print (stages[lives])
    print(" ".join(placeHolder))

    if atino==False:
        #check if guess is already used
        if guess in used_letters:
            print(stages[lives])
            print (f"--------* Incorrecto, ya has usado estas letras: '{used_letters}' *--------")

        else:
            lives -=1
            used_letters += guess
            print(stages[lives])
            print (f"incorrecto! te quita 1 vida, te quedan: {lives} ")
            print (f"--------*  has usado estas letras: '{used_letters}' *--------")

if lives==0:
    print (stages[lives])
    print (f"--------*Tu pierdes tienes ' {lives} ' vidas disponibles *--------")
    print (f"La palabra correcta era: '{chosen_word}'")
else:
    print (f"--------* Tu GANASTE y te quedaban  ' {lives} ' vidas disponibles *--------")
    print(f"Adivinaste la palabra correcta: '{chosen_word}'")


