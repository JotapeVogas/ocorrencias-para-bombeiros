# ocorrencias-fire
Sistema de registro de ocorrências para bombeiros em Python com Tkinter. Consulta CEP via API, preenche automaticamente endereço e salva em Excel. Campos obrigatórios: situação e número. Interface intuitiva com validação de dados.

# Sistema de Ocorrências - Bombeiros  

Aplicação em Python para registro de ocorrências, integrando consulta de CEP via API e armazenamento em planilha Excel.  

## Funcionalidades  
- Consulta automática de endereço por CEP (ViaCEP)  
- Validação de campos obrigatórios (*Situação* e *Número*)  
- Salva dados em arquivo Excel (`ocorrencias_bombeiros.xlsx`)  
- Interface simples com Tkinter  

## Requisitos  
- Python 3.x  
- Bibliotecas: `pandas`, `requests`, `tkinter`  

## Como Usar  
1. Preencha os campos (*Situação* e *Número* são obrigatórios).  
2. Clique em **Buscar CEP** para autocompletar o endereço.  
3. Salve com **Registrar Ocorrência**.  

## Observações  
- Dados são armazenados na mesma pasta do script.  
- CEP não é obrigatório, mas deve ter 8 dígitos se informado.  
