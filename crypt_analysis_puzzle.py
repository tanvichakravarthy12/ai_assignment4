from csp import Constraint, CSP
from typing import Dict, List, Optional

class CryptarithmeticConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        actual_letters = ["T", "W", "O", "F", "U", "R"]
        letter_assigned = [assignment[l] for l in actual_letters if l in assignment]
        if len(letter_assigned) != len(set(letter_assigned)):
            return False

        
        if len(assignment) == len(self.variables):
            # TWO + TWO = FOUR
            t = assignment["T"]
            w = assignment["W"]
            o = assignment["O"]
            f = assignment["F"]
            u = assignment["U"]
            r = assignment["R"]
            c1 = assignment["C1"]
            c2 = assignment["C2"]
            c3 = assignment["C3"]
            
            
            if t == 0 or f == 0:
                return False
                
            if o + o != r + 10 * c1:
                return False
            if w + w + c1 != u + 10 * c2:
                return False
            if t + t + c2 != o + 10 * c3:
                return False
            if f != c3:
                return False
                
        return True

if __name__ == "__main__":
    variables: List[str] = ["T", "W", "O", "F", "U", "R", "C1", "C2", "C3"]
    domains: Dict[str, List[int]] = {}
    
    for letter in ["T", "W", "O", "F", "U", "R"]:
        domains[letter] = list(range(10))
        
    for carry in ["C1", "C2", "C3"]:
        domains[carry] = [0, 1]
        
    csp: CSP[str, int] = CSP(variables, domains)
    
    
    csp.add_constraint(CryptarithmeticConstraint(variables))
    
    print("Solving TWO + TWO = FOUR Cryptarithmetic Puzzle...")
    solution: Optional[Dict[str, int]] = csp.backtracking_search()
    
    if solution is None:
        print("No solution found!")
    else:
        print("Solution found:")
        print(f"  {solution['T']}{solution['W']}{solution['O']}")
        print(f"+ {solution['T']}{solution['W']}{solution['O']}")
        print("-------")
        print(f" {solution['F']}{solution['O']}{solution['U']}{solution['R']}")
        print(f"Assignment: {solution}")
