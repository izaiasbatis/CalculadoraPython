from tkinter import *
from tkinter import ttk

cor1 = '#1e1f1e'
janela = Tk()
janela.title("Calculadora")
janela.geometry("250x300")
janela_frame = Frame(janela, width=250, height=30, bg=cor1)
janela_frame.grid(row=0,column=0)
janela.mainloop()
