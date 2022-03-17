import pandas as pd
import numpy as np

def limpar_coluna_nome(df):
  df.nome = df.nome.str.strip()
  return df

def carregar_df_2019():
    types = {
        'cpf': 'category',
        'vlrLiquido': 'float'
    }
    return pd.read_csv(r'C:\Users\liora\Downloads\CEAP2019.csv', sep=';', dtype=types)

def carregar_df_2020():
    types = {
        'cpf': 'category',
        'vlrLiquido': 'float'
    }
    return pd.read_csv(r'C:\Users\liora\Downloads\CEAP2020.csv', sep=';', dtype=types)

def carregar_df_2021():
    types = {
        'cpf': 'category',
        'vlrLiquido': 'float'
    }
    return pd.read_csv(r'C:\Users\liora\Downloads\CEAP2021.csv', sep=';', dtype=types)

def dados_nulos(df):
    return (df.isnull().sum() / df.shape[0]).sort_values(ascending=False)



