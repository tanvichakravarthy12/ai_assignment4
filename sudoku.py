from csp import Constraint, CSP
from typing import Dict, List, Optional

class SudokuConstraint(Constraint[str, int]):
    def __init__(self, variables: List[str]) -> None:
        super().__init__(variables)

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # Check if all assigned variables in this constraint have different values
        assigned_values = [assignment[var] for var in self.variables if var in assignment]
        return len(assigned_values) == len(set(assigned_values))

if __name__ == "__main__":
    variables: List[str] = []
    # Grid variables A1..I9
    rows = "ABCDEFGHI"
    cols = "123456789"
    for r in rows:
        for c in cols:
            variables.append(r + c)
            
    
    initial_grid = {
        'A3': 3, 'A5': 2, 'A7': 6,
        'B1': 9, 'B4': 3, 'B6': 5, 'B9': 1,
        'C3': 1, 'C4': 8, 'C6': 6, 'C7': 4,
        'D3': 8, 'D4': 1, 'D6': 2, 'D7': 9,
        'E1': 7, 'E9': 8,
        'F3': 6, 'F4': 7, 'F6': 8, 'F7': 2,
        'G3': 2, 'G4': 6, 'G6': 9, 'G7': 5,
        'H1': 8, 'H4': 2, 'H6': 3, 'H9': 9,
        'I3': 5, 'I5': 1, 'I7': 3
    }

    domains: Dict[str, List[int]] = {}
    for var in variables:
        if var in initial_grid:
            domains[var] = [initial_grid[var]]
        else:
            domains[var] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    csp: CSP[str, int] = CSP(variables, domains)

   
    # Rows
    for r in rows:
        csp.add_constraint(SudokuConstraint([r + c for c in cols]))
        
    # Columns
    for c in cols:
        csp.add_constraint(SudokuConstraint([r + c for r in rows]))
        
    
    for r_idx in [0, 3, 6]:
        for c_idx in [0, 3, 6]:
            block_vars = []
            for i in range(3):
                for j in range(3):
                    block_vars.append(rows[r_idx + i] + cols[c_idx + j])
            csp.add_constraint(SudokuConstraint(block_vars))

    print("Solving Sudoku CSP from Figure 5.4...")
    solution: Optional[Dict[str, int]] = csp.backtracking_search()
    
    if solution is None:
        print("No solution found!")
    else:
        print("Solution found:")
        for r in rows:
            row_vals = []
            for c in cols:
                row_vals.append(str(solution[r + c]))
            print(" ".join(row_vals))
