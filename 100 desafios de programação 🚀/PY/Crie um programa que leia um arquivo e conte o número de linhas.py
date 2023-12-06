import tkinter as tk
from tkinter import filedialog


def contar_linhas(arquivo_path):
    try:
        with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
            numero_linhas = sum(1 for linha in arquivo)
        return numero_linhas
    except UnicodeDecodeError:
        with open(arquivo_path, 'r', encoding='latin-1') as arquivo:
            numero_linhas = sum(1 for linha in arquivo)
        return numero_linhas
    except FileNotFoundError:
        return f"Arquivo '{arquivo_path}' não encontrado."
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}"


def exibir_resultado():
    caminho_arquivo = filedialog.askopenfilename(
        filetypes=[("Todos os arquivos", "*.*")])
    if caminho_arquivo:
        numero_linhas = contar_linhas(caminho_arquivo)
        resultado_var.set(f"Número de linhas no arquivo: {numero_linhas}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contador de Linhas")

    frame = tk.Frame(root, padx=10, pady=10)
    frame.pack()

    botao_abrir = tk.Button(frame, text="Abrir Arquivo",
                            command=exibir_resultado)
    botao_abrir.pack(pady=10)

    resultado_var = tk.StringVar()
    resultado_var.set("Número de linhas no arquivo: 0")  # Valor inicial
    resultado_label = tk.Label(frame, textvariable=resultado_var)
    resultado_label.pack()

    root.mainloop()
