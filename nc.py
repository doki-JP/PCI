#Bienvenida al usuario
print("===================¿Qué tanto sabes de química?===================\n")
print("☺ Bienvenid@ al programa! ☺\n")
print("Este es un cuestionario acerca de algunos conceptos de química, a ver si puedes sacar 100\n")

#Función para verificar sí la respuesta esta dentro del rango.
def corrector(entrada):
  entrada = entrada.lower()
  opciones = ["a","b","c","d"]
  while opciones.count(entrada) == 0:
    print("\n=====================*ERROR*=====================\nTu respuesta esta fuera del rango o no es válida\nRecuerda que solo se aceptan valores de:a, b, c, d\n-----------------INTENTE DE NUEVO-----------------\n")
    entrada = input("»» ")
    entrada = entrada.lower()
  return entrada

#Función para verificar sí la respuesta es correcta
def resultado(entrada, correcta):
  if entrada == correcta:
    print("√ ¡Correcto!") 
    return 1
  else:
    print("x Incorrecto D:")
    print("La respuesta correcta es la:", correcta) 
    return 0

#Variable Contador
contador = 0

#Pregunta 1

print("1. ¿Qué compuesto cuenta con puentes de hidrógeno?\nOpciones:")
print("\ta) NaCl")
print("\tb) H2O")# Respuesta correcta
print("\tc) Fe")
print("\td) Todos los compuestos con hidrógeno")
respuestaUsuario = input("\n»» ")
contador += resultado(corrector(respuestaUsuario), "b")
print("\nSiguiente pregunta...\n")

#Pregunta 2

print("2. ¿Cuantos electrones de valencia tiene el Xenon?\nOpciones:")
print("\ta) 8")# Respuesta correcta
print("\tb) 7")
print("\tc) 2")
print("\td) 1")
respuestaUsuario = input("\n»» ")
contador += resultado(corrector(respuestaUsuario), "a")
print("\nSiguiente pregunta...\n")

#Pregunta 3
print("3. ¿Para que una molécula sea POLAR debe tener una diferencia de _________ en un rango de __________\n Opciones:")
print("\ta) Electronegatividad, más de 1.7")
print("\tb) Electrones de valencia, 6 a 7")
print("\tc) Afinidad electrónica, 0.4 a 1.7") # Respuesta correcta
print("\td) Electronegatividad, menos de 0.4")
respuestaUsuario = input("\n»» ")
contador += resultado(corrector(respuestaUsuario), "c")
print("\nSiguiente pregunta...\n")

#Pregunta 4
print("4. Para poder calcular la presión, volumen, numero de moles, etc se debe tener la temperatura en un sistema distinto, \n¿Cuál?\n Opciones:")
print("\ta) Fahrenheit")
print("\tb) Rankine")
print("\tc) Réamur") 
print("\td) Kelvin") # Respuesta correcta
respuestaUsuario = input("\n»» ")
contador += resultado(corrector(respuestaUsuario), "d")
print("\nSiguiente pregunta...\n")

#Pregunta 5
print("5. Cuál es la conversión de Celsius a este sistema?\nOpciones:")
print("\ta) °C - 79.4")
print("\tb) Ra * 0.12")
print("\tc) °C + 273.15") # Respuesta correcta
print("\td) Kelvin - °C") 
respuestaUsuario = input("\n»» ")
contador += resultado(corrector(respuestaUsuario), "c")
print("\nSiguiente pregunta...\n")
