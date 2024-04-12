import tkinter as tk
from Interfaz.MainView import MainView

def main():
    root = tk.Tk()
    main_view = MainView(root)
    root.mainloop()

if __name__ == "__main__":
    main()