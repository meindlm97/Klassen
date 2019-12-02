#!/usr/bin/env python
"""
Aufgabe 3: Klassen - rechteck.py
"""
class Rectangle:
    """Klasse Rectangle"""
    def __init__(self, width, length):
        """init-Methode zur Instanziierung der Objekte der Klasse"""
        self.width = width
        self.length = length

    def getWidth(self):
        """Funktion der Breite"""
        return self.width

    def getLength(self):
        """Funktion der Laenge"""
        return self.length

    def getArea_(self):
        """Berechnung der Flaeche"""
        return self.width * self.length

    def getPerimeter_(self):
        """Berechnung des Umfangs"""
        return 2 * (self.width + self.length)