import tkinter as tk
from tkinter import ttk
import re


class EncontrarMaiorPonderado:
    def __init__(self, root):
        self.root = root
        self.root.title("Encontrar Maior Número Ponderado")

        self.label_lista = ttk.Label(root, text="Lista de Números:")
        self.label_lista.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.entry_lista = ttk.Entry(root, width=30)
        self.entry_lista.grid(column=1, row=0, padx=10, pady=5)

        self.label_resultado = ttk.Label(root, text="Maior Número:")
        self.label_resultado.grid(
            column=0, row=1, columnspan=2, padx=10, pady=5)

        self.botao_encontrar = ttk.Button(
            root, text="Encontrar Maior", command=self.encontrar_maior)
        self.botao_encontrar.grid(column=0, row=2, columnspan=2, pady=10)

    def encontrar_maior(self):
        entrada = self.entry_lista.get()

        # Remover caracteres não numéricos
        numeros_str = re.findall(r'\b\d+\b', entrada)

        # Converter para inteiros
        numeros = [int(num) for num in numeros_str]

        if numeros:
            # Pesos diferentes para cada número (exemplo: último número tem peso maior)
            maior_ponderado = max(numeros, key=lambda x: x * 2)
            self.label_resultado.config(
                text=f"Maior Número Ponderado: {maior_ponderado}")
        else:
            self.label_resultado.config(
                text="Insira uma lista válida de números.")


if __name__ == "__main__":
    root = tk.Tk()
    encontrar_maior_ponderado = EncontrarMaiorPonderado(root)
    root.mainloop()

