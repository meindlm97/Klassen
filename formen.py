#!/usr/bin/env python
"""
Aufgabe 2: Vererbung
"""

from math import pi
import random
import numpy as np

class Formen:
    """Klasse Formen"""
    def __init__(self):
        """init-Methode zur Instanziierung der Objekte der Klasse"""
    def flaeche(self):
        """Berechnung der Fläche"""
        return None
    def umfang(self):
        """Berechnung des Umfangs"""
        return None
    def volumen(self):
        """Berechnung des Volumens"""
        return "Die Berechnung des Volumens ist noch nicht näher speziﬁziert."

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

class Quader(Rechteck):
    """Klasse Quader, von Rechteck abgeleitet"""
    def __init__(self, length, width, heigth):
        """init-Methode zur Instanziierung der Objekte der Klasse"""
        self.length = length
        self.width = width
        self.heigth = heigth
    def volumen(self):
        """Berechnung des Volumens"""
        return self.length*self.width*self.heigth

def zufallszahl():
    """Funktion um Zufallszahl zu generieren"""
    number = random.randint(1, 50)
    return number

# Erzeugen eines leeren Arrays, danach zufaellige Befuellung mit Rechteck und Kreis
FORM = []
for i in range(10):
    y = random.choice(["Rechteck", "Kreis"])
    FORM.append(y)

# Erzeugen von 4 lerren Arrays zur Speicherung aller Umfaenge und Flaechen
FLAECHE_K = []
UMFANG_K = []
FLAECHE_R = []
UMFANG_R = []

# Zuweisung von zufaellig errechneten Flaechen und Umfaengen
for i in FORM:
    if i == "Rechteck":
        length = zufallszahl()
        width = zufallszahl()
        R_i = Rechteck(length, width)

        FLAECHE_R.append(R_i.flaeche())
        UMFANG_R.append(R_i.umfang())
    elif  i == "Kreis":
        radius = zufallszahl()
        K_i = Kreis(radius)

        FLAECHE_K.append(K_i.flaeche())
        UMFANG_K.append(K_i.umfang())

# Um Komplikationen beim Testing zu vermeiden sollten nachfolgende Zeilen auskommentiert werden

# Ausgabe der Umfaenge und Flaechen
print("Fläche aller Kreise in m²: " + str(FLAECHE_K))
print("Umfang aller Kreise in m: " + str(UMFANG_K))
print("Fläche aller Rechtecke in m²: " + str(FLAECHE_R))
print("Umfang aller Rechtecke in m: " + str(UMFANG_R))
print("")

# Ausgabe einer Zufallszahl zwischen 1 und 50
print("Zufallszahl zwischen 1 und 50: " + str(zufallszahl()))
print("")

# Ausgabe wie viele Rechtecke und Kreise es im Array gibt
print("In der Liste gibt es " + str(FORM.count("Kreis")) + " Kreise.")
print("In der Liste gibt es " + str(FORM.count("Rechteck"))  + " Rechtecke.")
print("")

# Ausgabe der durchschnittlichen Umfaenge
print("Der durchschnittliche Umfang aller Kreise beträgt: " + str(np.mean(UMFANG_K)) + " m.")
print("Der durchschnittliche Umfang aller Rechtecke beträgt: " +str(np.mean(UMFANG_R)) + " m.")
print("")
print("Das Volumen des Quaders beträgt " + str(Quader(4,4,4).volumen()) + " m³.")
