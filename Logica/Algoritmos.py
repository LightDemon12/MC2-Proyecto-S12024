from graphviz import Graph
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import tkinter as tk
import queue

class Grafo:
    def __init__(self, tk_widget):
        self.tk_widget = tk_widget
        self.image_queue = queue.Queue()
        self.grafo = Graph(engine='neato')
        self.current_window = None
        self.vertices = []
        self.aristas = []
        self.vecinos = {}




    def ejecutar_anchura(self):
        if not self.vertices and not self.aristas:  # Si el grafo está vacío
            messagebox.showerror("Error", "El grafo está vacío.")
            return
        vertices_ordenados = sorted(self.vertices)
        aristas_ordenadas = sorted(self.aristas)
        print("Vertices ordenados:", vertices_ordenados)
        print("Aristas ordenadas:", aristas_ordenadas)
        if vertices_ordenados:
            nodo_inicial = vertices_ordenados[0]
            self.grafo.node(nodo_inicial, color='green')
        vertices_visitados = set()
        for i, arista in enumerate(aristas_ordenadas, start=1):
            a, b = arista.split("--")
            if a not in vertices_visitados or b not in vertices_visitados:
                self.grafo.edge(a, b, color='blue')
                vertices_visitados.add(a)
                vertices_visitados.add(b)
                self.grafo.render(f'/Imagenes/grafoAnchura_{i}', format='png', view=False)
                self.image_queue.put(f'/Imagenes/grafoAnchura_{i}.png')
        self.show_next_image()

    def ejecutar_profundidad(self):
        if not self.vertices and not self.aristas:  # Si el grafo está vacío
            messagebox.showerror("Error", "El grafo está vacío.")
            return
        def dfs(nodo, visitados, nodo_inicial, i=1):
            visitados.add(nodo)
            if nodo == nodo_inicial:
                self.grafo.node(nodo, color='red')
            else:
                self.grafo.node(nodo, color='green')
            self.grafo.render(f'/Imagenes/grafoProfundidad_{i}', format='png', view=False)
            self.image_queue.put(f'/Imagenes/grafoProfundidad_{i}.png')
            for vecino in self.vecinos.get(nodo, []):
                if vecino not in visitados:
                    self.grafo.edge(nodo, vecino, color='red')
                    dfs(vecino, visitados, nodo_inicial, i+1)
        self.grafo.clear()  # Limpiar el grafo antes de ejecutar DFS
        vertices_ordenados = sorted(self.vertices)
        aristas_ordenadas = sorted(self.aristas)
        # Construir diccionario de vecinos
        self.vecinos = {v: [] for v in vertices_ordenados}
        for arista in aristas_ordenadas:
            a, b = arista.split("--")
            self.vecinos[a].append(b)
            self.vecinos[b].append(a)
        print("Vertices ordenados:", vertices_ordenados)
        print("Aristas ordenadas:", aristas_ordenadas)
        if vertices_ordenados:
            nodo_inicial = vertices_ordenados[0]
            dfs(nodo_inicial, set(), nodo_inicial)
        self.show_next_image()

    def show_next_image(self):
        if self.current_window is not None:
            self.current_window.destroy()
        if not self.image_queue.empty():
            image_path = self.image_queue.get()
            is_last = self.image_queue.empty()
            self.show_image(image_path, is_last)

    def show_image(self, image_path, is_last):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.current_window = tk.Toplevel(self.tk_widget)
        self.current_window.geometry("+300+200")  
        label = tk.Label(self.current_window, image=photo)
        label.image = photo  
        label.pack(side=tk.LEFT)  
        if not is_last:
            self.current_window.after(2000, self.show_next_image)  
        self.current_window.protocol("WM_DELETE_WINDOW", self.show_next_image)  