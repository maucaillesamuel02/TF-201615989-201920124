# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 19:36:55 2022

@author: Samuel
"""

import osmnx as ox

G = ox.graph_from_place('Santiago de Surco, Lima, Peru', network_type='drive')
 
prj_road=ox.project_graph(G)

ox.save_graph_shapefile(prj_road, filepath=r'C:\Users\PERU\Desktop\Test\Santiago de Surco1')


