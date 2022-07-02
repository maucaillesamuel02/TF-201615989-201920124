# -*- coding: utf-8 -*-

import osmnx as ox

G = ox.graph_from_place('Santiago de Surco, Lima, Peru', network_type='drive')
 
prj_road=ox.project_graph(G)

ox.save_graph_shapefile(prj_road, filepath=r'C:\Users\PERU\Desktop\Test\Santiago de Surco1')

nodes, edges = ox.graph_to_gdfs(G)
edges_series = edges['length']

G_proj = ox.project_graph(G)
points = ox.utils_geo.sample_points(ox.get_undirected(G_proj), 10000)
%time ne2 = ox.nearest_edges(G_proj, X=points.x, Y=points.y, interpolate=10, return_dist=True)