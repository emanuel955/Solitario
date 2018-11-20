from pila_cartas import *
import random

def crear_mazo(mazos=1, palos=4):
    """Devuelve una PilaCartas con las cartas boca abajo y mezcladas.
    Cada mazo de los mazos tiene 52 cartas, y puede ser completado con 1, 2 o 4 palos.
    En caso de que estén los 4 palos el mazo se conformará con la serie del 1 al 13
    para cada uno de ellos, en caso de ser sólo 2 palos serán 2 veces la serie 1 al 13
    para dos palos del mismo color y en caso de ser 1 sólo palo será 4 veces la serie 1 al 13
    para ese palo."""
    mazos_tot=PilaCartas()
    for cant in range(mazos):
    	if palos==3:
    		raise SolitarioError
    	elif palos==1:
    		palo=random.choice([0,1,2,3])
    		for cant in range(4):
    			mazo_individual(mazos_tot,palo)
    	elif palos==2:
    		while True:
    			palo1=random.choice[0,1,2,3]
    			palo2=random.choice[0,1,2,3]
    			if palo1!=palo2 and cond(palo1,palo2):
    				break
    		for palo in range(2):
    			mazo_individual(mazos_tot,palo1)
    			mazo_individual(mazos_tot, palo2)
    	else:
    		for palo in range(4):
    			mazo_individual(mazos_tot, palo)
    random.shuffle(mazos_tot.pila)
    return mazos_tot


def mazo_individual(mazos, palo):
    '''Agrega 13 cartas a un mazo del palo que se pase por parametro.'''
    for valor in range(1,14):
        mazos.apilar(Carta(valor, palo))

def cond(palo1, palo2):
    '''Verifica que los palos que se ingresen por parametro sean del mismo color.
    Devuelve un valor booleano.'''
    if palo1==0 and palo2==3 or palo1==3 and palo2==0:
        return True
    elif palo1==1 and palo2==2 or palo1==2 and palo2==1:
        return True
    return False