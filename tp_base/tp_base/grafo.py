#!/usr/bin/env python
# -*- coding: utf-8 -*-
from heap import MinHeap as Heap

"""Constantes"""
POS_INI = 0

def GenerarCamino(padre,origen,destino):
    """Funcion Auxiliar que genera un camino"""
    camino = []
    camino.insert(POS_INI, destino)
    while origen != destino:
        camino.insert(POS_INI, padre[destino])
        destino = padre[destino]
    return camino

class DatoVertice(object):
    """Representa el conjunto de datos de un vertice para generar un camino"""

    def __init__(self,vertice,peso):
        """Inicializador recibe el nombre y el peso hasta ese vertice"""
        self.vertice = vertice
        self.peso = peso

    def __cmp__(self,otro):
        """Funcion de comparacion"""
        return self.peso - otro.peso

    def ObtenerVertice(self):
        """"Devuelve una tupla con los datos"""
        return (self.vertice,self.peso)


""" 
Implementar clase Vertice.
Los vertices deben contar con un identificador, un valor (que representa lo que se desea guardar),
y con un diccionario con las aristas con las que está conectado.
"""
class Vertice(object):
    """Representa un Vertice de un Grafo"""

    """
    Implementar un constructor que cuente con un identificador, el valor del vertice y con 
    un diccionario con las aristas con las que conecta.
    """
    def __init__(self,identificador,valor):
        """Inicializador recibe un identificador y el valor del Vertice.
        Inicializa al Vertice con los parámetros especificados, y con un diccionario vacío de 
        aristas.
        """
        pass

    """
    Implementar un comparador que compare dos vertices segun su indice:
        If id1 > id2 -> 1
        If id1 < id2 -> -1
        Else -> 0
    """
    def __cmp__(self,otro):
        """Funcion de comparacion"""
        pass    

    """
    Implementar una función Valor que devuelva el valor almacenado en el Vertice.
    Extra: Reemplazar esta función por una property 
    (CUIDADO con los lugares en donde es usada).
    """
    def Valor(self):
        """Devuelve el valor que se encuentra en el vertice"""
        pass

    """
    Implementar una función Vecinos que devuelva el diccionario de aristas a los vecinos.
    Extra: Idem anterior.
    """
    def Vecinos(self):
        """Devuelve un Hash con todos las aristas con las que conecta el vertice"""
        pass

    """
    Implementar una función id que devuelva el id del Vertice.
    Extra: Idem anteriores.
    """    
    def id(self):
        """Devuelve el identificador del vertice"""
        pass


""" 
Implementar clase Arista.
Las aristas deben contar el identificador del vertice de origen, el identificador del vertice de 
destino y el peso de la misma.
"""

class Arista(object):
    """Representa una arista que une a dos vertices"""

    """
    Implementar un constructor que cuente con un id de origen, un id de destino y un peso.
    """
    def __init__(self,origen,destino,peso = None):
        """Inicializador recibe un id de origen, un id de destino y opcionalmente un peso.
        Inicializa a la Arista con los parámetros especificados.
        """
        pass

    """
    Implementar un comparador que compare dos aristas segun su peso:
        If peso1 > peso2 -> 1
        If peso1 < peso2 -> -1
        Else -> 0
    """
    def __cmp__(self,otro):
        """Funcion de comparacion"""
        pass

    """
    Implementar una función ObtenerPeso que devuelva el peso de la Arista.
    Extra: Idem anteriores.
    """     
    def ObtenerPeso(self):
        """Devuelve el peso de la arista"""
        pass

    """
    Implementar una función ObtenerArista que devuelva una tupla (origen, destino, peso).
    Extra: Idem anteriores.
    """    
    def ObtenerArista(self):
        """Devuelve todos los datos de la arista en forma de tupla"""
        pass

    """
    Implementar una función CambiarPeso que modifique el peso de la Arista.
    Extra: Idem anteriores (setter).
    """
    #TODO
    def CambiarPeso(self,nuevo_peso):
        pass

