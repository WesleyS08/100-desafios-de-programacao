import tkinter as tk
from tkinter import ttk
import re


class ValidadorEmail:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de E-mail")

        self.label_email = ttk.Label(root, text="Digite o endereço de e-mail:")
        self.label_email.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.entry_email = ttk.Entry(root, width=40)
        self.entry_email.grid(column=1, row=0, padx=10, pady=5)

        self.botao_validar = ttk.Button(
            root, text="Validar E-mail", command=self.validar_email)
        self.botao_validar.grid(column=0, row=1, columnspan=2, pady=10)

        self.label_resultado = ttk.Label(root, text="")
        self.label_resultado.grid(
            column=0, row=2, columnspan=2, padx=10, pady=5)

    def validar_email(self):
        endereco_email = self.entry_email.get()

        # Definir a expressão regular para validar e-mails
        padrao_email = re.compile(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        # Verificar se o e-mail corresponde ao padrão
        if padrao_email.match(endereco_email):
            resultado = "O endereço de e-mail é válido."
        else:
            resultado = "O endereço de e-mail é inválido."

        self.label_resultado.config(text=resultado)


if __name__ == "__main__":
    root = tk.Tk()
    validador_email = ValidadorEmail(root)
    root.mainloop()
