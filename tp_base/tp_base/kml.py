#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este modulo debe ser capaz de generar un archivo kml con las ciudades y rutas.
Para representar las ciudades sera necesario conocer el nombre, la longitud y 
latitud de la misma.
Para representar las rutas sera necesario conocer la longitud y latitud de 
origen y destino.

La estructura del archivo kml debe ser la siguiente:


<?xml version="1.0" encoding="UTF-8"?>
	<kml xmlns="http://earth.google.com/kml/2.1">
    	<Document>
			
			<!-- Lugares a representar -->

			<Placemark>
    			<name>Facultad de Ingeniería, UBA</name>
    			<Point>
        			<coordinates>-58.3679593, -34.6176355</coordinates>
    			</Point>
			</Placemark>
			
			....

			<!-- Rutas a representar -->
			
			<Placemark>
    			<LineString>
        			<coordinates>-58.36795, -34.61763 -58.39644, -34.58850</coordinates>
    			</LineString>
			</Placemark>
		</Document>
	</kml>
"""

