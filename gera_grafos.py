# Gera o grafos com base no ModelTable

import networkx as nx

# 1. Inicializa um Grafo Direcionado (DiGraph)
# A direção é Tabela -> Arquivo (a tabela LÊ o arquivo)
G = nx.DiGraph() 

def gera_grafos(lista_model_tables):
    """Gera um grafo direcionado a partir de uma lista de objetos ModelTable."""
    # 1. Inicializa um Grafo Direcionado (DiGraph)
    # A direção é Tabela -> Arquivo (a tabela LÊ o arquivo)
    # Adicionar label nos nós para diferenciar tabelas e arquivos

    G = nx.DiGraph()
    for model_table in lista_model_tables:
        tabela = model_table.nome
        # Adiciona o nó da tabela com label 'Tabela'
        G.add_node(tabela, type='table', label=tabela)
        
        # Adiciona os nós e arestas para arquivos de consulta
        if model_table.is_used_on_query:
            for arquivo, count in model_table.dict_query.items():
                G.add_node(arquivo, type='file', label=arquivo)
                G.add_edge(tabela, arquivo, weight=count)
        
        # Adiciona os nós e arestas para arquivos JSON
        if model_table.is_used_on_json:
            for arquivo, count in model_table.dict_json.items():
                G.add_node(arquivo, type='file', label=arquivo)
                G.add_edge(tabela, arquivo, weight=count)
        
        # Adiciona os nós e arestas para arquivos YAML
        if model_table.is_used_on_yaml:
            for arquivo, count in model_table.dict_yaml.items():
                G.add_node(arquivo, type='file', label=arquivo)
                G.add_edge(tabela, arquivo, weight=count)
    return G