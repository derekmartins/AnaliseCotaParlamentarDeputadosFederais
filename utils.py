import pandas as pd
from datetime import datetime
import numpy as np


def carregar_dados():
    df_2019 = pd.read_csv('Ano-2019.csv', sep=';')
    df_2020 = pd.read_csv('Ano-2020.csv', sep=';')
    df_2021 = pd.read_csv('Ano-2021.csv', sep=';')


NUM_MES_NOME_MES = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}


def carregar_dados(ano: int = 2021):
    filename = f'Ano-{ano}.csv'
    dataframe = pd.read_csv(filename, delimiter=';', dtype='str')
    return dataframe


def carregar_dados_todos_anos():
    types = {
        'cpf': 'category',
        'vlrLiquido': 'float'
    }
    return pd.read_csv("CEAP(2019-2020-2021).csv", sep=';', dtype=types)


def media_gastos(dataframe, colunas_agregadas=['vlrDocumento', 'vlrLiquido']):
    group_by_keys = dataframe.columns.difference(colunas_agregadas).to_list()
    group = dataframe.groupby(group_by_keys).mean()
    return group.reset_index()


def soma_gastos(dataframe, colunas_agregadas=['vlrDocumento', 'vlrLiquido']):
    group_by_keys = dataframe.columns.difference(colunas_agregadas).to_list()
    group = dataframe.groupby(group_by_keys).sum()
    return group.reset_index()


def _formatar_data_para_rotulo(data: str):
    data_dt = datetime.strptime(data, '%m/%Y')
    return f'{NUM_MES_NOME_MES[data_dt.month]} de {data_dt.year}'


def formatar_datas_para_rotulo(data: pd.Series):
    return data.apply(_formatar_data_para_rotulo)


def gerar_limites_eixo_y(lista):
    minimo = min(lista)
    maximo = max(lista)
    expoente = True

    if (-1 < minimo < 1) and (-1 < maximo < 1):
        expoente = False

    if maximo < 0:
        return _gerar_limite_apropriado(minimo, expoente_positivo=expoente), 0

    if minimo > 0:
        return 0, _gerar_limite_apropriado(maximo, expoente_positivo=expoente)

    return (_gerar_limite_apropriado(minimo, expoente_positivo=expoente),
            _gerar_limite_apropriado(maximo, expoente_positivo=expoente))


def _verificar_marcacao_expoente_positivo(
    valor,
    marcacao,
    expoente
):
    return (valor / marcacao) < 1


def _verificar_marcacao_expoente_negativo(
        valor,
        marcacao,
        expoente
):
    valor_analisado = valor / (10 ** expoente)
    return valor_analisado > 1 and valor < marcacao


def _gerar_limite_apropriado(
    valor,
    pontos_marcacao=[x/2 for x in range(1, 20, 1)],
    expoente_positivo=True
):

    sinal = np.sign(valor)
    valor = np.abs(valor)
    expoente = 0

    verificar = (_verificar_marcacao_expoente_positivo
                 if expoente_positivo
                 else _verificar_marcacao_expoente_negativo)

    while True:
        for ponto_marcacao in pontos_marcacao:
            marcacao = ponto_marcacao * (10 ** expoente)

            if verificar(valor, marcacao, expoente):
                return round(marcacao * sinal, np.abs(expoente) + 1)

        expoente += 1 if expoente_positivo else -1


def configurar_yticks(df, ax, num_amostras, formato, base):
    min_y, max_y = gerar_limites_eixo_y(df)
    yticks = np.linspace(min_y, max_y, num_amostras)
    ax.set_ylim([min_y, max_y])
    ax.set_yticks(yticks)
    yticks = [formato.format(x/base) for x in yticks]
    ax.set_yticklabels(yticks)

def buscar_por_cnpj(df, cnpj):
    filtro = df.txtCNPJCPF == cnpj
    return df[filtro]

def paginacao(lista, pagina, num_amostras=50):  
    return lista[(pagina-1)*num_amostras:pagina*num_amostras]