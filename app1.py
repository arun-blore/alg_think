#!/usr/bin/python

"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

from proj1 import *
import matplotlib.pyplot as plt

###################################
# Code for loading citation graph

def load_graph():
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = open ("alg_phys-cite.txt")
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    #print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph()

in_degree_dist = in_degree_distribution (citation_graph)

print (in_degree_dist)

x = []
y = []

for key in in_degree_dist :
   x.append(key)
   y.append(in_degree_dist[key])

plt.plot (x, y, 'ro')
plt.xscale('log')
plt.yscale('log')
plt.show()
