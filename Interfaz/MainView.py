import tkinter as tk
from Logica.Algoritmos import Grafo
import tkinter.messagebox as messagebox
import re


class GrafoVisualizer(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        tk.Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.grafo = Grafo(self.root) 
        self.root.title("Visualizador de Grafos")
        self.root.geometry("900x600")  # Establecer el tamaño de la ventana

        self.label_vertice = tk.Label(self.root, text="Ingrese un vértice:")
        self.label_vertice.place(relx=0.25, rely=0.3, anchor='center')

        self.textbox_vertice = tk.Entry(self.root)
        self.textbox_vertice.place(relx=0.25, rely=0.35, anchor='center')

        self.boton_agregar_vertice = tk.Button(self.root, text="Agregar Vértice", command=self.agregar_vertice)
        self.boton_agregar_vertice.place(relx=0.25, rely=0.4, anchor='center')

        self.label_arista = tk.Label(self.root, text="Ingrese una arista (en formato A--B):")
        self.label_arista.place(relx=0.75, rely=0.3, anchor='center')

        self.textbox_arista = tk.Entry(self.root)
        self.textbox_arista.place(relx=0.75, rely=0.35, anchor='center')

        self.boton_agregar_arista = tk.Button(self.root, text="Agregar Arista", command=self.agregar_arista)
        self.boton_agregar_arista.place(relx=0.75, rely=0.4, anchor='center')

        self.label_resultado_vertices = tk.Label(self.root, text="Vértices:")
        self.label_resultado_vertices.place(relx=0.25, rely=0.5, anchor='center')

        self.textbox_resultado_vertices = tk.Text(self.root, height=5, width=30)
        self.textbox_resultado_vertices.place(relx=0.25, rely=0.55, anchor='center')

        self.label_resultado_aristas = tk.Label(self.root, text="Aristas:")
        self.label_resultado_aristas.place(relx=0.75, rely=0.5, anchor='center')

        self.textbox_resultado_aristas = tk.Text(self.root, height=5, width=30)
        self.textbox_resultado_aristas.place(relx=0.75, rely=0.55, anchor='center')

        self.boton_visualizar_grafo = tk.Button(self.root, text="Visualizar Grafo", command=self.visualizar_grafo)
        self.boton_visualizar_grafo.place(relx=0.33, rely=0.7, anchor='center')

        self.boton_algoritmo_anchura = tk.Button(self.root, text="Algoritmo en Anchura", command=self.grafo.ejecutar_anchura)
        self.boton_algoritmo_anchura.place(relx=0.5, rely=0.7, anchor='center')

        self.boton_algoritmo_profundidad = tk.Button(self.root, text="Algoritmo en Profundidad", command=self.grafo.ejecutar_profundidad)
        self.boton_algoritmo_profundidad.place(relx=0.67, rely=0.7, anchor='center')

    def agregar_vertice(self):
        vertice = self.textbox_vertice.get().lower()  # Convertir a minúsculas
        if not vertice:  # Si el cuadro de texto está vacío
            messagebox.showerror("Error", "El cuadro de texto está vacío.")
            return
        if vertice in self.grafo.vertices:  # Si el vértice ya existe
            messagebox.showerror("Error", "El vértice ya existe.")
            return
        self.grafo.vertices.append(vertice)
        self.grafo.grafo.node(vertice)
        print("Vertices:", self.grafo.vertices)
        self.textbox_resultado_vertices.insert(tk.END, f"{vertice}\n")
        self.textbox_vertice.delete(0, tk.END)  # Limpiar el cuadro de texto

    def agregar_arista(self):
        arista = self.textbox_arista.get()
        if not arista:  # Si el cuadro de texto está vacío
            messagebox.showerror("Error", "El cuadro de texto está vacío.")
            return
        if not re.match(r"\w+--\w+", arista):  # Si la entrada no sigue la estructura correcta
            messagebox.showerror("Error", "La entrada no sigue la estructura correcta. (Ejemplo: A--B)")
            return
        a, b = arista.split("--")
        if a.lower() == b.lower():  # Si los elementos de la arista son iguales
            messagebox.showerror("Error", "Los elementos de la arista deben ser diferentes.")
            return
        if a.lower() not in self.grafo.vertices or b.lower() not in self.grafo.vertices:  # Si los elementos de la arista no existen en los vértices
            messagebox.showerror("Error", "Los elementos de la arista deben existir en los vértices.")
            return
        if {a.lower(), b.lower()} in [set(x.split("--")) for x in self.grafo.aristas]:  # Si la arista ya existe en cualquier orden
            messagebox.showerror("Error", "La arista ya existe.")
            return
        self.grafo.aristas.append(arista)
        self.grafo.grafo.edge(a, b)
        print("Aristas:", self.grafo.aristas)
        self.textbox_resultado_aristas.insert(tk.END, f"{arista}\n")
        self.textbox_arista.delete(0, tk.END)  # Limpiar el cuadro de texto

    def visualizar_grafo(self):
        if not self.grafo.vertices and not self.grafo.aristas:  # Si el grafo está vacío
            messagebox.showerror("Error", "El grafo está vacío.")
            return
        self.grafo.grafo.render('/Imagenes/grafo', format='png', view=False)
        self.grafo.show_image('/Imagenes/grafo.png', True)