#-*- coding:UTF-8 -*-

def salvar_dados():
    try:
        f = open("encomenda.txt", "a")
        f.write("Destino:")
        f.write("%s\n" % destino.get())
        f.write("Descricao:")
        f.write("%s\n" % descricao.get())
        f.write("Endereco:")
        f.write("%s\n" % endereco.get("1.0", END))
        destino.set('Sao José dos Campos')
        descricao.delete(0, END)
        endereco.delete("1.0", END)
        f.close()
    except Exception as x:
        app.title('Erro de gravacao arquivo %s' %x)

def ler_destinos(arquivo):
    destinos = []
    f = open(arquivo)
    for linha in f:
        destinos.append(linha.rstrip())
    return destinos

from tkinter import *
app = Tk()
app.title('Head-Ex Logística e Transportes')
Label(app, text = "Destino:").pack()
destino = StringVar()
destino.set(None)

opcoes = ler_destinos("cidades.txt")
OptionMenu(app, destino, *opcoes).pack()

Label(app, text = "Descricao:").pack()
descricao = Entry(app)
descricao.pack()
Label(app, text = "Endereco:").pack()
endereco = Text(app)
endereco.pack()
Button(app, text = "Salvar", command = salvar_dados).pack()
app.mainloop()
