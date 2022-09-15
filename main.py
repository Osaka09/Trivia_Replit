#descargamos el pquete de getkey en shell con la sentencia: pip install getkey
from getkey import getkey, keys
import random
import time

prg1Extr="La primera edición de la Copa Mundial de Fútbol organizada por la FIFA tuvo lugar en 1930, concretamente en Uruguay entre el 13 y el 30 de julio de este año, con motivo del centenario de la Jura de la Constitución de Uruguay. Participaron 13 selecciones\n"
prg2Extr="El máximo goleador de la historia de la Copa Mundial de Fútbol es Miroslav Klose. En 2014 marcó su gol número 16, lo que le convirtió en el primero de la lista, desbancando a Ronaldo con 15.\n"
prg3Extr="Se llama Zabivaka y fue la mascota del Mundial creada por Ekaterina Bocharova. Se trata de un simpático lobito antropomórfico que lleva gafas.\n"

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

sol_lst=["b","a","c"]
rpta1=[]
rpta2=[]
rpta3=[]
score_lst=[]
iniciar_trivia=True
intentos=0
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia

print ("¿Te consideras un experto de la historia del fútbol?")
print ("Veamos cuántos puntos obtienes demostrando tus conocimientos con esta trivia")

nombre=input("Ingresa tu nombre aquí: ")
while nombre=="":
  nombre=input(RED+"Campo obligatorio, escribe un nombre válido por favor"+RESET+"\n\nIngresa tu nombre aquí: ")
print("")
# Es importante dar instrucciones sobre cómo jugar:
while iniciar_trivia==True:
  intentos+=1
  #inicializamos puntaje
  puntaje=random.randint(0,11)

  puntos_facil=random.randint(1,10)

  puntos_dificil=random.randint(10,40)

  puntos_loco=random.randint(1000,4000)
  
  print("\nIntento número:", intentos)
  print (YELLOW+"Hola", nombre+"! Responde las siguientes preguntas sobre los mundiales de fútbol escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta\n"+RESET)
  time.sleep(1)
  print(BLUE+"Empezarás con", puntaje,"puntos\n"+RESET)
  time.sleep(1)
  print("¿Estás list@?, ¡dale enter para empezar!\n")
# OJO, el \n al final de la línea 6 es para dar un "salto de línea"
  pressed_key=getkey()
  while pressed_key!=keys.ENTER:
    pressed_key=getkey()
  for i in range(1,6,1):
    print(i)
    time.sleep(1)
  # Pregunta 1
  print (YELLOW+"Pregunta 1:\n¿En qué Año se dio la primera   Copa Mundial de Fútbol?"+RESET)
  print ("a) 1290")
  print ("b) 1930")
  print ("c) 1940")
  print ("d) 1950")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")

  while respuesta_1 not in ("a", "b", "c", "d", "x"):
    respuesta_1 = input(RED+"Debes responder a, b, c o d.   Ingresa nuevamente tu respuesta: "+RESET)
  time.sleep(1)
  rpta1.append(respuesta_1)
  if respuesta_1=="b":
    puntaje+=puntos_facil
    print("")
    print(GREEN+"Respuesta correcta",nombre,"ganas ",puntos_facil, " puntos!\n\n"+RESET,prg1Extr)
  elif respuesta_1=="x":
    puntaje +=puntos_loco
    print("")
    print(YELLOW+"Respuesta secreta ganas ",puntos_loco," puntos!!\n"+RESET)
  else:
    puntaje -=puntos_facil
    print("")
    print(RED+"Respuesta incorrecta",nombre,"pierdes ",puntos_facil," puntos :(\n\n"+RESET,prg1Extr)
  print(BLUE+"Tienes acumulado", puntaje, "puntos\n"+RESET)
  print("Presione la barra espaciadora para pasar a la siguiente pregunta!")
  pressed_key=getkey()
  while pressed_key!=keys.SPACE:
    pressed_key=getkey()
  print("")

