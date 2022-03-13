# Projeto Final Módulo 05 - Análise da Cota Parlamentar dos Deputados Federais


Esse projeto consiste em fazer uma Análise Exploratória dos Gastos da **Cota para Exercício da Atividade Parlamentar (CEAP)** Dos Deputados Federais.

Os arquivos que serão baixados e analisados se encontram [neste link.](https://drive.google.com/drive/u/0/folders/1H_uQc8UTzA1is3jjZjmrFRIabiOUHoIi)

Os links [Limpeza](/Limpeza.md) e [Análise](/Análise.ipynb) servirão para acompanhar algumas etapas do Processo de Análise.

Nessa Análise utilizamos a Linguagem Python com as Bibliotecas:

- Numpy
- Pandas
- Matplotlib
- Seaborn
- PyWaffle


# Execução

## Clonar Repositório

Copie o código abaixo e baixe o repositório. Assegure que o git está instalado no seu computador.

### Git - HTTPS

``` shell
git clone https://github.com/derekmartins/AnaliseCotaParlamentarDeputadosFederais
```

### Git - SSH

```
git clone git@github.com:derekmartins/AnaliseCotaParlamentarDeputadosFederais.git
```

## Criar Ambiente Virtual

Para criar um Ambiente Virtual, utilizamos os segunto comando.
``` python
python -m venv env
```

## Ativar o Ambiente Virtual

Depois disso você deve ativar o Ambiente utilizando os comandos:

### Linux

``` shell
source env/bin/activate
```

### Windows CMD
``` cmd
env\Scripts\activate.bat
```

### Windows PowerShell
``` PowerShell
env\Scripts\activate.ps1
```

Logo após, você pode instalar as dependências.

## Instalação das Dependências no Ambiente Virtual.

``` python
pip install requirements.txt
```

> Obs: Lembrando que toda vez que reabrir a sua IDE, você precisa reativar o seu Ambiente Virtual.