import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
import requests

def buscar_cep():
    cep = entry_cep.get().replace("-", "").strip()
    
    if len(cep) == 8 and cep.isdigit():
        try:
            response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            data = response.json()
            
            if not data.get("erro"):
                # Preenche automaticamente os campos
                entry_logradouro.insert(0, data.get('logradouro', ''))
                entry_bairro.insert(0, data.get('bairro', ''))
                entry_cidade.insert(0, data.get('localidade', ''))
                entry_uf.insert(0, data.get('uf', ''))
            else:
                messagebox.showwarning("CEP", "CEP não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha na consulta: {str(e)}")
    else:
        messagebox.showwarning("CEP", "CEP deve ter 8 dígitos!")

def salvar_ocorrencia():
    # Coletar dados
    ocorrencia = {
        "Data/Hora": [datetime.now().strftime("%d/%m/%Y %H:%M")],
        "Situação": [combo_situacao.get()],
        "CEP": [entry_cep.get()],
        "Logradouro": [entry_logradouro.get()],
        "Número": [entry_numero.get()],
        "Bairro": [entry_bairro.get()],
        "Cidade": [entry_cidade.get()],
        "UF": [entry_uf.get()],
        "Contato": [entry_contato.get()],
        "Complemento": [entry_complemento.get()],
        "Status": ["Pendente"]
    }
    
    # Validação
    if not all([ocorrencia["Situação"][0], ocorrencia["CEP"][0], ocorrencia["Número"][0]]):
        messagebox.showerror("Erro", "Preencha os campos obrigatórios!")
        return
    
    # Salvar
    try:
        df = pd.DataFrame(ocorrencia)
        try:
            df_existente = pd.read_excel("ocorrencias_bombeiros.xlsx")
            df_final = pd.concat([df_existente, df], ignore_index=True)
        except FileNotFoundError:
            df_final = df
        
        df_final.to_excel("ocorrencias_bombeiros.xlsx", index=False)
        messagebox.showinfo("Sucesso", "Ocorrência registrada!")
        limpar_campos()
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao salvar: {e}")

def limpar_campos():
    for entry in [entry_cep, entry_logradouro, entry_numero, 
                 entry_bairro, entry_cidade, entry_uf, 
                 entry_contato, entry_complemento]:
        entry.delete(0, tk.END)

# Interface
root = tk.Tk()
root.title("Sistema de Ocorrências - Bombeiros")
root.geometry("600x450")

# Layout
frame_cep = tk.Frame(root)
frame_cep.grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(frame_cep, text="CEP*:").pack(side=tk.LEFT)
entry_cep = tk.Entry(frame_cep, width=15)
entry_cep.pack(side=tk.LEFT, padx=5)
btn_cep = tk.Button(frame_cep, text="Buscar CEP", command=buscar_cep)
btn_cep.pack(side=tk.LEFT)

campos = [
    ("Situação*:", combo_situacao := ttk.Combobox(root, values=[
        "Incêndio Residencial", "Acidente de Trânsito", 
        "Resgate em Altura", "Afogamento", "Outros"
    ]), 1),
    ("Logradouro:", entry_logradouro := tk.Entry(root), 2),
    ("Número*:", entry_numero := tk.Entry(root), 3),
    ("Bairro:", entry_bairro := tk.Entry(root), 4),
    ("Cidade:", entry_cidade := tk.Entry(root), 5),
    ("UF:", entry_uf := tk.Entry(root, width=5), 6),
    ("Contato:", entry_contato := tk.Entry(root), 7),
    ("Complemento:", entry_complemento := tk.Entry(root), 8)
]

for idx, (label, widget, row) in enumerate(campos):
    tk.Label(root, text=label).grid(row=row, column=0, padx=10, pady=5, sticky="e")
    widget.grid(row=row, column=1, padx=10, pady=5, sticky="ew")

# Botões
btn_salvar = tk.Button(root, text="Registrar Ocorrência", command=salvar_ocorrencia, bg="#1B8800", fg="white")
btn_salvar.grid(row=9, column=1, pady=15, sticky="ew")

btn_limpar = tk.Button(root, text="Limpar Campos", command=limpar_campos)
btn_limpar.grid(row=9, column=0, pady=15, sticky="ew")

root.mainloop()