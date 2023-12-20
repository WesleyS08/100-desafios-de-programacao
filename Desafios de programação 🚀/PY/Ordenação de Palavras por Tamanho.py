import tkinter as tk
from tkinter import ttk


class OrdenadorPorTamanho:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenador por Tamanho")

        self.label_entrada = ttk.Label(
            root, text="Insira as palavras (separadas por espaço):")
        self.label_entrada.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.entrada_palavras = ttk.Entry(root, width=40)
        self.entrada_palavras.grid(column=0, row=1, padx=10, pady=5)

        self.botao_ordenar = ttk.Button(
            root, text="Ordenar por Tamanho", command=self.ordenar_por_tamanho)
        self.botao_ordenar.grid(column=0, row=2, padx=10, pady=5)

        self.label_saida = ttk.Label(
            root, text="Palavras Ordenadas por Tamanho:")
        self.label_saida.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)

        self.saida_ordenada = ttk.Entry(root, width=40, state="readonly")
        self.saida_ordenada.grid(column=0, row=4, padx=10, pady=5)

    def ordenar_por_tamanho(self):
        palavras = self.entrada_palavras.get().split()
        palavras_ordenadas = sorted(palavras, key=len)
        resultado = ' '.join(palavras_ordenadas)
        self.saida_ordenada.config(state="normal")
        self.saida_ordenada.delete(0, tk.END)
        self.saida_ordenada.insert(0, resultado)
        self.saida_ordenada.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    ordenador_tamanho = OrdenadorPorTamanho(root)
    root.mainloop()
