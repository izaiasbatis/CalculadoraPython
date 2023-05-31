from tkinter import * 
'''Ao utilizar o * isso indica que desejo importar todos os componentes desse módulo'''
from tkinter import ttk


cor1 = "#1e1f1e" # preta
cor2 = "#feffff" #branco
cor3 = "#38576b" #aazul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

janela =  Tk()
janela.title("Calculadora")
#aqui nomeamos
janela.geometry("235x318")

#aqui setamos tamanho
janela.config(bg=cor1)
'''estes passos importamos uma janela'''

'''Aqui iremo definir os frames '''
frame_display = Frame(janela, width=235, height=50,bg=cor3)
frame_display.grid(row=0,column=0)

frame_corpo = Frame(janela, width=235, height=18)
frame_corpo.grid(row=1,column=0)

frame_corpo = Frame(janela, width=235, height=250, bg=cor3)
frame_corpo.grid(row=2,column=0)

janela.mainloop() # esta função precisa estar no final

