#!/usr/bin/env python
"""
Aufgabe 2: Vererbung - rechteck.py
"""
from formen import Formen

class Rechteck(Formen):
    """Klasse Rechteck, von Formen abgeleitet"""
    def __init__(self, width, length):
        """init-Methode zur Instanziierung der Objekte der Klasse"""
        self.width = width
        self.length = length

    def flaeche(self):
        """Berechnung der Flaeche"""
        return self.width * self.length

    def umfang(self):
        """Berechnung des Umfangs"""
        return 2 * (self.width + self.length)