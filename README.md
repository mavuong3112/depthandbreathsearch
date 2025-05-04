# 🧠 Maze Solver with DFS & BFS
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/) 
🎓 Project Introduction to artificial intelligence
🏫 University of Economics HCMC  

## 📌 Project Overview

This project implements **maze generation and pathfinding** using two classical AI search algorithms:  
**Depth-First Search (DFS)** and **Breadth-First Search (BFS)**.  

The maze is procedurally generated and visualized using `tkinter`, with both DFS and BFS applied to find the shortest path from a start point to a target cell.

## 🧠 Algorithms Used

### 🔹 Breadth-First Search (BFS)
- Explores the maze level by level.
- Guarantees the **shortest path**.
- Suitable for unweighted graphs but **uses more memory**.

### 🔹 Depth-First Search (DFS)
- Explores deep into each branch before backtracking.
- **Less memory intensive**, but may not find the shortest path first.
- Good for exploring large and deep mazes.

## 🧱 Maze Structure

- The maze is represented as a 2D grid.
- Each cell may contain walls (top, right, bottom, left).
- The maze is built using DFS-based backtracking, ensuring a perfect maze (no loops, one unique path between any two cells).
- Target and path are visualized dynamically.
![image](https://github.com/user-attachments/assets/30ed2acf-4181-4d6f-bc12-b194abef4751)

