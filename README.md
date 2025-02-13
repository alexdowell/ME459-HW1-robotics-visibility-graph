# ME459 HW1: Robotics and Visibility Graphs

## Description  
This repository contains Homework 1 for **ME459 - Robotics and Unmanned Systems** at the **University of Missouri-Kansas City**. The assignment covers visibility graph generation, class-based node structures, shortest path computation, and grid-based path planning techniques.

## Files Included  

### **Assignment Document**  
- **File:** ME 459 HW 1.pdf  
- **Contents:**  
  - Problem descriptions  
  - Instructions for graph generation and pathfinding  
  - Equations for computing node indices  

### **Python Implementations**  
#### **Problem 2: Node Class Implementation**  
- **File:** ME_459_HW_1_P2.py  
- **Topics Covered:**  
  - Python class creation  
  - Instance variables for x, y, parent cost, and index  

#### **Problem 4: Node Indexing & Visualization**  
- **File:** ME_459_HW_1_P4.py  
- **Topics Covered:**  
  - Grid-based path planning  
  - Node indexing based on map coordinates  
  - Visualization of node indices on a graph  

#### **Problem 5: Distance Calculation**  
- **File:** ME_459_HW_1_P5.py  
- **Topics Covered:**  
  - Function for computing Euclidean distance between two nodes  
  - Testing with example coordinates  

## Installation  
Ensure you have Python installed along with the required libraries before running the scripts.

### Required Python Libraries  
- **Matplotlib** (for plotting graphs)  
- **NumPy** (for numerical computations)  

To install the necessary packages, run:  
`pip install matplotlib numpy`  

## Usage  
1. Run the Python scripts in a terminal or an IDE of your choice.  
2. Ensure the node class (Problem 2) is implemented correctly before using it in Problems 4 and 5.  
3. Generate and visualize the visibility graph for pathfinding solutions.  

## Example Output  

- **Node Class Definition (Problem 2)**
  ```python
  node1 = node()
  node1.define(2, 3, 5, 1)
  print(node1.x, node1.y, node1.parent_cost, node1.index)
