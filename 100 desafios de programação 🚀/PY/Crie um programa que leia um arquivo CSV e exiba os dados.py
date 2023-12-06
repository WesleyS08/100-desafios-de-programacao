import tkinter as tk
from tkinter import filedialog
import csv


class VisualizadorCSV:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de CSV")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.botao_abrir = tk.Button(
            self.frame, text="Abrir CSV", command=self.abrir_csv)
        self.botao_abrir.pack(pady=10)

        self.texto_dados = tk.Text(self.frame, height=20, width=50)
        self.texto_dados.pack()

    def abrir_csv(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos CSV", "*.csv")])

        if file_path:
            with open(file_path, newline="", encoding="utf-8") as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)
                dados = "\n".join([",".join(row) for row in leitor_csv])
                # Limpar o texto existente
                self.texto_dados.delete(1.0, tk.END)
                self.texto_dados.insert(tk.END, dados)


if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizadorCSV(root)
    root.mainloop()
