import tkinter.font
from tkinter import *
from tkinter import font

app = Tk()

app.title('IMC')
app.iconbitmap('icon.ico')
app.geometry('500x300')
app.configure(background='#FFAC2B')

#FUNÇÃO CALCULAR
def calcular():

    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso/(altura*altura)

    if (imc < 18.5):
        resultado['text']= 'IMC: {:.2f} - Abaixo do Peso'.format(imc)
    else:
        if(imc >= 18.5 and imc <= 24.9):
            resultado['text'] = 'IMC: {:.2f} - Peso Ideal'.format(imc)
        else:
            if(imc >= 25 and imc <= 29.9):
                resultado['text'] = 'IMC: {:.2f} - Sobrepeso'.format(imc)
            else:
                if(imc >= 30 and imc <= 34.9):
                    resultado['text'] = 'IMC: {:.2f} - Obesidade Grau I'.format(imc)
                else:
                    if(imc >= 35 and imc <= 39.9):
                        resultado['text'] = 'IMC: {:.2f} - Obesidade Grau II'.format(imc)
                    else:
                        if(imc >= 40):
                            resultado['text'] = 'IMC: {:.2f} - Obesidade Grau III ou Mórbida'.format(imc)
                        else:
                            resultado['text'] = 'IMC: {:.2f} - ERRO!'.format(imc)

#_--------------

#FONTES
title = font.Font(family='Helvetica', size='15', weight='bold')
text = font.Font(family='Times New Roman', size='13', weight='bold')
botaotexto = font.Font(family='Times New Roman', size='10', weight='bold')
#------

#TITULO
Label(app, text='CALCULE AQUI SEU IMC', bg='#D6E319', font=title).place(x=10, y=10, width=330)
#------

#LABEL PESO
Label(app, text='Insira seu peso: ', bg='#28FA7C', font=text).place(x=10, y=50, width=135)
#----------

#ENTRY PESO
entry_peso = Entry(app)
entry_peso.place(x=150, y=53)
#----------

#LABEL KG
Label(app, text='Ex: 85', font=text, bg='black', fg='white').place(x=280, y=53, width=60, height=19)
#--------

#LABEL ALTURA
Label(app, text='Insira sua altura: ', bg='#28FA7C', font=text).place(x=10, y=100)
#----------

#ENTRY ALTURA
entry_altura = Entry(app)
entry_altura.place(x=150, y=103)
#----------

#LABEL CM
Label(app, text='Ex: 192', font=text, bg='black', fg='white').place(x=280, y=103, height=19)
#--------

#BOTÃO CALCULAR
Button(app, text='CALCULAR', font=botaotexto, command=calcular).place(x=10, y=133)
#-------------


#LABEL RESULTADO
resultado = Label(app, text='asd')
resultado.place(x=10, y=165, width=330, height=50)

app.mainloop()
