#!/usr/bin/env python
"""
Aufgabe 2: Vererbung - quader.py
"""
from rechteck import Rechteck

class Quader(Rechteck):
    "Klasse Quader, von Rechteck abgeleitet"""
    def __init__(self, length, width, heigth):
        """init-Methode zur Instanziierung des Objektes der Klasse"""
        self.length = length
        self.width = width
        self.heigth = heigth
    def volumen(self):
        """Berechnung des Volumens"""
        return self.length*self.width*self.heigth