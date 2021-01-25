#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 04:16:06 2020

@author: andrea32
"""

## Introduction to Network Analysis

## Imports

import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np


## Basics of NetworkX

import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])
G.nodes()

G.add_edge(1,2)
G.add_edge("u","v")

G.add_edges_from([(1,3),(1,4),(1,5),(1,6)])
G.add_edge("u","w")

G.edges()

G.remove_node(2)
G.remove_nodes_from([4,5])

G.nodes()
G.remove_edge(1,3)

G.edges()
G.remove_edges_from([(1,2),("u","v")])

G.edges()

G.number_of_nodes()
G.number_of_edges()

## Graph Visualization

G = nx.karate_club_graph()

import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.savefig("karate_graph.pdf")

G.degree()

G.degree()[33]
G.degree(33)

## Random Graphs

from scipy.stats import bernoulli
bernoulli.rvs(p=0.2)

N = 20
p = 0.2 

    #Create empty graph
    # add all N nodes on the graph
    # loop over all pairs of nodes
        #add and edge with prop p

def er_graph(N, p):
    """ Generate an ER graph """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
           if node1 < node2 and bernoulli.rvs(p=p):
               G.add_edge(node1, node2)
    return G

nx.draw(er_graph(50, 0.08), node_size=40, node_color="gray")
plt.savefig("er1.pdf")

nx.erdos_renyi_graph(n=10,p=1)

## Plotting the degree Distribution

def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")

G = er_graph(500, 0.08)
plot_degree_distribution(G)
plt.savefig("hist1.pdf")


G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.savefig("hist_3.pdf")

## Descriptive Statistics of Empirical Social Networks

import numpy as np
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")


G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("number of nodes: %d" % G.number_of_nodes())
    print("number of edges: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))

basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.savefig("village_hist.pdf")


## Finding the Largest Connected Component

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)

(G.subgraph(c) for c in nx.connected_components(G1))

nx.connected_component_subgraphs(G1)

gen = connected_component_subgraphs(G1)
G1_lcc = G1.subgraph(max(nx.connected_components(G1), key=len)).copy() 
G1_lcc.number_of_nodes()
len(G1_lcc)


G1_lcc = G1.subgraph(max(nx.connected_components(G1), key=len)).copy() 
G2_lcc = G2.subgraph(max(nx.connected_components(G2), key=len)).copy() 

len(G1_lcc)
len(G2_lcc)

G1_lcc.number_of_nodes() / G1.number_of_nodes()
G2_lcc.number_of_nodes() / G2.number_of_nodes()


plt.figure()
nx.draw(G1_lcc, node_color="red", edge_color="gray", node_size=20)
plt.savefig("village1.pdf")

plt.figure()
nx.draw(G2_lcc, node_color="green", edge_color="gray", node_size=20)
plt.savefig("village2.pdf")

















































