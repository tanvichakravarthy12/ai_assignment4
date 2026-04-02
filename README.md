# 🧠 Constraint Satisfaction Problems (CSP) – AI Assignment

This repository contains Python implementations of classic **Constraint Satisfaction Problems (CSPs)**.  
It demonstrates how a generic backtracking framework can be applied to different domains like map coloring, puzzles, and cryptarithmetic.

---

## 📁 Repository Overview

### 🔹 Core Module
- **`csp.py`**  
  A reusable **Backtracking Search algorithm** for solving CSPs.  
  It manages:
  - Variables  
  - Domains  
  - Constraint validation

---

### 🔹 Implemented Problems

#### 🌍 Australia Map Coloring
- **`australia_map.py`**  
  Solves the classic map coloring problem using 3 colors.  
  Regions: WA, NT, SA, Q, NSW, V, T  

---

#### 🗺️ Telangana Map Coloring
- **`telangana_color.py`**  
  Applies CSP to color all **33 districts of Telangana (India)** while satisfying adjacency constraints.  

---

#### 📊 Graph Visualization
- **`telangana_graph.py`**  
  Generates a visual representation of the Telangana solution using:
  - `networkx`  
  - `matplotlib`  

---

#### 🔢 Sudoku Solver
- **`sudoku.py`**  
  Solves a standard **9×9 Sudoku puzzle** using CSP constraints:
  - Row constraints  
  - Column constraints  
  - 3×3 grid constraints  
  - Total: 27 AllDiff constraints  

---

#### 🔐 Cryptarithmetic Problem
- **`crypt-analysis_puzzle.py`**  
  Solves the puzzle:
