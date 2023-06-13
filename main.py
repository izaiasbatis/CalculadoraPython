from tkinter import *
from tkinter import ttk

# criando cor
cor1='#021fb0'
#criando objeto calculadora
tela =  Tk()
tela.title("Calculadora")
tela.geometry("200x300")

#criando variável para utilizar na função
num = ''
def entrada(event):
    global num
    num += event
    num_conversao.set(num)

#limpar

def clear():
    global num
    num = ''
    num_conversao.set('')



#calcular

def calcular():
    global num
    num_conversao.set(eval(num))
    num = ('')
    
num_conversao = StringVar()
#criando Frames ou seja, as divisões esperadadas no objeto
tela_frame= Frame(tela,width=250, height=50, bg=cor1)
tela_frame.grid(row=0, column=0)

tela_label = Label(tela_frame, textvariable=num_conversao,anchor='e', width=10, height=2)
tela_label.grid(row=0,column=0)

inter_frame= Frame(tela,width=250, height=10)
inter_frame.grid(row=1, column=0)

corpo_frame= Frame(tela,width=250, height=240, bg=cor1)
corpo_frame.grid(row=2, column=0)

#criando itens dentro do frame
tc1_frame = Button(corpo_frame, command=clear, text = 'C', width=13, height=2)
tc1_frame.place(x=0,y=0)

tc1_1_frame = Button(corpo_frame,command = lambda : entrada('%') , text = '%', width=5, height=2)
tc1_1_frame.place(x=106,y=0)

tc1_2_frame = Button(corpo_frame,command = lambda : entrada('/') , text = '/', width=5, height=2)
tc1_2_frame.place(x=156,y=0)

tc2_frame = Button(corpo_frame,command = lambda : entrada('7') , text = '7', width=5, height=2)
tc2_frame.place(x=0,y=50)

tc2_1_frame = Button(corpo_frame,command = lambda : entrada('8') , text = '8', width=5, height=2)
tc2_1_frame.place(x=55,y=50)

tc2_2_frame = Button(corpo_frame,command = lambda : entrada('9') , text = '9', width=5, height=2)
tc2_2_frame.place(x=106,y=50)

tc2_3_frame = Button(corpo_frame,command = lambda   : entrada('+') , text = '+', width=5, height=2)
tc2_3_frame.place(x=156,y=50)

tc3_frame = Button(corpo_frame,command = lambda : entrada('4') , text = '4', width=5, height=2)
tc3_frame.place(x=0,y=100)

tc3_1_frame = Button(corpo_frame,command = lambda : entrada('5') , text = '5', width=5, height=2)
tc3_1_frame.place(x=55,y=100)

tc3_2_frame = Button(corpo_frame,command = lambda : entrada('6') , text = '6', width=5, height=2)
tc3_2_frame.place(x=106,y=100)

tc3_3_frame = Button(corpo_frame,command = lambda : entrada('*') , text = '*', width=5, height=2)
tc3_3_frame.place(x=156,y=100)

tc4_frame = Button(corpo_frame,command = lambda : entrada('1') , text = '1', width=5, height=2)
tc4_frame.place(x=0,y=150)

tc4_1_frame = Button(corpo_frame,command = lambda : entrada('2') , text = '2', width=5, height=2)
tc4_1_frame.place(x=55,y=150)

tc4_2_frame = Button(corpo_frame,command = lambda : entrada('3') , text = '3', width=5, height=2)
tc4_2_frame.place(x=106,y=150)

tc4_3_frame = Button(corpo_frame,command = lambda : entrada('-') , text = '-', width=5, height=2)
tc4_3_frame.place(x=156,y=150)

tc1_frame = Button(corpo_frame,command = lambda : entrada('0') , text = '0', width=13, height=2)
tc1_frame.place(x=0,y=200)

tc1_1_frame = Button(corpo_frame,command = lambda : entrada('.') , text = '.', width=5, height=2)
tc1_1_frame.place(x=106,y=200)

tc1_2_frame = Button(corpo_frame,command=calcular, text = '=', width=5, height=2)
tc1_2_frame.place(x=156,y=200)



tela.mainloop()
