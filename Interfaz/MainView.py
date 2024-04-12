import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import itertools
import re

class MainView:
    def __init__(self, master):
        self.master = master
        master.title("Proyecto de Grafos")
        master.geometry("1200x720")

        self.label = tk.Label(master, text="Proyecto de Grafos")
        self.label.grid(row=0, column=0, columnspan=2)

        # Carga las imágenes
        self.images = [ImageTk.PhotoImage(Image.open(f"Imagenes/{img_name}").resize((600, 360), Image.LANCZOS)) 
                       for img_name in ["d63e0568a5eaaf1c0b2bdc8d6ccadb04.jpg", "eb3875fb5cab1f7933d5c96fd2b0757c.jpg"]]
        self.image_panel1 = tk.Label(master, image=self.images[0])
        self.image_panel1.grid(row=1, column=0)
        self.image_panel2 = tk.Label(master)
        self.image_panel2.grid(row=1, column=1)

        # Inicia el ciclo de cambio de imágenes
        self.image_cycle = itertools.cycle(self.images)
        self.change_image()

        self.default_vertex_message = "Ingrese el vértice"
        self.default_edge_message = "Ingrese la arista en formato A--B"
        self.edge_pattern = re.compile(r"^[A-Za-z0-9]+--[A-Za-z0-9]+$")

        self.vertex_entry = tk.Entry(master)
        self.vertex_entry.grid(row=2, column=0)
        self.vertex_entry.insert(0, self.default_vertex_message)
        self.vertex_entry.bind("<Button-1>", self.clear_vertex_entry)

        self.edge_entry = tk.Entry(master, width=50)
        self.edge_entry.grid(row=2, column=1)
        self.edge_entry.insert(0, self.default_edge_message)
        self.edge_entry.bind("<Button-1>", self.clear_edge_entry)

        self.vertex_button = tk.Button(master, text="Agregar vértice", command=self.add_vertex)
        self.vertex_button.grid(row=3, column=0)

        self.edge_button = tk.Button(master, text="Agregar arista", command=self.add_edge)
        self.edge_button.grid(row=3, column=1)

        self.vertex_text = tk.Text(master, height=5, width=30)
        self.vertex_text.grid(row=4, column=0)

        self.edge_text = tk.Text(master, height=5, width=30)
        self.edge_text.grid(row=4, column=1)

        # Crea un menú ficticio para evitar el menú predeterminado
        master.option_add('*tearOff', False)
        menubar = tk.Menu(master)
        master['menu'] = menubar
        menu_file = tk.Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')

        # Crea la barra de menú
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        # Crea el menú de algoritmos
        self.algorithm_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Algoritmos", menu=self.algorithm_menu)
        self.algorithm_menu.add_command(label="Generar Grafo", command=self.generate_graph)
        self.algorithm_menu.add_command(label="Algoritmo de búsqueda en anchura", command=self.run_algorithm1)
        self.algorithm_menu.add_command(label="Algoritmo de búsqueda en profundidad", command=self.run_algorithm2)

    def change_image(self):
        # Cambia la imagen en el panel derecho
        self.image_panel2.config(image=next(self.image_cycle))
        # Programa el próximo cambio de imagen
        self.master.after(2000, self.change_image)

    def clear_vertex_entry(self, event):
        self.vertex_entry.delete(0, tk.END)

    def clear_edge_entry(self, event):
        self.edge_entry.delete(0, tk.END)

    def add_vertex(self):
        vertex = self.vertex_entry.get()
        if vertex == "" or vertex == self.default_vertex_message:
            messagebox.showerror("Error", "Por favor, ingrese un vértice.")
        else:
            self.vertex_text.insert(tk.END, f"Vértice agregado: {vertex}\n")

    def add_edge(self):
        edge = self.edge_entry.get()
        if edge == "" or edge == self.default_edge_message or not self.edge_pattern.match(edge):
            messagebox.showerror("Error", "Por favor, ingrese una arista en formato A--B.")
        else:
            self.edge_text.insert(tk.END, f"Arista agregada: {edge}\n")

    def generate_graph(self):
        vertex = self.vertex_entry.get()
        edge = self.edge_entry.get()
        # Aquí puedes llamar a tus funciones para generar el grafo y aplicar los algoritmos
        print("Vértice: ", vertex)
        print("Arista: ", edge)

    def run_algorithm1(self):
        # Aquí puedes llamar a tu primer algoritmo
        print("Ejecutando algoritmo de búsqueda en anchura")

    def run_algorithm2(self):
        # Aquí puedes llamar a tu segundo algoritmo
        print("Ejecutando algoritmo de búsqueda en profundidad")