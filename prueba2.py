import json

import networkx as nx
from networkx.readwrite import json_graph


G = nx.DiGraph()

G.add_node("Daniel")
G.add_node("Javier")
G.add_node("Kimberly")
G.add_node("Fernando")

G.add_edge("Daniel", "Javier")
G.add_edge("Javier", "Kimberly")


for n in G:
    G.nodes[n]["name"] = n
# write json formatted data
d = json_graph.node_link_data(G)  # node-link format to serialize
# write json
json.dump(d, open("nodo.json", "w+"))
print("Wrote node-link JSON data to force/force.json")

