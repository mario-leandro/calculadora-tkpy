from tkinter import *

#Criar Janela
janelaPrincipal = Tk()
janelaPrincipal.title("Calculadora")

# Criar funções - Ações
def inserir(valor):
    display.insert(END, valor)

def limpar():
    display.delete(0, END)

def calcular():
    resultado = eval(display.get())
    display.delete(0, END)
    display.insert(END, resultado)

# Criar visor para mostrar resultados
display = Entry(janelaPrincipal, font="Arial 20 bold", bg="#F6F6F6", fg="#000000", width=19)
display.pack() # Ativar o visor

# Criar painel para inserir os números
painel = Frame(janelaPrincipal)

## Criar botões - todos os botões
# Números
botao_1 = Button(painel, bg="#222222", fg="white", bd=1, text="1", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("1"))
botao_2 = Button(painel, bg="#222222", fg="white", bd=1, text="2", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("2"))
botao_3 = Button(painel, bg="#222222", fg="white", bd=1, text="3", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("3"))
botao_4 = Button(painel, bg="#222222", fg="white", bd=1, text="4", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("4"))
botao_5 = Button(painel, bg="#222222", fg="white", bd=1, text="5", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("5"))
botao_6 = Button(painel, bg="#222222", fg="white", bd=1, text="6", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("6"))
botao_7 = Button(painel, bg="#222222", fg="white", bd=1, text="7", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("7"))
botao_8 = Button(painel, bg="#222222", fg="white", bd=1, text="8", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("8"))
botao_9 = Button(painel, bg="#222222", fg="white", bd=1, text="9", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("9"))
botao_0 = Button(painel, bg="#222222", fg="white", bd=1, text="0", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("0"))

# Especiais
botao_soma = Button(painel, bg="orange", fg="white", bd=1, text="+", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("+"))
botao_subtracao = Button(painel, bg="orange", fg="white", bd=1, text="-", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("-"))
botao_multiplicacao = Button(painel, bg="orange", fg="white", bd=1, text="X", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("*"))
botao_divisao = Button(painel, bg="orange", fg="white", bd=1, text="/", font="Arial 16 bold", width=5, height=3, command=lambda: inserir("/"))
botao_resultado = Button(painel, bg="orange", fg="white", bd=1, text="=", font="Arial 16 bold", width=5, height=3, command=calcular)
botao_reset = Button(painel, bg="orange", fg="white", bd=1, text="C", font="Arial 16 bold", width=5, height=3, command=limpar)

#Primeira Linha
botao_7.grid(row=0, column=0)
botao_8.grid(row=0, column=1)
botao_9.grid(row=0, column=2)
botao_divisao.grid(row=0, column=3)

#Segunda Linha
botao_4.grid(row=1, column=0)
botao_5.grid(row=1, column=1)
botao_6.grid(row=1, column=2)
botao_multiplicacao.grid(row=1, column=3)

#Terceira Linha
botao_1.grid(row=2, column=0)
botao_2.grid(row=2, column=1)
botao_3.grid(row=2, column=2)
botao_soma.grid(row=2, column=3)

#Quarta Linha
botao_0.grid(row=3, column=0)
botao_resultado.grid(row=3, column=1)
botao_reset.grid(row=3, column=2)
botao_subtracao.grid(row=3, column=3)


# Ativar o painel, depois de todos os botões
painel.pack()

#Abrir a janela
mainloop()