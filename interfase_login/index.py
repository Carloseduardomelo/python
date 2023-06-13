import customtkinter as ctk

#definimdo o modo deles e o tema #
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#criando as interface #
janela = ctk.CTk()
janela.geometry("350x350")

#colocando um ico #
janela.iconbitmap("interfase_login/hack.ico")

#criando a função de click #
def clicar():
    print("login OK")

#criando um função de verificar senha #
def veri():
    if senha == "py":
        text02 = ctk.CTkLabel(janela, text='senha correta pode ir ')
        text02.pack(padx=10, pady=10)
    else:
        text02 = ctk.CTkLabel(janela, text="senha incorreta")
        text02.pack(padx=10, pady=10)

#criando um texto #
text01 = ctk.CTkLabel(janela, text='Fazer login')

#criando o input de E-mail #
email = ctk.CTkEntry(janela, 
                     placeholder_text="E-mail")

#criando o input da senha #
senha = ctk.CTkEntry(janela,
                     placeholder_text="senha")
                     #show="*")

#criando o botão de fazer login #
botao = ctk.CTkButton(janela, text="logar", 
                      command=veri)

#colocando padding entre os elementos #
text01.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

janela.mainloop()