import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# CARREGAR OS 3 DATAFRAMES PARA CONHECIMENTO PRÉVIO

df19 = pd.read_csv('/content/Ano-2021.csv', delimiter=';')
df.head()

df20 = pd.read_csv('/content/Ano-2020.csv', delimiter=';')
df.head()

df21 = pd.read_csv('/content/Ano-2019.csv', delimiter=';')
df.head()

# CALCULANDO O VALOR TOTAL DE GASTO POR ESTADO

def valor_total_de_gasto_estado(df):
    return df[['sgUF','vlrDocumento']].groupby(['sgUF']).sum().sort_values(by=['vlrDocumento'])

# EXCLUINDO OS DADOS(REPRESENTANTES) REPETIDOS E AGRUPANDO POR ESTADO

def quantidade_representantes_por_estado(df):
    return df[['sgUF','txNomeParlamentar']].drop_duplicates(subset='txNomeParlamentar', keep='first').groupby(['sgUF']).count().sort_values(by=['txNomeParlamentar']).tail()

# PLOTANDO GRÁFICO PARA ILUSTRAÇÃO DA CORRELAÇÃO: QAUNTIDADE DE PARLAMENTAR X VALOR TOTAL DOS GASTOS

def gráfico_correlacao_parlamentar_gastoporestado(df):
    
return  x = df19i['txNomeParlamentar'].tolist()
        y = vlre19['vlrDocumento'].tolist()
        plt.scatter( x, y,color = 'b', marker = 'v')
        plt.axis('auto')
        plt.grid(True)
        plt.xlabel('Quantidade de parlamentares')
        plt.ylabel('Gasto por estado (em milhões)')
        plt.title('Gasto por estado x numero de parlamentares')
        plt.show()

# ATRAVÉS DO CALCULO DA CORRELAÇÃO DE PEASON, DESCOBRIMOS NO DATAFRAME DE 2019 O INDICE DE: 0,98
# LEGENDA CORRELAÇÃO DE PEARSON: QUANTO MAIS PRÓXIMO DE 1 ALTA CORRELAÇÃO POSITIVA E DIRETA, QUANTO MAIS 
# PRÓXIMO DE 0 SEM CORRELAÇAO E QUANTO MAIS PRÓXIMO DE -1 CORRELAÇÃO NEGATIVA E INDIRETA