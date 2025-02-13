# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:21:21 2022

@author: Alexander Dowell
"""
import matplotlib.pyplot as plt # plotting tools
import numpy as np  # poor mans matlab
'''
class Node():           # for assigning attributes to nodes 
    def __init__(self,x,y,parent_cost,index):
        self.x = x
        self.y = y
        self.parent_cost = parent_cost
        self.index = index
 '''       
        
def make_grid(x_min, x_max, y_min, y_max, gs): # for creating a x,y grid
    
    x_bounds = np.arange(x_min_max[0],x_min_max[1]+gs,gs)
    y_bounds = np.arange(y_min_max[0],y_min_max[1]+gs,gs)
    
    return x_bounds, y_bounds

if __name__=='__main__': 
    x_min_max = [0,10]
    y_min_max = [0,10]
    gs = 0.5
    
    x_bounds, y_bounds = make_grid(x_min_max[0], x_min_max[1], y_min_max[0], y_min_max[1], gs)
    plt.axis([x_min_max[0], x_min_max[-1]+gs, y_min_max[0], y_min_max[-1]+gs]) # plots the axes
    
    for y in y_bounds:
        for x in x_bounds:
            index_current = ((y - y_min_max[0]) / gs) * ((x_min_max[1] - x_min_max[0])+gs)/gs + ((x - x_min_max[0]) / gs)
            plt.text(x, y, str(int(index_current)), color="red", fontsize=8) # plots the node number on x,y grid
            print(x,y,index_current)
    
    