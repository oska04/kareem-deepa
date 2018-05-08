# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:37:10 2018

@author: kayod
"""

from Prims import Prims
from Kruskals import Kruskals

""" This file should be your main program
which solves the MST using either
Prims or Kruskals (bonus for both) """
def MST(textfile, algorithm = 'Prims'):
	if algorithm == 'Prims':
		return Prims(textfile)
	else:
		return Kruskals(textfile)



MST("sample_input.txt", "Kruskals")