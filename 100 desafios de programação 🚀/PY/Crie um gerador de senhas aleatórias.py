import tkinter as tk
from tkinter import messagebox
import secrets
import string


def gerar_senha():
    tamanho = int(entry.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha


def mostrar_senha_aleatoria():
    senha_aleatoria = gerar_senha()
    messagebox.showinfo("Senha Aleatória",
                        f'A senha aleatória gerada é:\n{senha_aleatoria}')


# Criar janela
janela = tk.Tk()
janela.title("Gerador de Senha Aleatória")

rotulo = tk.Label(janela, text="Digite o tamanho da senha:")
rotulo.pack(pady=2)

# Criar entrada (entry) para o número
entry = tk.Entry(janela)
entry.pack(pady=25)

# Criar botão para gerar senha aleatória
botao_gerar_senha = tk.Button(
    janela, text="Gerar Senha Aleatória", command=mostrar_senha_aleatoria)
botao_gerar_senha.pack(pady=20)

# Rodar a janela
janela.mainloop()