"""
Comentario:
El IteradorGrafo se utiliza en el código para encontrar el camino minimo.
No necesitaran usarlo!
"""
class _IteradorGrafo(object):
    """Iterador del Grafo"""

    def __init__(self,Grafo):
        """Inicializador recibe el grafo a iterar"""
        self.grafo = Grafo
        self.grafo_claves = Grafo.keys()
        self.indice = 0
        self.elementos = len(self.grafo_claves)

    def next(self):
        """Devuelve el proximo elemento"""
        if self.indice == self.elementos:
            raise StopIteration
        valor = self.grafo.get(self.grafo_claves[self.indice])
        self.indice +=1
        return valor


""" 
Implementar clase Grafo.
El Grafo lo representaremos como básicamente con un diccionario de Vertice. Cada uno de estos Vertice 
contendrán a las Aristas que salen del mismo.
"""

class Grafo(object):
    """Representa un Grafo"""
 
    """
    Implementar un constructor que cuente con un diccionario de vertices y un booleano que indique
    si es dirigido o no.
    """
    def __init__(self,dirigido = False):
        """Inicializador, recibe un booleano para indicar si es dirigido o no. 
        Inicializa un grafo vacío (sin vertices) y con el parámetro dirigido según corresponda.
        """
        pass

    def __iter__(self):
        """Funcion de iteracion"""
        return _IteradorGrafo(self.grafo)

    """
    Implementar función AgregarVertice que reciba un identificador y opcionalmente un valor, cree 
    el vertice con estos parámetros y lo almacene en el grafo.
    """
    def AgregarVertice(self,identificador,valor = None):
        """Agrega un vertice al grafo recibe un identificador y opcionalmente un valor"""
        pass
    
    """
    Implementar función AgregarArista que reciba un identificador de origen, un identificador de 
    destino y opcionalmente un peso, cree la arista y la almacene en el grafo.
    Nota: Verificar casos de error.
    """
    def AgregarArista(self,identificador_v1,identificador_v2,peso = None):
        """Agrega una arista que conecta dos vertices recibe dos identificadores y opcionalmente el peso de la arista"""
        pass

    """
    Implementar función ObtenerValor que reciba un identificador y devuelva el valor almacenado 
    en el vertice.
    Nota: Verificar errores.
    Extra: Reemplazar esta función por __getitem__, de forma tal de que grafo[id] -> valor
    """
    def ObtenerValor(self,identificador):
        """Devuelve el valor de un vertice"""
        pass

    """
    Implementar función HayArista que reciba un identificador de origen y otro de destino, y 
    devuelva true si existe la arista, y false si no existe.
    """
    def HayArista(self,identificador_v1,identificador_v2):
        """Devuelve True o False segun si existe arista que une dos vertices"""
        pass
    
    """
    Implementar función PesoArista que reciba un identificador de origen y otro de destino, y 
    devuelva el peso de la arista.
    Nota: Verificar errores.
    """
    def PesoArista(self,identificador_v1,identificador_v2):
        """Devuelve el peso de una arista que une dos vertices"""
        pass
        
    """
    Algoritmo de Dijkstra
    """
    def ObtenerCaminoMinimo(self,origen,destino):
        """Devuelve una lista con los vertices del camino minimo desde origen a destino"""
        padre = {}
        padre[origen] = None
        distancia = {}
        for vert in self:
            distancia[vert.id()] = float("inf")
        distancia[origen] = 0
        heap = Heap()
        dato_origen = DatoVertice(origen,distancia[origen])
        heap.encolar(dato_origen)
        while not heap.esta_vacio():
            vertice = heap.desencolar()
            vertice_actual,peso = vertice.ObtenerVertice()
            if vertice_actual == destino:
                return GenerarCamino(padre,origen,destino)
            for vecino in self.grafo[vertice_actual].Vecinos():
                if distancia[vecino] > distancia[vertice_actual] + self.PesoArista(vertice_actual,vecino):
                    distancia[vecino] = distancia[vertice_actual] + self.PesoArista(vertice_actual,vecino)
                    padre[vecino] = vertice_actual
                    dato_v = DatoVertice(vecino,distancia[vecino])
                    heap.encolar(dato_v)
        return None
