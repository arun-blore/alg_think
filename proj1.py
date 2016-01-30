#!/usr/bin/python

"""
This file creates simple graphs using python dictionaries.
It also conatains functions to compute features related to degrees of graphs.
"""

EX_GRAPH0 = {
0: set([1,2]),
1: set([]),
2: set([])
}

EX_GRAPH1 = {
0: set([1, 5, 4]),
1: set([2, 6]),
2: set([3]),
3: set([0]),
4: set([1]),
5: set([2]),
6: set([])
}

EX_GRAPH2 = {
0: set([1, 5, 4]),
1: set([2, 6]),
2: set([3, 7]),
3: set([7]),
4: set([1]),
5: set([2]),
6: set([]),
7: set([3]),
8: set([1, 2]),
9: set([0, 4, 5, 6, 7, 3])
}

def make_complete_graph (num_nodes) :
   """
   num_nodes is an integer.
   This function creates a complete directed graph with num_nodes.
   The graph is implemented as a dictionary. Each key is an integer which corresponds to a node.
   If num_nodes is negative or 0, it returns an empty graph
   """
   graph = dict ()
   if (num_nodes < 1) :
      return graph

   for node_ind in range (num_nodes) :
      # create a set containing nodes adjacent to node node_ind
      # node node_ind of the complete graph will have edges to all other nodes except itself
      adj_nodes = range (num_nodes) # list containing numbers from 0 - num_nodes-1
      adj_nodes.remove(node_ind)
      graph[node_ind] = set(adj_nodes)

   return graph

def compute_in_degrees (digraph) :
   """
   This function takes a directed graph (digraph) represented as a dictionary
   and returns the in-degree of nodes that grpah. The returned object is a
   dictionary with the same set of keys as digraph and whose corresponding values
   are in-degrees of the node corresponding to that key
   """
   in_degree = dict()

   # initialize the in-degree of each node with 0s
   for key in digraph :
      in_degree[key] = 0

   for node in digraph :
      for head_node in digraph[node] :
         in_degree[head_node]+=1

   return in_degree

def in_degree_distribution (digraph) :
   """
   This function takes a directed graph (digraph) represented as a dictionary and 
   returns the unnormalized distribution of in-degrees of the graph.
   The returned object is a dictionary with keys as the in-degree and the value as
   the number of nodes which have that key as their in-degree.
   In-degrees with no corresponding nodes will be included in the dictionary.
   """

   in_degree_dist = dict ()
   in_degrees = compute_in_degrees (digraph)

   for node in in_degrees :
      if in_degrees[node] in in_degree_dist :
         in_degree_dist[in_degrees[node]] += 1
      else :
         in_degree_dist[in_degrees[node]] = 1

   return in_degree_dist

#print make_complete_graph(3)
#print compute_in_degrees(EX_GRAPH2)
#print in_degree_distribution(EX_GRAPH2)
