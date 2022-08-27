#Función para asegurar que la respuesta esté dentro del rango de opciones
def verif(Rusuario):

#Función para comprobar si la respuesta es correcta
def cali(Rusuario,Rcorrecta):
	if Rusuario == Rcorrecta:
		print("Respuesta Correcta")
		return 1
	else:
		print("ups, creo que te confundiste, tu respuesta es incorrecta")
		print("tristemente la respuesta correcta era el inciso:", Rcorrecta)
		return 0

#Preguntas de química

#Para que una molecula sea polar debe tener una diferencia de _________ en un rango de ___________
#Para poder calcular la presión, volumen, numero de moles, etc se debe tener la temperatura en un sistema distinto, ¿Cuál?
# - Como pasas de este sistema a Celsius?