# Pregunta 2
  print (YELLOW+"Pregunta 2:\n¿Quién es el máximo goleador de la historia de la Copa Mundial de Fútbol?"+RESET)
  print ("a) Miroslav Klose")
  print ("b) Ronaldo Nazario")
  print ("c) Gerd Muller")
  print ("d) Pelé")

  respuesta_2 = input("\nTu respuesta: ")

  while respuesta_2 not in ("a", "b", "c", "d", "w"):
    respuesta_2 = input(RED+"Debes responder a, b, c o d.   Ingresa nuevamente tu respuesta: "+RESET)
  time.sleep(1)
  rpta2.append(respuesta_2)
  if respuesta_2=="a":
    print("")
    puntaje += puntos_dificil
    print(GREEN+"Respuesta correcta",nombre,"ganas ",puntos_loco," puntos!\n\n"+RESET,prg2Extr)
  elif respuesta_2=="w":
    puntaje -=puntos_loco 
    print("")
    print(YELLOW+"Respuesta secreta pierdes ",puntos_loco," puntos xD!!\n"+RESET) 
  else:
    print("")
    puntaje -=puntos_dificil
    print(RED+"Respuesta incorrecta",nombre,"pierdes ",puntos_dificil," puntos :(\n\n"+RESET,prg2Extr)
  print(BLUE+"Tienes acumulado",   puntaje,"puntos\n"+RESET,RED+"Se viene la pregunta mas dificil"+RESET)
  print("Presione la barra espaciadora para pasar a la siguiente pregunta!")
  pressed_key=getkey()
  while pressed_key!=keys.SPACE:
    pressed_key=getkey()
  print("")

# Pregunta 3
  print (YELLOW+"Pregunta 3:\n¿Qué animal fue el escogido para ilustrar la mascota del Mundial de Rusia?"+RESET)
  print ("a) Un perro")
  print ("b) Un gato")
  print ("c) Un lobo")
  print ("d) Un loro")
  respuesta_3 = input("\nTu respuesta: ")

  while respuesta_3 not in ("a", "b", "c", "d", "f"):
    respuesta_3 = input(RED+"Debes responder a, b, c o d.   Ingresa nuevamente tu respuesta: "+RESET)
  time.sleep(1)
  rpta3.append(respuesta_3)
  if respuesta_3=="c":
    print("")
    puntaje *=puntos_dificil
    print(GREEN+"Respuesta correcta",nombre,"ganas ",puntos_dificil," puntos!\n\n"+RESET,prg3Extr)
  elif respuesta_3=="f":
    puntaje *=puntos_loco
    print("")
    print(YELLOW+"Respuesta secreta ganas ",puntos_loco, " puntos xD!!\n"+RESET)
  else:
    print("")
    puntaje /=puntos_dificil
    print(RED+"Respuesta incorrecta",nombre,"pierdes ",puntos_dificil," puntos :(\n\n"+RESET,prg3Extr)
  score_lst.append(puntaje)
  time.sleep(1)
  print(YELLOW+"Gracias por jugar la trivia, Tu puntaje final es:\n")
  for i in random.sample(range(0,2200),10):
    print(i)
    time.sleep(1)
  print(RESET,GREEN+"PUNTAJE: ",puntaje, "PUNTOS\nFelicitaciones!"+RESET)
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia!="si":
    print("\nReporte de intentos\n")
    print("respuesta correcta: "+sol_lst[0]+sol_lst[1]+sol_lst[2]+"\n")
    for i in range(0,intentos):
      print("\nintento",i+1,":\n")
      
      if rpta1[i]==sol_lst[0]:
        print("respuesta 1->",rpta1[i],"✓")
      else:print("respuesta 1->",rpta1[i],"×")
      if rpta2[i]==sol_lst[1]:
        print("\nrespuesta 2->",rpta2[i],"✓")
      else:print("\nrespuesta 2->",rpta2[i],"×")
      if rpta3[i]==sol_lst[2]:
        print("\nrespuesta 3->",rpta3[i],"✓")
      else:print("\nrespuesta 3->",rpta3[i],"×")
      
#      print("respuesta 1->",rpta1[i],"\nrespuesta 2->",rpta2[i],"\nrespuesta 3->",rpta3[i])

    print("\nEspero",nombre,"que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia=False


