import tkinter as tk
from functools import partial

def create_calculator_window():
    window = tk.Tk()
    window.geometry("500x600")
    window.title("出租车计价器")



    window.mainloop()

if __name__ == "__main__":
    create_calculator_window()