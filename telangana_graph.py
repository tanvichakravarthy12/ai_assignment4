import networkx as nx
import matplotlib.pyplot as plt
from telangana_coloring import variables, domains, csp, neighbors

def draw_telangana_map():
    
    solution = csp.backtracking_search()
    if solution is None:
        print("No solution found for graph visualization!")
        return
        
    G = nx.Graph()
    for district in variables:
        G.add_node(district)
        
    for district, adjacencies in neighbors.items():
        for adjacent in adjacencies:
            G.add_edge(district, adjacent)
            
    
    
    pos = {
        "Adilabad": (0, 10),
        "Kumurambheem Asifabad": (2, 9.5),
        "Nirmal": (-1, 8.5),
        "Mancherial": (1.5, 8),
        "Nizamabad": (-2, 7.5),
        "Jagtial": (0, 7.5),
        "Peddapalli": (1.5, 6.5),
        "Jayashankar Bhupalpally": (3, 6),
        "Mulugu": (4, 5.5),
        "Bhadradri Kothagudem": (5, 4.5),
        "Kamareddy": (-2, 6.5),
        "Rajanna Sircilla": (-0.5, 6.5),
        "Karimnagar": (0.5, 6),
        "Hanumakonda": (1.5, 5),
        "Warangal Rural": (2.5, 4.8),
        "Mahabubabad": (3, 4),
        "Khammam": (4, 3),
        "Medak": (-1.5, 5),
        "Siddipet": (0, 5),
        "Jangaon": (1.5, 4),
        "Suryapet": (2.5, 2.5),
        "Sangareddy": (-2, 4),
        "Medchal Malkajgiri": (-0.5, 4),
        "Yadadri Bhuvanagiri": (1, 3.5),
        "Nalgonda": (1.5, 2),
        "Vikarabad": (-3, 3),
        "Rangareddy": (-1, 3),
        "Hyderabad": (-0.5, 3.5),
        "Mahabubnagar": (-1.5, 1.5),
        "Narayanpet": (-3, 1),
        "Jogulamba Gadwal": (-2.5, 0),
        "Wanaparthy": (-1.5, 0.5),
        "Nagarkurnool": (0, 1)
    }

    
    for node in G.nodes():
        if node not in pos:
            pos[node] = (0, 0)
            
    color_map = []
    color_dict = {
        "Red": "#FF9999",
        "Green": "#99FF99",
        "Blue": "#9999FF",
        "Yellow": "#FFFF99"
    }
    
    for node in G:
        color_map.append(color_dict.get(solution.get(node, "Red")))
        
    plt.figure(figsize=(12, 12))
    nx.draw(G, pos, node_color=color_map, with_labels=True, 
            node_size=2500, font_size=8, font_weight="bold", 
            edge_color="gray", width=1.5)
            
    plt.title("Telangana Districts Map Coloring CSP Solution", size=16)
    plt.savefig("telangana_map_solution.png", dpi=300, bbox_inches='tight')
    print("Graph visualization saved to telangana_map_solution.png")

if __name__ == "__main__":
    draw_telangana_map()
