import tkinter as tk
from tkinter import messagebox


def calcula_digitos_verificadores(cpf_parcial):
    # Calcula o primeiro dígito verificador
    soma = 0
    peso = 10
    for digito in cpf_parcial:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    digito_verificador_1 = 0 if resto < 2 else 11 - resto

    # Adiciona o primeiro dígito verificador ao CPF parcial
    cpf_com_digito_1 = cpf_parcial + str(digito_verificador_1)

    # Calcula o segundo dígito verificador
    soma = 0
    peso = 11
    for digito in cpf_com_digito_1:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    digito_verificador_2 = 0 if resto < 2 else 11 - resto

    # Adiciona o segundo dígito verificador ao CPF completo
    cpf_completo = cpf_com_digito_1 + str(digito_verificador_2)

    return cpf_completo


def valida_cpf(cpf):
    # Remove pontos e traços do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    # Calcula os dígitos verificadores e compara com os dígitos fornecidos
    cpf_calculado = calcula_digitos_verificadores(cpf[:-2])
    return cpf_calculado == cpf

def verificar_cpf():
    cpf_digitado = entry_cpf.get()
    
    if valida_cpf(cpf_digitado):
        messagebox.showinfo("CPF Válido", "O CPF é válido.")
    else:
        messagebox.showerror("CPF Inválido", "O CPF é inválido.")


# Criando a janela principal
janela = tk.Tk()
janela.title("Validador de CPF")

# Criando e posicionando os widgets na janela
label_instrucao = tk.Label(janela, text="Digite o CPF (apenas números):")
label_instrucao.pack(pady=10)

entry_cpf = tk.Entry(janela)
entry_cpf.pack(pady=10)

botao_verificar = tk.Button(janela, text="Verificar CPF", command=verificar_cpf)
botao_verificar.pack(pady=20)

# Iniciando o loop principal da interface gráfica
janela.mainloop()
