from tkinter import * 
'''Ao utilizar o * isso indica que desejo importar todos os componentes desse módulo'''
from tkinter import ttk


cor1 = "#1e1f1e" # preta
cor2 = "#feffff" #branco
cor3 = "#38576b" #aazul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laracalcunja

janela =  Tk()
janela.title("Calculadora")
#aqui nomeamos
janela.geometry("240x380")

#aqui setamos tamanho
janela.config(bg=cor1)
'''estes passos importamos uma janela'''

'''Aqui iremo definir os frames '''
frame_display = Frame(janela, width=240, height=63,bg=cor3) #aqui eu criei a 1ª frame, ou seja um conjunto/ uma fatia dentro da minha janela dedicada com geometry 240x380
frame_display.grid(row=0,column=0) #Aqui eu sinalizei a posição primeira linha da primeira coluna

frame_corpo1 = Frame(janela, width=240, height=330, bg=cor3)#aqui eu criei a 2ª frame, dedicada a área de trabalho da calculadora
frame_corpo1.grid(row=2,column=0)

'''criando nossa função para recepcionar a lógica de calculo'''

# variável que receberá valores 
toda_entrada = ''

num_entrada = StringVar() #criamos uma variável que aceite string para ser utulizada dentro da nossa função

def entrada(event):
    global toda_entrada # tornando a variável global
    toda_entrada += str(event)
    calculo = eval('1+1') #estamos utilizando eval que se trata de uma função que calcula os operadores em python
    num_entrada.set(toda_entrada) #estamos chamando nossa variável esterna dentro da função

'''criando uma função para calcular'''

def calcular():
    global toda_entrada
    calculo = eval(toda_entrada)
    toda_entrada = ''
    num_entrada.set(calculo)
'''criando uma função para limpar tela'''

def clear():
    global toda_entrada #aqui tornamos a variável global pois ela recebeu um novo valor
    toda_entrada = ''
    num_entrada.set('')

'''Criando um Label'''
label_display = Label(frame_display, textvariable=num_entrada, width=34, height=3, padx=1,  relief=FLAT, anchor="e", justify=RIGHT, font=('Arial 9 bold'))#aqui eu sinalizei com uma Label que irei trabalhar ela dentro de uma frame --> repare que no width e height utilizamos número menores 
#padx=1,  
#relief=FLAT, --> 
# anchor="e", manter posicionado a direita
# justify=RIGHT, justificar a direita
# font=('Ivy 8 bold') conte
label_display.place(x=0, y=0) #a posição que ocupa dentro do objeto


'''Criando botões'''
b1 = Button(frame_corpo1, command=clear, text="C      ", width=15, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE) # aqui criamos um botão dentro da frame corpo1 e demos características e texto para o mesmo
b1.place(x=0, y=0)# 1º momento - aqui nó sinalizamos sua localização dentro da  frame ao qual ele pertence

#2º momento -  com o command = lambda:entrada('%') estamos sinalizando que ao clicar neste botão a função seja chamada para adicionar seu valor
b2 = Button(frame_corpo1, command= lambda:entrada('%'), text="%", width=6, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b2.place(x=122, y=0)

b3 = Button(frame_corpo1,command= lambda:entrada('/'), text="/", width=6, height=3, bg=cor5, foreground=cor2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b3.place(x=182, y=0)

b4 = Button(frame_corpo1,command= lambda:entrada('7'), text="7", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b4.place(x=0, y=60)

b5 = Button(frame_corpo1,command= lambda:entrada('8'), text="8", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b5.place(x=62, y=60)

b6 = Button(frame_corpo1,command= lambda:entrada('9'), text="9", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b6.place(x=122, y=60)

b7 = Button(frame_corpo1,command= lambda:entrada('*'), text="*", width=6, height=3,bg=cor5, foreground=cor2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b7.place(x=182, y=60)

b8 = Button(frame_corpo1,command= lambda:entrada('4'), text="4", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b8.place(x=0, y=122)

b9 = Button(frame_corpo1,command= lambda:entrada('5'), text="5", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b9.place(x=62, y=122)

b10 = Button(frame_corpo1,command= lambda:entrada('6'), text="6", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b10.place(x=122, y=122)

b11 = Button(frame_corpo1,command= lambda:entrada('-'), text="-", width=6, height=3,bg=cor5, foreground=cor2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b11.place(x=182, y=122)


b12 = Button(frame_corpo1,command= lambda:entrada('1'), text="1", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b12.place(x=0, y=184)

b13 = Button(frame_corpo1,command= lambda:entrada('2'), text="2", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b13.place(x=62, y=184)

b14 = Button(frame_corpo1,command= lambda:entrada('3'), text="3", width=6, height=3, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b14.place(x=122, y=184)

b15 = Button(frame_corpo1,command= lambda:entrada('+'), text="+", width=6, height=3,bg=cor5, foreground=cor2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b15.place(x=182, y=184)

b1 = Button(frame_corpo1,command= lambda:entrada('0'), text="0      ", width=15, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b1.place(x=0, y=246)

b2 = Button(frame_corpo1,command= lambda:entrada('.'), text=".", width=6, height=3, bg=cor4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b2.place(x=122, y=246)

b3 = Button(frame_corpo1,command= calcular, text="=", width=6, height=3, bg=cor5, foreground=cor2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b3.place(x=182, y=246)

# criando função para calcular


janela.mainloop() # esta função precisa estar no final

