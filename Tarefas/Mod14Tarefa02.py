import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

#verifica se existe argumentos
if len(sys.argv) < 2:
    print("Insira um argumento após Mod14Tarefa02.py, ex: Mod14Tarefa02.py ARG1 ARG2 ...")
    sys.exit()

#armazena os argumentos
args = sys.argv[1:]


#Gera os gráficos
def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada',titulo=''):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5],title=titulo)
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).sort_values(value).plot(figsize=[15, 5],title=titulo)
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5],title=titulo)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None

#Cria o diretório, chama a função de gerar gráficos e salva no diretório
def mes_plot (data):
    max_data = data.DTNASC.max()[:7]
    os.makedirs('./output/figs/'+max_data, exist_ok=True)
    
    plota_pivot_table(data, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack',"IDADEMAE / ['DTNASC', 'SEXO']")
    plt.savefig('./output/figs/'+max_data+'/media idade mae por sexo.png')

    plota_pivot_table(data, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack',"PESO / ['DTNASC', 'SEXO']")
    plt.savefig('./output/figs/'+max_data+'/media peso bebe por sexo.png')

    plota_pivot_table(data, 'PESO', 'ESCMAE', 'median', 'apgar1 medio','gestacao','sort',"PESO / ESCMAE")
    plt.savefig('./output/figs/'+max_data+'/media apgar1 por escolaridade mae.png')

    plota_pivot_table(data, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort',"APGAR1 / GESTACAO")
    plt.savefig('./output/figs/'+max_data+'/media apgar1 por gestacao.png')

    plota_pivot_table(data, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio','gestacao','sort',"APGAR5 / GESTACAO")
    plt.savefig('./output/figs/'+max_data+'/media apgar5 por gestacao.png')

# Verifica se o arquivo existe e executa.
for x in args:
    try:
        with open('./input/SINASC_RO_2019_'+x+'.csv','r') as f:
            sinasc = pd.read_csv('./input/SINASC_RO_2019_'+x+'.csv')
            mes_plot(sinasc)
            print(f'Análise do arquivo SINASC_RO_2019_{x}.csv gerado com sucesso!')
    except IOError:
        print(f'Arquivo SINASC_RO_2019_{x}.csv NÃO encontrado!')
