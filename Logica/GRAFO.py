from graphviz import Digraph

def generate_graph(edges):
    dot = Digraph()

    # Añadir vértices y aristas al gráfico
    for edge in edges:
        vertex1, vertex2 = edge.split("--")
        dot.node(vertex1)
        dot.node(vertex2)
        dot.edge(vertex1, vertex2)

    # Generar el gráfico y guardarlo como una imagen .jpg
    dot.format = 'jpg'
    dot.render('Imagenes/grafo.gv', view=False)