#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: 0102_strings.py
Author: academia hola_mundo_io, mikdevio
Date: 2026-15-02
Description: This module has code written during a programation practice.
"""

print("0102 Python basics strings.")

course_name = "Ultimate Python"

# Docstring
course_description = """
    Master Python fundamentals and powerful libraries through hands-on projects designed to solve real-world logic and data challenges. Transition from a coding novice to a versatile developer ready to automate the boring stuff and build the future of tech.
"""
# Indexado de strings
# Los indices en python empiezan con 0, es decir que el tamaño del 
# string es el numero de caracteres menos 1
print(f"El nombre del curso es: {len(course_name)}")
print(f"La primera letra del nombre del curso es: {course_name[0]}")
print(f"La segunda letra del nombre de curso es: {course_name[1]}")
print(f"Primera palabra del titulo: {course_name[:8]}")
print(f"Ultima palabra del nombre del curso: {course_name[9:]}")