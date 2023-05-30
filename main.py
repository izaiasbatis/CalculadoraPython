from tkinter import * 
'''Ao utilizar o * isso indica que desejo importar todos os componentes desse módulo'''
from tkinter import ttk


cor1 = "#1e1f1e" # preta
janela =  Tk()
janela.title("Calculadora")
#aqui nomeamos
janela.geometry("235x318")
#aqui setamos tamanho

'''estes passos importamos uma janela'''
frame_display = Frame(janela, width=235, height=35, bg=cor1)
frame_display.grid(row=0,column=0)


janela.mainloop() # esta função precisa estar no final

