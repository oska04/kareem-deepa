# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:34:49 2018

@author: kayod
"""

import kruskals_functions

""" This file should implement Kruskal's algorithm """
def Kruskals(textfile):
	result = []

	i = 0
	e = 0

	g = kruskals_functions.getGraph(textfile)

	print('Original graph\n')

	g.draw_graph()

	edge_dict = g.edge_dict()

	edge_dict_sorted_keys = sorted(edge_dict, key=lambda x : edge_dict[x]) 
	
	V = kruskals_functions.getVertexNumber(g)

	parent = []
	rank = []
	for node in range(V):
		parent.append(node)
		rank.append(0)


	while e < V - 1:

		u, v = edge_dict_sorted_keys[i]
		i = i + 1
		x = kruskals_functions.find(parent, u)
		y = kruskals_functions.find(parent, v)

		if x != y:
			e = e + 1
			result.append([u, v, edge_dict[(u, v)]])
			kruskals_functions.union(parent, rank, x, y)
	kruskals_functions.write_to_file(result)

	print('Kruskal ran successfully, edge list stored in mst_graph.txt')

	print('Here is how the graph looks!')

	mst_graph = kruskals_functions.getGraph("mst_graph.txt")

	mst_graph.draw_graph()
