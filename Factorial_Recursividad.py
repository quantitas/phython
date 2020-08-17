# Se define la función recursiva r_fact()
def r_fact(n):
  if n == 1:
	return n
  else:
  	return n*r_fact(n-1)

# Se pide el número
num = int(input("Introduce un número: "))

# Se comprueba si es negativo o 0 el número introducido
if num < 0:
	print("Número negativo")
elif num == 0:
	print("El factorial de 0 es 1")
else:
	print("El factorial de",num,"es",r_fact(num))