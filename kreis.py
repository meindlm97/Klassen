#!/usr/bin/env python
"""
Aufgabe 2: Vererbung - kreis.py
"""
# Importieren von pi aus dem Mathe-Paket
from formen import Formen
from math import pi

class Kreis(Formen):
    """Klasse Kreis, von Formen abgeleitet"""
    def __init__(self, radius):
        """init-Methode zur Instanziierung des Objektes der Klasse"""
        self.radius = radius

    def flaeche(self):
        """Berechnung der Flaeche"""
        return self.radius**2 * pi

    def umfang(self):
        """Berechnung des Umfangs"""
        return 2 * self.radius * pi