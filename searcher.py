# -*- coding:utf-8 -*-

"""
brunolcarli@gmail.com
"""


from tkinter import *
import tkinter.messagebox



def engine(db):     # Função que vai buscar a entrada no arquivo_morto
    x = inp.get()   # captura a entrada do usuario
    if x == '':     # se a caixa de entrada estiver vazia...
        l = Label(frm, text='Caixa de texto vazia', bg='red')  # ...da nisso
        l.pack()

    else:
        for lines in db:
            if x in lines:
                l = Label(frm, text=lines, bg='white')
                l.pack()
                inp.delete(0, END)


    if x not in db: # quando nao mais encontrar o que procura
        l = Label(frm, text='Fim da busca', bg='orange')
        l.pack()
        inp.delete(0, END)





def busca():
    global frm       #acesso ao frame manipulavel
    frm.destroy()    #limpar tudo que há no frame atual
    frm = Frame(root, bg = 'white') #readicionar o frame na janela
    o = option.get() #define qual ação à ser tomada


    #AÇÃO 1
    if o == 'Buscar no morto':
        db = open('arquivo_morto', 'r')  # abre arquivo_morto alvo em modo de leitura
        engine(db)                 # processa o arquivo_morto
        db.close()                 # fechar o arquivo_morto

    #AÇÃO 2
    elif o == 'Inserir no morto':
        if inp.get() == '':  # se a caixa de entrada estiver vazia...
            l = Label(frm, text='Caixa de texto vazia', bg='red')  # ...da nisso
            l.pack()
        else:
            db = open('arquivo_morto', 'a')  #abrir o arquivo_morto alvo em modo 'append' para anexar dados
            db.write('\n'+ inp.get())          #pula uma linha e escreve o que estiver no Entry
            tkinter.messagebox.showinfo('Concluído', 'Inserido com sucesso')
            l = Label(frm, text='Inserido com sucesso', bg = 'white')
            l.pack()
            inp.delete(0, END)         #sempre limpar o Entry
            db.close()

    #AÇÃO 3
    elif o == 'Buscar no atual':
        db = open('arquivo_atual', 'r') # igual ação um, mas em outro arquivo_morto
        engine(db)
        db.close()

    # Caso o menu não tenha sido selecionado...
    else:
        tkinter.messagebox.showerror("Atenção!", "Escolha uma das opções na caixa")
        l = Label(frm, text='Escolha uma opção', bg = 'red')  # ... da nisso
        l.pack()
        inp.delete(0, END)
    frm.pack()  #anexamos o resultado na janela


"""CONSTRUINDO A JANELA"""
root = Tk()
root.title("Buscador")
root.geometry("500x400+200+100")

"""ROTULOS INDICADORES/TITLOS"""
Label(root, text="Gerenciador de busca").pack()
Label(root, text="Insira o Nome").pack()

"""CAIXA ENTRY"""
inp = Entry(root)
inp.pack()

Label(root, text="Selecione uma tarefa:").pack()

"""VARIÁVEIS PARA A CAIXA DE OPÇÕES"""
option = StringVar()
option.set('Escolha uma opção')

"""CAIXA DE OPÇÕES"""
opcoes = ['Buscar no morto', 'Inserir no morto', 'Buscar no atual']
OptionMenu(root, option, *opcoes).pack()

"""BOTÃO"""
btn = Button(root, text = "Confirma", command = busca)
btn.pack()

"""FRAME MANIPULAVEL"""
frm = Frame(root)
frm.pack()

root.mainloop()