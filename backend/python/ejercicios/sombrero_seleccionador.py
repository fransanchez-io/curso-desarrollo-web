gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print("Entras al salon de hogwarts y te hacen llamar al para que te sientes en medio de todos")
name= input("Hola, como te llamas?:  ")
print("Mucho gusto", name + "te voy a poner el Sombrero seleccionador y el te hara unas preguntas")


print(" el sombrero te pregunta ", name + " Que te gusta más?: \n1) El Amanecer \n2) El Atardecer ")

respuesta_1 = int(input("cual es tu respuesta: "))

if respuesta_1 == 1:
    gryffindor += 1
    ravenclaw +=1
elif respuesta_1 == 2:
    ravenclaw += 1
    slytherin +=1
else:
    print("Entrada incorrecta")

print(name + " Cuando mueras, como quieres que la gente me recuerde como: \n1) El Bueno/La Buena \n2) El Grande/La Grande \n3) El Sabio/La Sabia \n4) El Valiente/ La Valiente")
respuesta_2 = int(input("cual es tu respuesta: "))

if respuesta_2 == 1:
    hufflepuff += 2
elif respuesta_2 == 2:
    slytherin += 2
elif respuesta_2 == 3:
    ravenclaw += 2
elif respuesta_2 == 4:
    gryffindor += 2
else:
    print("Entrada incorrecta")

pregunta_3 = name + " Que instrumento te gusta más escuchar: \n1) El violin \n2) La trompeta \n3) El Piano \n4) El Tambor"
print(pregunta_3)
respuesta_3 = int(input("cual es tu respuesta: "))

if respuesta_2 == 1:
    slytherin += 2
elif respuesta_2 == 2:
    hufflepuff += 2
elif respuesta_2 == 3:
    ravenclaw += 2
elif respuesta_2 == 4:
    gryffindor += 2
else:
    print("Entrada incorrecta")

print("El sombrero piensa y grita: ")
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('Tu casa es 🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('Tu casa es 🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
  print('Tu casa es 🦡 Hufflepuff!')
else:
  print('Tu casa es 🐍 Slytherin!')