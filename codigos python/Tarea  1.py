#TAREA 1
"""
Usted desea simular un juego y para ello crea la función ESCALANDO que depende del número de intentos (N = 100), torpeza (T = 1) y tamaño del edificio (P = 60). Valores por defecto entre paréntesis. El juego consiste en tratar de subir por las escaleras al último piso de un edificio de P pisos empezando desde el lobby (piso 0), para ello:

Lanza un dado. Si sale 1 ó 2, baja un piso. Si sale 3, 4 ó 5, sube un piso. Si sale 6, vuelve a lanzar el dado y sube tantos pisos como indique el dado.
Tiene hasta N intentos de lanzar el dado para llegar al último piso
En cada intento, puede caer al primer piso con una probabilidad de T%
El edificio no tiene sótanos, por lo que no hay pisos negativos
La función devuelve a qué piso llego.
"""
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
from random import randint,random

def Escalando():
	n=1	
	p=0
	while n<=100:
		posibilidades=randint(1,6)
		if 0<posibilidades<=6:
			t=randint(1,100)
			if posibilidades==1 or posibilidades==2:
				n=n+1
				print("\033[92mNumero obtenido: \033[0m",posibilidades)
				if t==1:
					p=0
					print("\033[91mUps! te caiste \n ","Devuelta al lobby\033[0m")
				else:
					if p-1<0:
						p=0
					else:
						p=p-1
			elif posibilidades==3 or posibilidades==4 or posibilidades==5:
				n=n+1
				print("\033[92mNumero obtenido: \033[0m",posibilidades)
				if t==1:
					p=0
					print("\033[91mUps! te caiste \n ","Devuelta al lobby\033[0m")
				else:
					if p==60:
						p=p+0
					else:
						p=p+1
			elif posibilidades==6:
				n=n+1
				print("\033[92mNumero obtenido: \033[0m",posibilidades)
				if t==1:
					p=0
					print("\033[91mUps! se cayó \n ","De vuelta al lobby\033[0m")
				else:
					a=randint(1,6)
					print(" \033[93mTiro repetido:\033[0m ",a)
					if p+a>60:
						p=(p+a)-60
					else:
						p=p+a	
	print("Estas en el piso",p)
Escalando()







