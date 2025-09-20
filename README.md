# GrafosTables

Este projeto tem como objetivo analisar a utilização de tabelas em diferentes arquivos de consultas, JSON e YAML, gerando um grafo interativo das dependências entre as tabelas.

## Funcionalidades
- Lê um arquivo com o nome das tabelas (`nome_tabelas.csv`).
- Procura o uso dessas tabelas em arquivos de consultas (`consultas/*.csv`), arquivos JSON (`json/**/*.json`) e arquivos YAML (`yaml/**/*.yaml`).
- Gera um relatório (`model_tables.csv`) indicando em quais arquivos cada tabela é utilizada.
- Cria um grafo interativo das dependências das tabelas, salvo em `grafo_dependencias_interativo.html`.

## Estrutura do Projeto
- `main.py`: Script principal que executa todo o fluxo.
- `ModelTable.py`: Classe que representa o modelo de uma tabela e seus usos.
- `gera_grafos.py`: Função para gerar o grafo de dependências.
- `nome_tabelas.csv`: Lista de nomes das tabelas a serem analisadas (um nome por linha).
- `consultas/`: Diretório com arquivos de consulta (CSV).
- `json/`: Diretório com arquivos JSON (pode conter subdiretórios).
- `yaml/`: Diretório com arquivos YAML (pode conter subdiretórios).
- `model_tables.csv`: Arquivo gerado com o resultado da análise.
- `grafo_dependencias_interativo.html`: Grafo interativo gerado.

## Como executar
1. Certifique-se de que os arquivos e diretórios necessários estão presentes conforme a estrutura acima.
2. Instale as dependências necessárias:
   ```bash
   pip install networkx pyvis
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. O resultado será salvo em `model_tables.csv` e o grafo interativo em `grafo_dependencias_interativo.html`.

## Observações
- O script procura os nomes das tabelas em minúsculo nos arquivos.
- O grafo é gerado utilizando as bibliotecas NetworkX e PyVis.
- O arquivo `model_tables.csv` é sobrescrito a cada execução.


