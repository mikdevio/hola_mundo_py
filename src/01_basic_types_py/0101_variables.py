#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: 0101_variables.py
Author: academia hola_mundo_io, mikdevio
Date: 2026-15-02
Description: This module has code written during a programation practice.
"""

# Nombre de variable : Los nombres de variable debe empezar on letras no numeros y usar notacion snakecase, palabras encadenadas con "_".

course_name = "Ultimate python"
Course_name = "Ultimate python, second."

print(course_name)  # El resultado muestra que las variables son case sensitive y diferencia caracteres

# El interprete es case sensitive es decir diferencia caracteres mayusculos de minusculos
name_1 = "Hola"
COURSE_NAME = "Mundo"
CoUrSe_NaMe = "Intercalado"

print(course_name, name_1, COURSE_NAME)

number_students = 5000  # Entero
score = 9.5             # Flotante
published = False       # Boolean

print(number_students, score, published)
