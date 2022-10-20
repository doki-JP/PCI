"""Función de verificación, verifica que la respuesta esté dentro de los intervalos necesarios"""
def corrector(entrada):
  entrada = entrada.lower()
  opciones = ["a","b","c","d"]
  while opciones.count(entrada) == 0:
    print("\n=====================*ERROR*=====================\nTu respuesta esta fuera del rango o no es válida\nRecuerda que solo se aceptan valores de:a, b, c, d\n-----------------INTENTE DE NUEVO-----------------\n")
    entrada = input("»» ")
    entrada = entrada.lower()
  return entrada

"""Función calificadora, compara dos variables y determinar si esta correcta o no(+1 o +0)"""
def resultado(entrada, correcta):
  if entrada == correcta:
    print("√ ¡Correcto!") 
    return 1
  else:
    print("x Incorrecto D:")
    return 0

"""Función 'graciosa', muestra un mensaje a partir del intervalo de la calificación"""
def calf(contador):
	if contador >80:
		print('Felicidades, tu dominio acerca del tema es algo que temer, no puedo enseñarte nada más')
	elif contador <=80 and contador>59:
		print('Definitivamente se puede mejorar. La próxima vez espero y sea un 100')
	elif contador <=60 and contador>25:
		print('Hay que echarle más ganitas, estudiale una vez más e intentalo de nuevo')
	else:
		print("No por mala onda o así, pero...\n¿si pusiste atención o que pasa?")

"""Funcion del cuestionario en sí, recibe una respuesta y enseña las preguntas"""
def cuest():
	"""Variable contador (contador) y matriz (preguntas, respuesta,opciones)"""
	contador=0
	l_preg= [["1. ¿Qué compuesto cuenta con puentes de hidrógeno?\nOpciones:","2. ¿Cuantos electrones de valencia tiene el Xenon?\nOpciones:","3. ¿Para que una molécula sea POLAR debe tener una diferencia de _________ en un rango de __________\n Opciones:"\
	,"4. Para poder calcular la presión, volumen, numero de moles, etc se debe tener la temperatura en un sistema distinto, \n¿Cuál?\n Opciones:","5. Cuál es la conversión de Celsius a este sistema?\nOpciones:"],["b",'a','c','d','c'],\
	[["a) NaCl","b) H2O","c) Fe","d) Todos los compuestos con hidrógeno"],["a) 8","b) 7","c) 2","d) 1"],["a) Electronegatividad, más de 1.7","b) Electrones de valencia, 6 a 7","c) Afinidad electrónica, 0.4 a 1.7","d) Electronegatividad, menos de 0.4"]\
	,["a) Fahrenheit","b) Rankine","c) Réamur","d) Kelvin"],["a) °C - 79.4","b) Ra * 0.12","c) °C + 273.15","d) Kelvin - °C"]]]
	for x in range(len(l_preg[0])):
		print(l_preg[0][x],l_preg[2][x])
		Ru=input("\n»»>")				
		contador+=resultado(corrector(Ru),l_preg[1][x])
	
	contador = contador / len(l_preg[2])
	contador = contador * 100
	print('Su calificación es de:',contador,'puntos')
	calf(contador)
	nom= input("Me puedes dar tu nombre? (se utiliza para la sección de puntajes ;)\n")
	punt(nom, contador)


"""Funcion de menú, imprime de acuerdo a la función que elijas"""
def menu():
	print("===================¿Qué tanto sabes de química?===================\n")
	print("☺ Bienvenid@ al programa! ☺\n")
	print("Este es un cuestionario acerca de algunos conceptos de química, a ver si puedes sacar 100\n")
	print("selecciona una de estas opciones por favor:\n(1)Iniciar Quiz\n(2)Ver Puntuaciones\n(3)Créditos\n(4) Salir\n")
	op=int(input())
	while op<5 and op>0:
		if op==1:
			cuest()
			op=int(input("selecciona una de estas opciones por favor:\n(1)Iniciar Quiz\n(2)Ver Puntuaciones\n(3)Créditos\n(4) Salir\n"))
		elif op==2:
			Vpunt()
			op=int(input("selecciona una de estas opciones por favor:\n(1)Iniciar Quiz\n(2)Ver Puntuaciones\n(3)Créditos\n(4) Salir\n"))
		elif op==3:
			print("Este código fue hecho por el estudiante que lo entregó\n (no sabía si poner mi nombre por lo de la privacidad de GitHub\n")
			op=int(input("selecciona una de estas opciones por favor:\n(1)Iniciar Quiz\n(2)Ver Puntuaciones\n(3)Créditos\n(4) Salir\n"))
		elif op==4:
			print("gracias por usar este código, hasta pronto")
			break
		
"""Función que añade la puntuación de los usuarios en el puntaje, accede al documento y lo edita (append)"""
def punt(nom, contador):
	file = open("puntaje.txt", "a")
	nom.upper()
	contador=str(contador)
	file.write(nom+ " ---> "+ contador+"\n")
	file.close()

"""Función para imprimir los puntajes, accede al documento y lo imprime"""
def Vpunt():
	file=open("puntaje.txt", "r")
	p =file.read()
	print(p)
	file.close()

"""Función main"""
def main():
	menu()

"""Ejecución de todo el código"""
main()
