
n=1	
p=0

from random import randint, uniform,random


#manual
"""
while n<=10:
	posibilidades=int(input("Número obtenido: "))
	if 0<posibilidades<=6:
		if posibilidades==1 or posibilidades==2:
			n=n+1
			t=randint(1,10)
			if t==1:
				p=0
				print("Ups! te caiste \n ","Regresas al lobby")
			else:
				if p-1<0:
					p=0
				else:
					p=p-1
		elif posibilidades==3 or posibilidades==4 or posibilidades==5:
			n=n+1
			t=randint(1,100)
			if t==1:
				p=0
				print("Ups! te caiste \n ","Regresas al lobby")
			else:
				if p==60:
					p=p+0
				else:
					p=p+1
		elif posibilidades==6:
			n=n+1
			t=randint(1,100)
			if t==1:
				p=0
				print("Ups! te caiste \n ","Regresas al lobby")
			else:
				a=int(input("Tira de nuevo: "))
				if p+a>60:
					p=(p+a)-60
				else:
					p=p+a
	else:	
		print("Vuelve a intentarlo: ")
print("Estas en piso: ",p)
"""




	
		
#automatico

while n<=100:
	posibilidades=randint(1,6)
	if 0<posibilidades<=6:
		t=randint(1,100)
		if posibilidades==1 or posibilidades==2:
			n=n+1
			print("Numero obtenido: ",posibilidades)
			if t==1:
				p=0
				print("Ups! te caiste \n ","Devuelta al lobby")
			else:
				if p-1<0:
					p=0
				else:
					p=p-1
		elif posibilidades==3 or posibilidades==4 or posibilidades==5:
			n=n+1
			print("Numero obtenido: ",posibilidades)
			if t==1:
				p=0
				print("Ups! te caiste \n ","Devuelta al lobby")
			else:
				if p==60:
					p=p+0
				else:
					p=p+1
		elif posibilidades==6:
			n=n+1
			print("Numero obtenido: ",posibilidades)
			if t==1:
				p=0
				print("Ups! se cayó \n ","De vuelta al lobby")
			else:
				a=randint(1,6)
				print(" Tiro repetido: ",a)
				if p+a>60:
					p=(p+a)-60
				else:
					p=p+a	
print("Estas en piso: ",p)



