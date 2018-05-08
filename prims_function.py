# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:37:09 2018

@author: kayod
"""

from Weighted_Graph import *

def getGraph(textfile):
	return Weighted_Graph(textfile)

def getVertexNumber(g):
	return len(g.vertex_set())

def minKey(key, mstSet):
 
	# Initilaize min value
	min = 999999

	for v in range(len(mstSet)):
		if key[v] < min and mstSet[v] == False:
			min = key[v]
			min_index = v

	return min_index

def getMST(parent):
	mst_edges = []
	for i in range(1, len(parent)):
		mst_edges.append((parent[i], i))
	return mst_edges

def write_to_file(mst_edges, g):
	edge_dict = g.edge_dict()
	f = open("mst_graph.txt", "w")
	for x in mst_edges:
		u, v = x
		y = (v, u)
		if x in edge_dict:
			f.write(str(u) + " " + str(v) + " " + str(edge_dict[x]))
		elif y in edge_dict:
			f.write(str(u) + " " + str(v) + " " + str(edge_dict[y]))
		f.write("\n")

	f.close()
