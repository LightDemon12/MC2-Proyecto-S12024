def edges_to_graph(edges):
    graph = {}
    for edge in edges:
        vertex1, vertex2 = edge.split("--")
        if vertex1 not in graph:
            graph[vertex1] = []
        if vertex2 not in graph:
            graph[vertex2] = []
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    return graph

def DFS(graph, start, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path.append(start)
    for next_vertex in sorted(set(graph[start]) - visited):
        DFS(graph, next_vertex, visited, path)
    return path

def generate_graph_with_path(edges, path):
    from graphviz import Digraph
    dot = Digraph()

    for edge in edges:
        vertex1, vertex2 = edge.split("--")
        dot.node(vertex1)
        dot.node(vertex2)
        if vertex1 in path and vertex2 in path:
            dot.edge(vertex1, vertex2, color="red")
        else:
            dot.edge(vertex1, vertex2)

    dot.format = 'pdf'
    dot.render('Imagenes/graph.gv', view=True)

def run_DFS(vertices, edges):
    graph = edges_to_graph(edges)
    
    if not graph:
        print("No se proporcionaron aristas.")
        return
    
    # Determinar el vértice inicial
    start_vertex = vertices[0]  # Usar el primer vértice de la lista de vértices
    
    if start_vertex in graph:
        path = DFS(graph, start_vertex)
        generate_graph_with_path(edges, path)
    else:
        print(f"El vértice de inicio {start_vertex} no está en el grafo.")