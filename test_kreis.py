#!/usr/bin/env python
"""
Aufgabe 3: pytest - test_kreis.py
"""

from math import pi
import pytest
from formen import Kreis

def test_for_kreis_flaeche():
    "Testing für Flächenberechnung eines Kreises"
    assert Kreis(1).flaeche() == pi

def test_for_kreis_umfang():
    "Testing für Berchnung des Umfangs eines Kreises"
    assert Kreis(1).umfang() == 2*pi

def test_for_kreis_volumen():
    "Testing für Volumsberechnung eines Rechtecks"
    assert Kreis(1).volumen() == "Die Berechnung des Volumens ist noch nicht näher speziﬁziert."