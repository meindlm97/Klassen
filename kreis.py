#!/usr/bin/env python
"""
Aufgabe 3: Klassen - kreis.py
"""
# Importieren von pi aus dem Mathe-Paket
from math import pi

class Circle:
    """Klasse Circle"""
    def __init__(self, radius):
        """init-Methode zur Instanziierung des Objektes der Klasse"""
        self.radius = radius
      
    def getRadius(self):
        """Funktion des Radius"""
        return self.radius

    def getArea(self):
        """Berechnung der Fläche"""
        return self.radius**2 * pi

    def getPerimeter(self):
        """Berechnung des Umfangs"""
        return 2 * self.radius * pi
