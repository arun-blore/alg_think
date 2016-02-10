#!/usr/bin/python
"""
This file contains functions related to computation of connected components and resilience of graphs.
"""

from collections import deque

def bfs_visited (ugraph, start_node) :
   """
   Takes an undirected graph (ugraph) and node start_node as inputs.
   Returns the set of all nodes visited by a breadth first seach that starts at start_node.
   """
   q_tmp = deque ()
   visited = set ([start_node])
   q_tmp.append (start_node)
   while len(q_tmp) :
      node1 = q_tmp.pop ()
      for node2 in ugraph[node1] :
         if node2 not in visited :
            visited.add(node2)
            q_tmp.append(node2)
   return visited

def cc_visited (ugraph) :
   """
   Takes an undirected graph (ugraph) as input.
   Returns the set of connected components of the graph.
   The returned output is a set which further contains sets, each of which is a connected component of ugraph
   """
   nodes_set = set(ugraph.keys())
   conn_comps = []
   while len(nodes_set) :
      node = nodes_set.pop ()
      cc_node = bfs_visited (ugraph, node)
      nodes_set.difference_update(cc_node)
      conn_comps.append(cc_node)
   return conn_comps

def largest_cc_size (ugraph) :
   """
   Takes an undirected graph (ugraph) as input.
   Returns the size (an integer) of the largest connected component of ugraph.
   """
   cc_ugraph = cc_visited (ugraph)
   max_size = 0
   for conn_comp in cc_ugraph :
      if len(conn_comp) > max_size :
         max_size = len(conn_comp)
   return max_size

def compute_resilience (ugraph, attack_order) :
   """
   Takes an undirected graph (ugraph) and a list of nodes in ugraph (attack_order) as inputs.
   Returns a list (of size len(attack_order)+1) whose k+1 th entry is the size of the largest connected component of ugraph when the first k nodes in attack_order are removed.
   """
   largest_cc_sizes = []
   largest_cc_sizes.append(largest_cc_size(ugraph))
   for att_node in attack_order :
      # remove att_node from graph
      for node in ugraph :
         ugraph[node].discard(att_node)
      ugraph.pop(att_node)
      largest_cc_sizes.append(largest_cc_size(ugraph))
   return largest_cc_sizes
