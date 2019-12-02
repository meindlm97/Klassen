#!/usr/bin/env python
"""
Aufgabe 3: Klassen - formen.py
"""
#numpy, random und die zwei Module importieren
import random
import numpy as np
from kreis import Circle
from rechteck import Rectangle

# Klasse Formen definieren und instanzieren
class Formen(Rectangle, Circle):
    """Klasse Formen mit Parametern Rectangle und Circle"""
    def __init__(self, getArea, getPerimeter, getArea_, getPerimeter_):
        """init-Methode zur Instanziierung der Objekte der Klasse"""
        self.getArea = getArea
        self.getPerimeter = getPerimeter
        self.getArea_ = getArea_
        self.getPerimter_ = getPerimeter_

# Erzeugen von jeweils einem Rechteck und Kreis + Berechnung von Umfang und Fläche
for i in range(10):
    x = random.randint(1, 51)

A1 = Circle(x)
A2 = Rectangle(x, x)
print("Flächeninhalt Kreis: " + str(A1.getArea()) + " m²")
print("Umfang Kreis: " + str(A1.getPerimeter()) + " m")
print("Flächeninhalt Rechteck: " + str(A2.getArea_()) + " m²")
print("Umfang Rechteck: " + str(A2.getPerimeter_()) + " m")
print("")

def Zufallszahl():
    """Funktion um Zufallszahl zu generieren"""
    number = random.randint(1,50)
    return number

# Erzeugen eines leeren Arrays, danach zufällige Befüllung mit Rechteck und Kreis
Form = []
for i in range(10):
    y = random.choice(["Rechteck", "Kreis"])
    Form.append(y)

# Erzeugen von 4 lerren Arrays zur Speicherung aller Umfänge und Flächen
areas_k = []
perimeters_k = []
areas_r = []
perimeters_r = []

# Zuweisung von zufällig errechneten Flächen und Umfängen
for i in Form:
    if i == "Rechteck":
        length = Zufallszahl()
        width = Zufallszahl()
        R_i = Rectangle(length, width)
        
        areas_r.append(R_i.getArea_())
        perimeters_r.append(R_i.getPerimeter_())
    elif  i == "Kreis":
        radius = Zufallszahl()
        K_i = Circle(radius)
        
        areas_k.append(K_i.getArea())
        perimeters_k.append(K_i.getPerimeter())

# Ausgabe der Umfänge und Flächen
print("Fläche aller Kreise in m²: " + str(areas_k))
print("Umfang aller Kreise in m: " + str(perimeters_k))
print("Fläche aller Rechtecke in m²: " + str(areas_r))
print("Umfang aller Rechtecke in m: " + str(perimeters_r))
print("")

# Ausgabe einer Zufallszahl zwischen 1 und 50
print("Zufallszahl zwischen 1 und 50: " + str(Zufallszahl()))
print("")

# Ausgabe wie viele Rechtecke und Kreise es im Array gibt
print("In der Liste gibt es " + str(Form.count("Kreis")) + " Kreise.")
print("In der Liste gibt es " + str(Form.count("Rechteck"))  + " Rechtecke.")
print("")

# Ausgabe der durchschnittlichen Umfänge
print("Der durchschnittliche Umfang aller Kreise beträgt: " + str(np.mean(perimeters_k)) + " m.")
print("Der durchschnittliche Umfang aller Rechtecke beträgt: " +str(np.mean(perimeters_r)) + " m.")