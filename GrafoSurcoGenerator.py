# -*- coding: utf-8 -*-

import osmnx as ox

G = ox.graph_from_place('Santiago de Surco, Lima, Peru', network_type='drive')
 
prj_road=ox.project_graph(G)

ox.save_graph_shapefile(prj_road, filepath=r'C:\Users\PERU\Desktop\Test\Santiago de Surco1')

nodes, edges = ox.graph_to_gdfs(G)
edges_series = edges['length']