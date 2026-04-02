from csp import CSP
from australia_coloring import MapColoringConstraint
from typing import Dict, List, Optional

variables: List[str] = [
    "Adilabad", "Kumurambheem Asifabad", "Nirmal", "Mancherial", 
    "Nizamabad", "Jagtial", "Peddapalli", "Jayashankar Bhupalpally", 
    "Mulugu", "Bhadradri Kothagudem", "Kamareddy", "Rajanna Sircilla", 
    "Karimnagar", "Hanumakonda", "Warangal Rural", "Mahabubabad", 
    "Khammam", "Medak", "Siddipet", "Jangaon", "Suryapet", 
    "Sangareddy", "Medchal Malkajgiri", "Yadadri Bhuvanagiri", 
    "Nalgonda", "Vikarabad", "Rangareddy", "Hyderabad", 
    "Mahabubnagar", "Narayanpet", "Jogulamba Gadwal", "Wanaparthy", 
    "Nagarkurnool"
]

domains: Dict[str, List[str]] = {}
for variable in variables:
    domains[variable] = ["Red", "Green", "Blue", "Yellow"]
    
csp: CSP[str, str] = CSP(variables, domains)

neighbors = {
    "Adilabad": ["Nirmal", "Kumurambheem Asifabad"],
    "Kumurambheem Asifabad": ["Adilabad", "Nirmal", "Mancherial"],
    "Nirmal": ["Adilabad", "Kumurambheem Asifabad", "Mancherial", "Jagtial", "Nizamabad"],
    "Mancherial": ["Kumurambheem Asifabad", "Nirmal", "Jagtial", "Peddapalli", "Jayashankar Bhupalpally"],
    "Nizamabad": ["Nirmal", "Jagtial", "Rajanna Sircilla", "Kamareddy"],
    "Jagtial": ["Nirmal", "Mancherial", "Peddapalli", "Karimnagar", "Rajanna Sircilla", "Nizamabad"],
    "Peddapalli": ["Mancherial", "Jayashankar Bhupalpally", "Karimnagar", "Jagtial"],
    "Jayashankar Bhupalpally": ["Mancherial", "Peddapalli", "Karimnagar", "Hanumakonda", "Mulugu"],
    "Mulugu": ["Jayashankar Bhupalpally", "Hanumakonda", "Warangal Rural", "Mahabubabad", "Bhadradri Kothagudem"],
    "Bhadradri Kothagudem": ["Mulugu", "Mahabubabad", "Khammam"],
    "Kamareddy": ["Nizamabad", "Rajanna Sircilla", "Siddipet", "Medak", "Sangareddy"],
    "Rajanna Sircilla": ["Nizamabad", "Jagtial", "Karimnagar", "Siddipet", "Kamareddy"],
    "Karimnagar": ["Jagtial", "Peddapalli", "Jayashankar Bhupalpally", "Hanumakonda", "Siddipet", "Rajanna Sircilla"],
    "Hanumakonda": ["Jayashankar Bhupalpally", "Warangal Rural", "Jangaon", "Siddipet", "Karimnagar"],
    "Warangal Rural": ["Hanumakonda", "Mulugu", "Mahabubabad", "Jangaon"],
    "Mahabubabad": ["Warangal Rural", "Mulugu", "Bhadradri Kothagudem", "Khammam", "Suryapet", "Jangaon"],
    "Khammam": ["Bhadradri Kothagudem", "Mahabubabad", "Suryapet"],
    "Medak": ["Kamareddy", "Siddipet", "Medchal Malkajgiri", "Sangareddy"],
    "Siddipet": ["Kamareddy", "Rajanna Sircilla", "Karimnagar", "Hanumakonda", "Jangaon", "Yadadri Bhuvanagiri", "Medchal Malkajgiri", "Medak"],
    "Jangaon": ["Siddipet", "Hanumakonda", "Warangal Rural", "Mahabubabad", "Suryapet", "Yadadri Bhuvanagiri"],
    "Suryapet": ["Jangaon", "Mahabubabad", "Khammam", "Nalgonda", "Yadadri Bhuvanagiri"],
    "Sangareddy": ["Kamareddy", "Medak", "Medchal Malkajgiri", "Rangareddy", "Vikarabad"],
    "Medchal Malkajgiri": ["Medak", "Siddipet", "Yadadri Bhuvanagiri", "Rangareddy", "Hyderabad", "Sangareddy"],
    "Yadadri Bhuvanagiri": ["Siddipet", "Jangaon", "Suryapet", "Nalgonda", "Rangareddy", "Medchal Malkajgiri"],
    "Nalgonda": ["Yadadri Bhuvanagiri", "Suryapet", "Nagarkurnool", "Rangareddy"],
    "Vikarabad": ["Sangareddy", "Rangareddy", "Mahabubnagar", "Narayanpet"],
    "Rangareddy": ["Vikarabad", "Sangareddy", "Medchal Malkajgiri", "Hyderabad", "Yadadri Bhuvanagiri", "Nalgonda", "Nagarkurnool", "Mahabubnagar"],
    "Hyderabad": ["Medchal Malkajgiri", "Rangareddy"],
    "Mahabubnagar": ["Vikarabad", "Rangareddy", "Nagarkurnool", "Wanaparthy", "Narayanpet"],
    "Narayanpet": ["Vikarabad", "Mahabubnagar", "Wanaparthy", "Jogulamba Gadwal"],
    "Jogulamba Gadwal": ["Narayanpet", "Wanaparthy"],
    "Wanaparthy": ["Jogulamba Gadwal", "Narayanpet", "Mahabubnagar", "Nagarkurnool"],
    "Nagarkurnool": ["Wanaparthy", "Mahabubnagar", "Rangareddy", "Nalgonda"]
}

# Add constraints efficiently
for district, adjacencies in neighbors.items():
    for adjacent in adjacencies:
        # add condition to prevent duplicate constraints (A->B and B->A)
        # but our CSP can handle duplicates, doing this ensures cleaner code
        csp.add_constraint(MapColoringConstraint(district, adjacent))

if __name__ == "__main__":
    print("Solving Telangana Map Coloring Problem...")
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    
    if solution is None:
        print("No solution found!")
    else:
        print("Solution for Telangana Map Coloring:")
        for state, color in solution.items():
            print(f"{state}: {color}")
