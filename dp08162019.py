# This problem was recently asked by Facebook:

# Given an undirected graph, determine if a cycle exists in the graph.

def find_cycle(graph):
    # Fill this in.
    marked = { u : False for u in graph }
    found_cycle = [False]

    for u in graph:
        for v in graph[u]:
            marked[v] = False

    for u in graph:   
        if not marked[u]:
            dfs_visit(graph, u, found_cycle, u, marked) 

        if found_cycle[0]:
            break
        
    return found_cycle[0]

def dfs_visit(G, u, found_cycle, pred_node, marked):
    if found_cycle[0]:
        return

    marked[u] = True

    for v in G[u]:
        if marked[v] and v != pred_node:
            found_cycle[0] = True
            return

        if not marked[v]:
            dfs_visit(G[u], v, found_cycle, u, marked)      

graph = {
    'a': {'a2':{}, 'a3':{} },
    'b': {'b2':{}},
    'c': {},
    # 'a2':{},
    # 'a3':{},
    # 'b2':{}
}
print (find_cycle(graph))
# False
graph['c'] = graph
print (find_cycle(graph))
# True
