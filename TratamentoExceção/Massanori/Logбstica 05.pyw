def salvar_dados(): 
    f = open("encomenda.txt", "a")    
    f.write("Destino:") 
    f.write("%s\n" % destino.get()) 
    f.write("Descrição:") 
    f.write("%s\n" % descricao.get()) 
    f.write("Endereço:") 
    f.write("%s\n" % endereco.get("1.0", END)) 
    destino.set('Jacareí') 
    descricao.delete(0, END) 
    endereco.delete("1.0", END)
    f.close()
def ler_destinos(arquivo): 
    destinos = [] 
    f = open(arquivo) 
    for linha in f: destinos.append(linha.rstrip())
    f.close()
    destinos.sort()
    return destinos
from tkinter import * 
app = Tk() 
app.title('Head-Ex Logística e Transportes') 
Label(app, text = "Destino:").pack() 
destino = StringVar() 
destino.set('Jacareí') 
opcoes = ler_destinos("cidades.txt") 
OptionMenu(app, destino, *opcoes).pack()
Label(app, text = "Descrição:").pack() 
descricao = Entry(app) 
descricao.pack() 
Label(app, text = "Endereço:").pack() 
endereco = Text(app) 
endereco.pack() 
Button(app, text = "Salvar", command = salvar_dados).pack() 
app.mainloop() 

