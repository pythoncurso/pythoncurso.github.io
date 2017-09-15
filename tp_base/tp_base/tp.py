#!/usr/bin/env python
# -*- coding: utf-8 -*-

from grafo import Grafo
import csv
from kml import *

NOMBRE_ARCHIVO_CIUDAD = "ciudades.csv"
NOMBRE_ARCHIVO_RUTAS = "rutas.csv"

NOMBRE_ARCHIVO_SALIDA_SELECCION_RUTA = "rutas.kml"
NOMBRE_DESCRIPCION_SALIDA_SELECCION_RUTA = "Rutas Ferroviarias"
DESCRIPCION_SALIDA_SELECCION_RUTA = "Rutas Ferroviarias"

NOMBRE_ARCHIVO_SALIDA_CAMINO_SELECCION_RUTA = "seleccion_rutas_camino_minimo.kml"
NOMBRE_DESCRIPCION_SALIDA_CAMINO_SELECCION_RUTA = "Camino minimo"
DESCRIPCION_SALIDA_CAMINO_SELECCION_RUTA = "Minimiza la distancia entre dos ciudades"

def construir_rutas():
	"""Lee los archivos CSV que corresponden a las rutas y ciudades. Escribe los resultados en un archivo kml y devuelve
	el grafo resultante."""

	###Crear Grafo
	
	###Leer archivo csv de ciudades y agregar vertices

	###Leer archivo csv de rutas y agregar aristas

	###Escribir kml con las ciudades y rutas entre ellas
	
	###Devolver grafo

	pass

def pedir_ciudades(grafo):
	"""Pide al usuario  dos nombres de ciudades (origen y destino) hasta recibir dos ciudades que esten en el grafo, y devuelve el id de cada una."""
	pass


def camino_minimo(grafo,id_ciudad_1,id_ciudad_2,nombre_archivo_salida,nombre_descripcion,descripcion):
	"""Dados un origen y un destino, encuentra el camino minimo entre ambas ciudades y lo escribe en un archivo kml."""
	
	###Obtener camino mimino usando el metodo del grafo

	pass

def main():
	grafo_rutas = construir_rutas()
	id_ciudad_origen,id_ciudad_destino = pedir_ciudades(grafo_rutas)
	camino_minimo(grafo_rutas,id_ciudad_origen,id_ciudad_destino,NOMBRE_ARCHIVO_SALIDA_CAMINO_SELECCION_RUTA,NOMBRE_DESCRIPCION_SALIDA_CAMINO_SELECCION_RUTA,DESCRIPCION_SALIDA_CAMINO_SELECCION_RUTA)
	print "Los archivos se generaron correctamente"

main()
