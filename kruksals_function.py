# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:35:58 2018

@author: kayod
"""

from Weighted_Graph import *

def getGraph(textfile):
	return Weighted_Graph(textfile)

def getVertexNumber(g):
	return len(g.vertex_set())

def find(parent, i):
	if parent[i] == i:
		return i
	return find(parent, parent[i])


def union(parent, rank, x, y):
	xroot = find(parent, x)
	yroot = find(parent, y)

	# Attach smaller rank tree under root of 
	# high rank tree (Union by Rank)
	if rank[xroot] < rank[yroot]:
		parent[xroot] = yroot
	elif rank[xroot] > rank[yroot]:
		parent[yroot] = xroot

	# If ranks are same, then make one as root 
	# and increment its rank by one
	else :
		parent[yroot] = xroot
		rank[xroot] += 1

def write_to_file(results):
	f = open("mst_graph.txt", "w")
	for u, v, w in results:
		f.write(str(u) + " " + str(v) + " " + str(w))
		f.write("\n")

	f.close()