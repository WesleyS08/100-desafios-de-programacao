import tkinter as tk
from tkinter import ttk
import re


class ValidadorSenha:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Senha")

        self.label_senha = ttk.Label(root, text="Digite a senha:")
        self.label_senha.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.entry_senha = ttk.Entry(root, show="*", width=20)
        self.entry_senha.grid(column=1, row=0, padx=10, pady=5)

        self.botao_validar = ttk.Button(
            root, text="Validar Senha", command=self.validar_senha)
        self.botao_validar.grid(column=0, row=1, columnspan=2, pady=10)

        self.label_resultado = ttk.Label(root, text="")
        self.label_resultado.grid(
            column=0, row=2, columnspan=2, padx=10, pady=5)

    def validar_senha(self):
        senha = self.entry_senha.get()

        # Critérios simples de validação de senha (ajuste conforme necessário)
        if len(senha) < 8:
            resultado = "A senha deve ter pelo menos 8 caracteres."
        elif not re.search("[a-z]", senha):
            resultado = "A senha deve conter pelo menos uma letra minúscula."
        elif not re.search("[A-Z]", senha):
            resultado = "A senha deve conter pelo menos uma letra maiúscula."
        elif not re.search("[0-9]", senha):
            resultado = "A senha deve conter pelo menos um número."
        else:
            resultado = "A senha é válida."

        self.label_resultado.config(text=resultado)


if __name__ == "__main__":
    root = tk.Tk()
    validador_senha = ValidadorSenha(root)
    root.mainloop()
