import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def analisar_sentimento():
    texto = entry_texto.get()
    if not texto:
        messagebox.showwarning("Aviso", "Por favor, digite algum texto.")
        return

    sid = SentimentIntensityAnalyzer()
    pontuacao = sid.polarity_scores(texto)

    if pontuacao['compound'] >= 0.05:
        sentimento = 'Feliz'
    elif pontuacao['compound'] <= -0.05:
        sentimento = 'Triste'
    else:
        sentimento = 'Neutro'

    messagebox.showinfo("Resultado", f"Sentimento: {sentimento}")


# Criar janela
janela = tk.Tk()
janela.title("Análise de Sentimento")

# Criar rótulo para a entrada de texto
rotulo_texto = tk.Label(janela, text="Digite o texto:")
rotulo_texto.pack(pady=5)

# Criar entrada para o texto
entry_texto = tk.Entry(janela, width=50)
entry_texto.pack(pady=5)

# Criar botão para analisar o sentimento
botao_analisar = tk.Button(
    janela, text="Analisar Sentimento", command=analisar_sentimento)
botao_analisar.pack(pady=10)

# Rodar a janela
janela.mainloop()
