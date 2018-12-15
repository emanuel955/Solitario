NUMERO_FINAL= 13

from mesa import *
from mazo import *

    
class SolitarioClasico:
    """Interfaz para implementar un solitario."""

    def __init__(self, mesa):
        """Inicializa con una mesa creada y vacía."""
        self.mesa=mesa

    def armar(self):
        """Arma el tablero con la configuración inicial."""
        self.mesa.mazo=crear_mazo()
        print(self.mesa.mazo.es_vacia())
        for i in range(4):
            self.mesa.pilas_tablero.append(PilaCartas(criterio_apilar=criterio(palo=DISTINTO_COLOR, orden=DESCENDENTE),
                criterio_mover=criterio(palo=DISTINTO_COLOR, orden=DESCENDENTE), pila_visible=True))
            self.mesa.pilas_tablero[i].apilar(self.mesa.mazo.desapilar())
            self.mesa.pilas_tablero[i].tope().voltear()
        
        for i in range(4):
            self.mesa.fundaciones.append(PilaCartas(valor_inicial=1, criterio_apilar=criterio(palo=MISMO_PALO, orden=ASCENDENTE)))

        self.mesa.descarte=PilaCartas()

    def termino(self):
        """Avisa si el juego se terminó."""
        for fundacion in self.mesa.fundaciones:
            if fundacion.es_vacia() or fundacion.tope().valor!=NUMERO_FINAL:
                return False
        return True

    def jugar(self, jugada): #utilizar alguna funcion auxiliar, quedo demasiado larga y se hace complicado el seguimiento (es la correccion mas importante)
        """Efectúa una movida.
            La jugada es una lista de pares (PILA, numero). (Ver mesa.)
            Si no puede realizarse la jugada se levanta una excepción SolitarioError *descriptiva*."""
        j0, p0 = jugada[0]
        j1, p1 = jugada[1] if len(jugada) == 2 else (SALIR, 0)


        self.auxiliar_jugar(len(jugada), j0, p0, j1, p1)             


    def _carta_a_pila(self, origen, destino):
        """Mueve la carta del tope entre un origen y un destino, si se puede, levanta SolitarioError si no."""
        if origen.es_vacia():
            raise SolitarioError("La pila está vacía")

        destino.apilar(origen.tope())
        origen.desapilar()

        if origen in self.mesa.pilas_tablero and not origen.es_vacia() and origen.tope().boca_abajo:
            origen.tope().voltear()

    def _subpila_a_pila(self, origen, destino):
        """Mueve un subpilon de cartas de origen a destino si se puede, levanta SolitarioError si no"""
        if origen.es_vacia():
            raise SolitarioError("El origen está vacío")
        
        destino.mover(origen)

        if not origen.es_vacia() and origen.tope().boca_abajo:
            origen.tope().voltear()

    def renovar_mazo(self):
        '''Vuelve a armar el mazo con las cartas del descarte'''
        while not self.mesa.descarte.es_vacia():
            carta=self.mesa.descarte.desapilar()
            carta.voltear()
            self.mesa.mazo.apilar(carta)


    def auxiliar_jugar(self, len_jugada, j0, p0, j1, p1):
        origen = self.mesa.pilas_tablero[p0] if j0 == PILA_TABLERO else self.mesa.fundaciones[p0] if j0 == FUNDACION else self.mesa.descarte

        if len_jugada==1:

            if j0==MAZO:
                if self.mesa.mazo.es_vacia():
                    self.renovar_mazo()
                self.mesa.descarte.apilar(self.mesa.mazo.desapilar())
                self.mesa.descarte.tope().voltear()
            else:
                for fundacion in self.mesa.fundaciones:
                    try:
                        self._carta_a_pila(origen, fundacion)
                        return
                    except SolitarioError:
                        pass
                raise SolitarioError("No puede moverse esa carta a la fundación")
        else:

            destino = self.mesa.pilas_tablero[p1] if j1==PILA_TABLERO  else self.mesa.fundaciones[p1]
            if origen == self.mesa.fundaciones[p0] and origen == self.mesa.fundaciones[p1]:
                raise SolitarioError('No se puede mover de una fundacion a otra.')
            elif origen in self.mesa.pilas_tablero and destino in self.mesa.pilas_tablero:
                self._subpila_a_pila(origen,destino)
            else:
                self._carta_a_pila(origen, destino)

