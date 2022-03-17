
import pandas as pd
import numpy as np

df_2019 = pd.read_csv('Ano-2019.csv', on_bad_lines='skip', sep = ';')
df_2020 = pd.read_csv('Ano-2020.csv', on_bad_lines='skip', sep = ';')
df_2021 = pd.read_csv('Ano-2021.csv', on_bad_lines='skip', sep = ';')

#PREPARAÇÃO DO DATAFRAME (DADOS DE 2019)

nomeParlamentar19 = df_2019[['txNomeParlamentar', 'vlrDocumento', 'vlrLiquido']] #novo DF com colunas que considerei relevantes para extrair os dados

vlrDocumento2019 = nomeParlamentar19.groupby('txNomeParlamentar') #agrupei todos os valores por parlamentar

for nome, dados in vlrDocumento2019:
  print(nome)

#GASTO MÉDIO POR PARLAMENTAR (DADOS DE 2019)

vlrDocumento2019[['vlrDocumento', 'vlrLiquido']].mean().round(2) #gasto médio especificado pelo vlrDocumento

for nome, dados in vlrDocumento2019:
  print('{} Gastou em média {}'.format(nome, dados.mean().round(2))) #gasto médio detalhadamente para facilitar a compreensão 

#PARLAMENTARES QUE MAIS E QUE MENOS CONSUMIRAM RECURSOS EM 2019

vlrDocumento2019.sum().idxmax() #idmax() puxa o índice com valor máximo dentro do datafframe

maisOneroso2019 = nomeParlamentar19.loc[nomeParlamentar19['txNomeParlamentar'] == 'Professora Marcivania']
maisOneroso2019.sum() #apliquei um loc[] para extrair os gastos da parlamentar e conferir se ralmente foi o que maiss consumiu recursos

vlrDocumento2019.sum().idxmin() #idmin() puxa o índice com valor mínimo dentro do dataframe

menosOneroso2019 = nomeParlamentar19.loc[nomeParlamentar19['txNomeParlamentar'] == 'FELIPE BORNIER']
menosOneroso2019.sum() #apliquei um loc[] para extrair os gastos do parlamentar e conferir se realmente foi o que menos consumiu recursos

#PREPARAÇÃO DO DATAFRAME (DADOS DE 2020)

nomeParlamentar20 = df_2020[['txNomeParlamentar', 'vlrDocumento', 'vlrLiquido']] #novo DF com colunas que considerei relevantes para extrair os dados

vlrDocumento2020 = nomeParlamentar20.groupby('txNomeParlamentar') #agrupei todos os valores por parlamentar

for nome, dados in vlrDocumento2020:
  print(nome)

#GASTO MÉDIO POR PARLAMENTAR (DADOS DE 2020)

vlrDocumento2020[['vlrDocumento', 'vlrLiquido']].mean().round(2) #gasto médio especificado pelo vlrDocumento

for nome, dados in vlrDocumento2020:
  print('{} Gastou em média {}'.format(nome, dados.mean().round(2))) #gasto médio detalhadamente para facilitar a compreensão 

#PARLAMENTARES QUE MAIS E QUE MENOS CONSUMIRAM RECURSOS EM 2020

vlrDocumento2020.sum().idxmax() #idmax() puxa o índice com valor máximo dentro do datafframe

maisOneroso2020 = nomeParlamentar20.loc[nomeParlamentar20['txNomeParlamentar'] == 'Jesus Sérgio']
maisOneroso2020.sum() #apliquei um loc[] para extrair os gastos da parlamentar e conferir se ralmente foi o que maiss consumiu recursos

vlrDocumento2020.sum().idxmin() #idmin() puxa o índice com valor mínimo dentro do dataframe

menosOneroso2020 = nomeParlamentar20.loc[nomeParlamentar20['txNomeParlamentar'] == 'Marcelo Álvaro Antônio']
menosOneroso2020.sum() #apliquei um loc[] para extrair os gastos do parlamentar e conferir se realmente foi o que menos consumiu recursos

#PREPARAÇÃO DO DATAFRAME (DADOS DE 2021)

nomeParlamentar21 = df_2021[['txNomeParlamentar', 'vlrDocumento', 'vlrLiquido']] #novo DF com colunas que considerei relevantes para extrair os dados

vlrDocumento2021 = nomeParlamentar21.groupby('txNomeParlamentar') #agrupei todos os valores por parlamentar

for nome, dados in vlrDocumento2021:
  print(nome)

#GASTO MÉDIO POR PARLAMENTAR (DADOS DE 2021)

vlrDocumento2021[['vlrDocumento', 'vlrLiquido']].mean().round(2) #gasto médio especificado pelo vlrDocumento

for nome, dados in vlrDocumento2021:
  print('{} Gastou em média {}'.format(nome, dados.mean().round(2))) #gasto médio detalhadamente para facilitar a compreensão 

#PARLAMENTARES QUE MAIS E QUE MENOS CONSUMIRAM RECURSOS EM 2021

vlrDocumento2021.sum().idxmax() #idmax() puxa o índice com valor máximo dentro do datafframe

maisOneroso2021 = nomeParlamentar21.loc[nomeParlamentar21['txNomeParlamentar'] == 'Jéssica Sales']
maisOneroso2021.sum() #apliquei um loc[] para extrair os gastos da parlamentar e conferir se ralmente foi o que maiss consumiu recursos

vlrDocumento2021.sum().idxmin() #idmin() puxa o índice com valor mínimo dentro do dataframe

menosOneroso2021 = nomeParlamentar21.loc[nomeParlamentar21['txNomeParlamentar'] == 'Fábio Faria']
menosOneroso2021.sum() #apliquei um loc[] para extrair os gastos do parlamentar e conferir se realmente foi o que menos consumiu recursos
