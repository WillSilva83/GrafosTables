# Criação de Script em Python que irá ler um arquivo com o nome de todas as tabelas 
# com base no em uma lista de consultas identificar quais tabelas são utilizadas  
# verificar as mesmas tabelas em diversos arquivos json 
# verificar as mesmas tabelas em diverss arquivos yaml 

# TO-DOs 
# 1 - Ler o arquivo com o nome das tabelas
# 2 - Padronizar o nome das tabelas em minusculo

from ModelTable import ModelTable
import os
from gera_grafos import gera_grafos
import networkx as nx
from pyvis.network import Network


def ler_arquivo_tabelas(caminho_arquivo):
    """Lê um arquivo de texto e retorna uma lista de tabelas em minúsculo."""
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            tabelas = [linha.strip().lower() for linha in arquivo if linha.strip()]
        return tabelas
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return []

def lookup_on_files(tabela_nome: str, dir_files: str, type_file:str) -> dict:
    """Verifica se o nome da tabela está presente em um diretorio e subdiretorios e retorna uma dicionario com o nome do arquivo e a quantidade de vezes que a tabela foi encontrada."""

    count = 0
    resultado = {}

    try:
        for root, dirs, files in os.walk(dir_files):
            for arquivo in files:
                if arquivo.endswith(type_file):
                    caminho_completo = os.path.join(root, arquivo)

                    caminho_completo = os.path.join(root, arquivo)
                    
                    with open(caminho_completo, 'r') as arquivo:
                        conteudo = arquivo.read().lower()
                        count = conteudo.count(tabela_nome)
                        if count > 0:
                            resultado[caminho_completo] = count
    except FileNotFoundError:
        print(f"Diretório {dir_files} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler os arquivos: {e}")    

    return resultado

def salvar_model_table(model_table: ModelTable, caminho_arquivo: str, type_arquivo: str = 'csv'):
    """Salva a representação do ModelTable em um arquivo de csv ou parquet."""
    try:
        if type_arquivo == 'csv':
            with open(caminho_arquivo, 'a') as arquivo:
                arquivo.write(f"{model_table}\n")
        #elif type_arquivo == 'parquet':
            # import pandas as pd
            # df = pd.DataFrame([model_table.__dict__])
            # df.to_parquet(caminho_arquivo, index=False, compression='snappy', append=True)
        else:
            print("Tipo de arquivo não suportado. Use 'csv' ou 'parquet'.")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo: {e}")

def main():
    caminho_arquivo = 'nome_tabelas.csv'  # Substitua pelo caminho do seu arquivo
    tabelas = ler_arquivo_tabelas(caminho_arquivo)
    lista_model_tables = []

    for tabela in tabelas:
        dict_query = lookup_on_files(tabela, 'consultas/', '.csv')

        dict_json = lookup_on_files(tabela, 'json/', '.json')

        dict_yaml = lookup_on_files(tabela, 'yaml/', '.yaml')

        model_table = ModelTable(
            nome=tabela,
            is_used_on_query=bool(dict_query),
            dict_query=dict_query,
            is_used_on_json=bool(dict_json),
            dict_json=dict_json,
            is_used_on_yaml=bool(dict_yaml), 
            dict_yaml=dict_yaml
        )
        #print(model_table)

        lista_model_tables.append(model_table)

        salvar_model_table(model_table, 'model_tables.csv')

    grafos(lista_model_tables)


def grafos(lista_model_tables):
    grafo = gera_grafos(lista_model_tables)
        
    nt = Network(
        notebook=True, 
        height='600px', 
        width='100%', 
        directed=True, 
        select_menu=True,
        # Adicione ou altere o cdn_resources aqui:
        cdn_resources='in_line' 
    )

    # Carrega o grafo do NetworkX para o PyVis
    nt.from_nx(grafo)

    # Configurações adicionais para melhorar a visualização
    nt.toggle_physics(True)

    # Adiciona botões para interatividade
    nt.show_buttons(filter_=['physics', 'layout'])

    # Salva e exibe o grafo interativo em um arquivo HTML
    nt.show("grafo_dependencias_interativo.html")


if __name__ == "__main__":
    main()