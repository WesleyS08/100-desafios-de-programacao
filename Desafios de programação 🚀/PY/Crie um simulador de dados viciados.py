import tkinter as tk
from tkinter import ttk
import random


class SimuladorDadosViciados:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Dados Viciados")

        self.label_lados = ttk.Label(root, text="Número de Lados do Dado:")
        self.label_lados.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.entry_lados = ttk.Entry(root, width=5)
        self.entry_lados.grid(column=1, row=0, padx=10, pady=5)

        self.label_resultado = ttk.Label(root, text="Resultado:")
        self.label_resultado.grid(
            column=0, row=1, columnspan=2, padx=10, pady=5)

        self.botao_sorteio = ttk.Button(
            root, text="Sortear Dado", command=self.sortear_dado)
        self.botao_sorteio.grid(column=0, row=2, columnspan=2, pady=10)

    def sortear_dado(self):
        try:
            num_lados = int(self.entry_lados.get())
            # Exemplo: dado viciado, 6 tem probabilidade maior
            resultado = random.choice([1, 2, 3, 4, 5, 6, 6])
            self.label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.label_resultado.config(
                text="Insira um número válido de lados do dado.")


if __name__ == "__main__":
    root = tk.Tk()
    simulador_dados = SimuladorDadosViciados(root)
    root.mainloop()
