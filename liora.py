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


def metodo_describe(df):
    return df.describre()


def verificar_dados_nulos(df):
    return (df.isnull().sum() / df.shape[0]).sort_values(ascending=False)


def categoria_despesa_onerosa(df):
    return df.groupby(['txtDescricao'])[ 'vlrLiquido'].sum().sort_values(ascending=False).head(3)


def trecho_viagem_recorrente(df):
    return df['txtTrecho'].value_counts().head(3)


def extra_parlamentar_restituição(df):
    return df.groupby(['txtDescricao', 'txNomeParlamentar'])['vlrRestituicao'].sum().sort_values(ascending=False).head(10)


#atribuir cada soma a uma variável e somar os três anos para chegar no valor final.
def extra_montante_ativ_parlam(df):
    return df[df['txtDescricao'] == 'DIVULGAÇÃO DA ATIVIDADE PARLAMENTAR.']['vlrLiquido'].sum()


