"""
	Doc strigns for test_py_geometry.py
	This file comtains tests for the various functions 
"""

from geometry import *



def test_area_of_square():
	assert area_of_square(3) == 9
	assert area_of_square(2) == 4

def test_area_of_square_with_string_args():
	assert area_of_square('3') == 9
	assert area_of_square('2') == 4
	assert area_of_square('3') == 9

def test_area_of_rectangle():
	assert area_of_rectangle(3, 4) == 12
	assert area_of_rectangle(2, 5) == 10
	# assert area_of_rectangle('3', 5) == 15

def test_area_of_rectangle_with_string_args():
	assert area_of_square('3', '3') == 9
	assert area_of_square('2', '3') == 4
	assert area_of_square('3', '3') == 9