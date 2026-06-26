import tkinter as tk

janela = tk.Tk()

imagem = tk.PhotoImage(file="sprites/corpo/corpo1.png")

label = tk.Label(janela, image=imagem)
label.pack()

janela.mainloop()