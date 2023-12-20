import tkinter as tk
from tkinter import ttk


def cifra_cesar(texto, chave):
    resultado = ""
    for caractere in texto:
        if caractere.isalpha():
            maiuscula = caractere.isupper()
            caractere = caractere.lower()
            indice = ord(caractere) - ord('a')
            indice_cifrado = (indice + chave) % 26
            novo_caractere = chr(indice_cifrado + ord('a'))
            resultado += novo_caractere.upper() if maiuscula else novo_caractere
        else:
            resultado += caractere
    return resultado


def cifrar():
    texto_original = entry_texto.get()

    # Tratamento de erro para garantir que a chave seja um número inteiro
    try:
        chave = int(entry_chave.get())
    except ValueError:
        resultado_label.config(
            text="Por favor, insira um valor numérico para a chave.")
        return

    texto_cifrado = cifra_cesar(texto_original, chave)
    resultado_label.config(text=f"Texto cifrado: {texto_cifrado}")


# Criar a janela principal
root = tk.Tk()
root.title("Cifra de César - Interface Gráfica")

# Criar widgets
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_texto = ttk.Label(frame, text="Texto:")
label_texto.grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)

entry_texto = ttk.Entry(frame)
entry_texto.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))

label_chave = ttk.Label(frame, text="Chave:")
label_chave.grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)

entry_chave = ttk.Entry(frame)
entry_chave.grid(column=1, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

botao_cifrar = ttk.Button(frame, text="Cifrar", command=cifrar)
botao_cifrar.grid(column=0, row=2, columnspan=2, pady=10)

resultado_label = ttk.Label(frame, text="")
resultado_label.grid(column=0, row=3, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
