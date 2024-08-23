import tkinter as tk
import time

def loading_screen(seconds):
    root = tk.Tk()
    root.geometry("300x100")
    root.title("Loading...")

    progress_bar = tk.ttk.Progressbar(root, orient="horizontal", length=280, mode="determinate")
    progress_bar.pack(pady=30)

    for i in range(seconds * 10):
        progress_bar["value"] = i / 10
        root.update_idletasks()
        time.sleep(0.1)

    root.destroy()

# Exemplo de uso:
loading_screen(5)  # Simula o processo de carregamento em 5s