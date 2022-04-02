import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# CALCULANDO O VALOR TOTAL DE GASTO POR ESTADO

def valor_total_de_gasto_estado(df):
    return df[['sgUF','vlrDocumento']].groupby(['sgUF']).sum().sort_values(by=['vlrDocumento'])

# EXCLUINDO OS DADOS(REPRESENTANTES) REPETIDOS E AGRUPANDO POR ESTADO

def quantidade_representantes_por_estado(df):
    return df[['sgUF','txNomeParlamentar']].drop_duplicates(subset='txNomeParlamentar', keep='first').groupby(['sgUF']).count().sort_values(by=['txNomeParlamentar']).tail()

# PLOTANDO GRÁFICO PARA ILUSTRAÇÃO DA CORRELAÇÃO: QAUNTIDADE DE PARLAMENTAR X VALOR TOTAL DOS GASTOS


# ATRAVÉS DO CALCULO DA CORRELAÇÃO DE PEASON, DESCOBRIMOS NO DATAFRAME DE 2019 O INDICE DE: 0,98
# LEGENDA CORRELAÇÃO DE PEARSON: QUANTO MAIS PRÓXIMO DE 1 ALTA CORRELAÇÃO POSITIVA E DIRETA, QUANTO MAIS 
# PRÓXIMO DE 0 SEM CORRELAÇAO E QUANTO MAIS PRÓXIMO DE -1 CORRELAÇÃO NEGATIVA E INDIRETA