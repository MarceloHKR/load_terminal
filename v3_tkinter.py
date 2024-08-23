import tkinter as tk

def loading_screen(root, seconds):
    splash_win = tk.Toplevel(root)
    splash_win.title("Splash Screen Example")
    splash_win.geometry("700x200")
    splash_win.overrideredirect(True)
    splash_label = tk.Label(splash_win, text="Hello World!", fg="green", font=('Times New Roman', 40))
    splash_label.pack(pady=20)

    def mainWin():
        splash_win.destroy()
        win = tk.Toplevel(root)
        win.title("Main Window")
        win.geometry("700x200")
        win_label = tk.Label(win, text="Main Window", font=('Helvetica', 25), fg="red")
        win_label.pack(pady=20)

    splash_win.after(seconds * 1000, mainWin)

root = tk.Tk()
loading_screen(root, 5)
root.mainloop()