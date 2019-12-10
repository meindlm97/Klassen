#!/usr/bin/env python
"""
Aufgabe 3: pytest - test_rechteck.py
"""

import pytest
from formen import Quader

def test_for_quader_flaeche():
    "Testing für Flächenberechnung eines Quaders"
    assert Quader(1, 2, 3).flaeche() == 2

def test_for_quader_umfang():
    "Testing für Berechnung des Umfangs eines Quaders"
    assert Quader(1, 2, 3).umfang() == 6

def test_for_quader_volumen():
    "Testing für Volumsberechnung eines Quaders"
    assert Quader(1, 2, 3).volumen() == 6