import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import cmath


def resolver_equacao():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        delta = cmath.sqrt(b**2 - 4*a*c)

        x1 = (-b + delta) / (2*a)
        x2 = (-b - delta) / (2*a)

        resultado_label.config(
            text=f"Soluções da equação:\nX1 = {x1}\nX2 = {x2}")

    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, insira valores numéricos para os coeficientes.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


# Criar a janela principal
root = tk.Tk()
root.title("Resolva uma Equação de Segundo Grau")

# Criar widgets
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_a = ttk.Label(frame, text="Coeficiente a:")
label_a.grid(column=0, row=0, padx=5, pady=5, sticky=tk.E)

entry_a = ttk.Entry(frame)
entry_a.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))

label_b = ttk.Label(frame, text="Coeficiente b:")
label_b.grid(column=0, row=1, padx=5, pady=5, sticky=tk.E)

entry_b = ttk.Entry(frame)
entry_b.grid(column=1, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))

label_c = ttk.Label(frame, text="Coeficiente c:")
label_c.grid(column=0, row=2, padx=5, pady=5, sticky=tk.E)

entry_c = ttk.Entry(frame)
entry_c.grid(column=1, row=2, padx=5, pady=5, sticky=(tk.W, tk.E))

botao_resolver = ttk.Button(frame, text="Resolver", command=resolver_equacao)
botao_resolver.grid(column=0, row=3, columnspan=2, pady=10)

resultado_label = ttk.Label(frame, text="")
resultado_label.grid(column=0, row=4, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
