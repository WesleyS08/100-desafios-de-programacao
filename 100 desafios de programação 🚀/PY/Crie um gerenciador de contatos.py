import json
import tkinter as tk
from tkinter import messagebox


def carregar_contatos():
    try:
        with open('contatos.json', 'r') as arquivo:
            contatos = json.load(arquivo)
    except FileNotFoundError:
        contatos = {}
    return contatos


def salvar_contatos(contatos):
    with open('contatos.json', 'w') as arquivo:
        json.dump(contatos, arquivo, indent=2)


def adicionar_contato(nome, telefone, email):
    contatos = carregar_contatos()
    contatos[nome] = {'Telefone': telefone, 'Email': email}
    salvar_contatos(contatos)
    messagebox.showinfo("Sucesso", f"Contato '{nome}' adicionado com sucesso!")


def listar_contatos():
    contatos = carregar_contatos()
    lista_contatos = "\nLista de Contatos:\n"
    for nome, info in contatos.items():
        lista_contatos += f"{nome}: Telefone - {info['Telefone']}, Email - {info['Email']}\n"
    messagebox.showinfo("Contatos", lista_contatos)


def mostrar_janela_adicionar_contato():
    janela_adicionar_contato = tk.Toplevel(janela)
    janela_adicionar_contato.title("Adicionar Contato")

    rotulo_nome = tk.Label(janela_adicionar_contato, text="Nome:")
    rotulo_nome.pack(pady=5)

    entry_nome = tk.Entry(janela_adicionar_contato)
    entry_nome.pack(pady=5)

    rotulo_telefone = tk.Label(janela_adicionar_contato, text="Telefone:")
    rotulo_telefone.pack(pady=5)

    entry_telefone = tk.Entry(janela_adicionar_contato)
    entry_telefone.pack(pady=5)

    rotulo_email = tk.Label(janela_adicionar_contato, text="E-mail:")
    rotulo_email.pack(pady=5)

    entry_email = tk.Entry(janela_adicionar_contato)
    entry_email.pack(pady=5)

    botao_adicionar = tk.Button(
        janela_adicionar_contato, text="Adicionar", command=lambda: adicionar_contato(entry_nome.get(), entry_telefone.get(), entry_email.get()))
    botao_adicionar.pack(pady=10)


# Criar janela principal
janela = tk.Tk()
janela.title("Gerenciador de Contatos")

# Criar botões para a interface gráfica
botao_adicionar_contato = tk.Button(
    janela, text="Adicionar Contato", command=mostrar_janela_adicionar_contato)
botao_adicionar_contato.pack(pady=20)

botao_listar_contatos = tk.Button(
    janela, text="Listar Contatos", command=listar_contatos)
botao_listar_contatos.pack(pady=20)

# Rodar a janela
janela.mainloop()
