def limpar_coluna_nome(df):
  df.nome = df.nome.str.strip()
  return df
