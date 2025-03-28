import string
import numpy 
import tkinter as tk
from tkinter import messagebox
from funcoes import *

def gerar_senha():
    try:
        tamanho_senha = int(entry_tamanho.get())
        
        if tamanho_senha < 8 or tamanho_senha > 32:
            raise ValueError("A senha deve ter entre 8 e 32 caracteres.")
        
        senha_numero = var_numero.get()
        senha_letra = var_letra.get()
        senha_letra_maiuscula = var_letra_maiuscula.get()
        senha_caracter_especial = var_caracter_especial.get()

        opcoes_conjuntos = {
            'numeros': string.digits,
            'letras_minusculas': string.ascii_lowercase,
            'letras_maiusculas': string.ascii_uppercase,
            'especial': string.punctuation
        }

        conjuntos_escolhidos = []

        if senha_numero:
            conjuntos_escolhidos.append(opcoes_conjuntos['numeros'])
        if senha_letra:
            conjuntos_escolhidos.append(opcoes_conjuntos['letras_minusculas'])
        if senha_letra_maiuscula:
            conjuntos_escolhidos.append(opcoes_conjuntos['letras_maiusculas'])
        if senha_caracter_especial:
            conjuntos_escolhidos.append(opcoes_conjuntos['especial'])

        if conjuntos_escolhidos:
            conjunto_total = ''.join(conjuntos_escolhidos)
            senha = numpy.random.choice(list(conjunto_total), tamanho_senha)
            senha_gerada = ''.join(senha)
            label_senha.config(text=f"Senha gerada: {senha_gerada}")
        else:
            messagebox.showerror("Erro", "Por favor, selecione ao menos um tipo de caractere para a senha.")
    
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

root = tk.Tk()
root.title("Gerador de Senha")

var_numero = tk.BooleanVar()
var_letra = tk.BooleanVar()
var_letra_maiuscula = tk.BooleanVar()
var_caracter_especial = tk.BooleanVar()

label_tamanho = tk.Label(root, text="Quantos caracteres a senha deve ter? (8-32)")
label_tamanho.pack(pady=5)

entry_tamanho = tk.Entry(root)
entry_tamanho.pack(pady=5)

checkbox_numero = tk.Checkbutton(root, text="Incluir números", variable=var_numero)
checkbox_numero.pack(pady=5)

checkbox_letra = tk.Checkbutton(root, text="Incluir letras minúsculas", variable=var_letra)
checkbox_letra.pack(pady=5)

checkbox_letra_maiuscula = tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=var_letra_maiuscula)
checkbox_letra_maiuscula.pack(pady=5)

checkbox_caracter_especial = tk.Checkbutton(root, text="Incluir caracteres especiais", variable=var_caracter_especial)
checkbox_caracter_especial.pack(pady=5)

botao_gerar = tk.Button(root, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack(pady=20)

label_senha = tk.Label(root, text="Senha gerada: ")
label_senha.pack(pady=5)

root.mainloop()
