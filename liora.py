def limpar_coluna_nome(df):
  df.nome = df.nome.str.strip()
  return df

def df_2019():
    types = {
        'cpf': 'category',
        'vlrLiquido': 'float'
    }
    return pd.read_csv(r'C:\Users\liora\Downloads\CEAP2019.csv', sep=';', dtype=types)

def df_2020():
    types = {
        'cpf': 'category',
        'vlrLiquido': 'float'
    }
    return pd.read_csv(r'C:\Users\liora\Downloads\CEAP2020.csv', sep=';', dtype=types)

def df_2021():
    types = {
        'cpf': 'category',
        'vlrLiquido': 'float'
    }
    return pd.read_csv(r'C:\Users\liora\Downloads\CEAP2021.csv', sep=';', dtype=types)
