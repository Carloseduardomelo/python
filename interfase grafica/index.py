import tkinter as tk

# Cria uma nova janela
janela = tk.Tk()

#adicionando icon
janela.iconbitmap("interfase grafica/hack.ico")

# Define o título da janela
janela.title("Minha Janela")

# Define o tamanho da janela
janela.geometry("400x300")

#adicionando um texto na janela
text1 = tk.Label(janela , text='Ola mundo')
text1.pack()

# Cria um botão
botao = tk.Button(janela, text="Clique aqui", command='clicar')

#quando clicar no botao
def clicar():
    text1.config(text="carlos aqui")

# Adiciona o botão à janela
botao.pack()

# Inicia o loop da janela
janela.mainloop()
