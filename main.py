import tkinter as tk
from Interfaz.MainView import GrafoVisualizer

if __name__ == "__main__":
    root = tk.Tk()
    app = GrafoVisualizer(root)
    root.mainloop()