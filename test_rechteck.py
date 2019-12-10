#!/usr/bin/env python
"""
Aufgabe 3: pytest - test_rechteck.py
"""

import pytest
from formen import Rechteck

def test_for_rechteck_flaeche():
    "Testing für Flächenberechnung eines Rechtecks"
    assert Rechteck(2, 2).flaeche() == 4

def test_for_rechteck_umfang():
    "Testing für Berechnung des Umfangs eines Rechtecks"
    assert Rechteck(2, 2).umfang() == 8

def test_for_rechteck_volumen():
    "Testing für Volumsberechnung eines Rechtecks"
    assert Rechteck(2, 2).volumen() == "Die Berechnung des Volumens ist noch nicht näher speziﬁziert."