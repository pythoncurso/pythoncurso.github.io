#!/usr/bin/env python
# -*- coding: utf-8 -*-

POS_MIN = 0


def upheap(arreglo, posicion):
    """Dado un arreglo, lo ordena de manera que quede estructurado como un heap."""
    if not posicion:
        return
    pos_padre = (posicion-1)/2
    if arreglo[posicion] < arreglo[pos_padre]:
        aux = arreglo[pos_padre]
        arreglo[pos_padre] = arreglo[posicion]
        arreglo[posicion] = aux
        upheap(arreglo, pos_padre)

def downheap(arreglo, cant_elem, posicion):
    """Dado un arreglo, lo ordena de manera que quede estructurado como un heap."""
    if posicion >= cant_elem -1 :
        return
    pos_hijo_izq = (posicion*2) + 1
    pos_hijo_der = pos_hijo_izq + 1
    pos_padre = posicion
    if pos_hijo_izq < cant_elem and arreglo[pos_padre] > arreglo[pos_hijo_izq]:
        pos_padre = pos_hijo_izq
    if pos_hijo_der < cant_elem and arreglo[pos_padre] > arreglo[pos_hijo_der]:
        pos_padre = pos_hijo_der
    if pos_padre != posicion:
        aux = arreglo[pos_padre]
        arreglo[pos_padre] = arreglo[posicion]
        arreglo[posicion] = aux
        downheap(arreglo, cant_elem, pos_padre)

class MinHeap(object):
    """Estructura para almacenar datos que permite obtener siempre al menor de ellos."""
    def __init__(self):
        """Crea un arreglo vacio donde luego se guardaran los datos."""
        self.arreglo = []
        self.cant_elem = 0

    def encolar(self, elemento):
        """Agrega un elemento al heap de manera que quede ordenado con respecto a los otros."""
        self.arreglo.append(elemento)
        upheap(self.arreglo, self.cant_elem)
        self.cant_elem += 1

    def desencolar(self):
        """Elimina y devuelve el elemento mas chico en el heap."""
        if self.esta_vacio():
            return
        max = self.ver_min()
        self.arreglo[POS_MIN] = self.arreglo[self.cant_elem - 1]
        self.arreglo[self.cant_elem - 1] = max
        self.arreglo.pop(self.cant_elem-1)
        self.cant_elem -= 1
        downheap(self.arreglo, self.cant_elem, POS_MIN)
        return max

    def ver_min(self):
        """Devuelve el elemento mas chico en el heap."""
        return self.arreglo[POS_MIN]

    def esta_vacio(self):
        """Devuelve true o false dependiendo de si el heap tiene o no elementos."""
        return self.cant_elem == 0

    def ver_cantidad(self):
        """Devuelve la cantidad de elementos almacenados en el heap."""
        return self.cant_elem
