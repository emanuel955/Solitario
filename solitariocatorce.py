from mesa import *
from mazo import*

class SolitarioCatorce:
    """Interfaz para implementar un solitario."""

    def __init__(self, mesa):
        """Inicializa con una mesa creada y vacía."""
        self.mesa=mesa

    def armar(self):
        """Arma el tablero con la configuración inicial."""
        self.mesa.mazo=crear_mazo()

        for i in range (12):
            self.mesa.pilas_tablero.append(PilaCartas(pila_visible=True))
        i=0
        while not self.mesa.mazo.es_vacia():
            carta=self.mesa.mazo.desapilar()
            carta.voltear()
            self.mesa.pilas_tablero[i%12].apilar(carta)
            i+=1

    def termino(self):
        """Avisa si el juego se terminó."""
        for pila in self.mesa.pilas_tablero:
            if not pila.es_vacia():
                return False
        return True     

    def jugar(self, jugada):
        """Efectúa una movida.
            La jugada es una lista de pares (PILA, numero). (Ver mesa.)
            Si no puede realizarse la jugada se levanta una excepción SolitarioError *descriptiva*."""
        j0, p0 = jugada[0]
        j1, p1 = jugada[1] if len(jugada) == 2 else (SALIR, 0)
        pila_a=self.mesa.pilas_tablero[p0]
        pila_b=self.mesa.pilas_tablero[p1]
        if  not pila_a.es_vacia() and not pila_b.es_vacia() and pila_a.tope().valor+pila_b.tope().valor==14:
            pila_a.desapilar()
            pila_b.desapilar()
        else:
            raise SolitarioError('Movimiento invalido')
