# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:37:08 2018

@author: kayod
"""

import prims_functions


def Prims(textfile):
	g = prims_functions.getGraph(textfile)

	print('Original graph\n')
	g.draw_graph()

	
	V = prims_functions.getVertexNumber(g)
	key = [99999] * V
	parent = [None] * V
	mstSet = [False] * V
	parent[0] = -1
	key[0] = 0

	edge_dict = g.edge_dict()

	for i in range(0, V):
		u = prims_functions.minKey(key, mstSet)

		mstSet[u] = True

		for v in range(V):
			temp = (u, v)
			temp2 = (v, u)
			if temp in edge_dict and mstSet[v] == False and key[v] > edge_dict[temp]:
				key[v] =  edge_dict[temp]
				parent[v] = u
			elif temp2 in edge_dict and mstSet[v] == False and key[v] > edge_dict[temp2]:
				key[v] =  edge_dict[temp2]
				parent[v] = u

	mst_edges = prims_functions.getMST(parent)

	prims_functions.write_to_file(mst_edges, g)

	print('Prim ran successfully, edge list stored in mst_graph.txt')

	print('Here is how the graph looks!')

	mst_graph = prims_functions.getGraph("mst_graph.txt")

	mst_graph.draw_graph()