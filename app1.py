#!/usr/bin/python

"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

from proj1 import *
from random import *
from DPATrial import *
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
    num_edges = 0
    
    # print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))
            num_edges+=1

    # print "Loaded graph with", num_edges, "edges"

    return answer_graph

def plot_in_degree_dist (graph) :
   x = []
   y = []
   
   for key in graph :
      x.append(key)
      y.append(graph[key])

   # if there are nodes with 0 in degree, dont include them in the plot since log(0) = -inf
   if x[0] == 0 :
      x = x[1:]
      y = y[1:]

   plt.plot (x[1:], y[1:], 'ro')
   plt.xscale('log')
   plt.yscale('log')
   plt.xlabel("in degrees (log scale)")
   plt.ylabel("number of nodes (log scale)")
   plt.show()

def plot_in_degree_dist_lin (graph) :
   x = []
   y = []
   
   for key in graph :
      x.append(key)
      y.append(graph[key])

   plt.plot (x, y, 'ro')
   plt.xlabel("in degrees")
   plt.ylabel("number of nodes")
   plt.show()

def make_random_graph (num_nodes, p) :
   """
   this function creates a random directed graph with num_nodes nodes. num_nodes >= 2.
   p is the probability with which any 2 nodes are connected by an edge. 0 <= p < 1
   """
   rand_graph = {}
   for node in range (num_nodes) :
      rand_graph[node] = set([])

   for node1 in rand_graph :
      for node2 in rand_graph :
         if node1 == node2 :
            continue

         rand_num = random ()
         if rand_num < p :
            rand_graph[node1].add(node2)

   return rand_graph

def make_dpa_graph (n, m) :
   """
   makes a dpa graph - as mentioned in Q3 of app1 question. n is the number of nodes in the graph.
   m is (roughly) the number of nodes to which each node is connected
   m <= n
   n > 0
   """

   # start by creating a complete graph of m nodes
   graph = make_complete_graph (m)

   dpa_obj = DPATrial (m)

   for ind in range (m, n) :
      graph[ind] = dpa_obj.run_trial (m)

   return graph


#citation_graph = load_graph()
#in_degree_dist = in_degree_distribution (citation_graph)
# plot_in_degree_dist (in_degree_dist)

#rand_graph = make_random_graph (1000, 0.7)
#rand_graph_in_degree_dist = in_degree_distribution (rand_graph)
#plot_in_degree_dist_lin (rand_graph_in_degree_dist)

n = 27770
m = 13
dpa_graph = make_dpa_graph (n, m)
in_deg_dist_dpa = in_degree_distribution (dpa_graph)
plot_in_degree_dist (in_deg_dist_dpa)
