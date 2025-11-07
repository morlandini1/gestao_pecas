# Desafio de Automação Digital: Gestão de Peças (UniFECAF)

[cite_start]Este projeto é um protótipo em Python desenvolvido para a disciplina de Algoritmos e Lógica de Programação, focado em resolver um desafio de automação industrial[cite: 5].

[cite_start]O sistema simula o controle de qualidade e armazenamento de peças em uma linha de montagem [cite: 7][cite_start], automatizando a inspeção manual que anteriormente gerava atrasos e falhas.

## Funcionalidades

[cite_start]O script `gestao_pecas.py` apresenta um menu interativo  com as seguintes opções:

1.  [cite_start]**Cadastrar nova peça** [cite: 47][cite_start]: Recebe os dados da peça (peso, cor, comprimento) [cite: 10] e a avalia.
2.  [cite_start]**Listar peças aprovadas/reprovadas**[cite: 48]: Exibe um resumo de todas as peças processadas.
3.  [cite_start]**Remover peça cadastrada**: Permite ao usuário remover uma peça (aprovada ou reprovada) do sistema pelo seu ID.
4.  [cite_start]**Listar caixas fechadas** [cite: 50][cite_start]: Mostra as caixas que atingiram a capacidade máxima de 10 peças.
5.  [cite_start]**Gerar relatório final** [cite: 51][cite_start]: Apresenta um dashboard consolidado com o total de peças aprovadas [cite: 19][cite_start], reprovadas (com motivos)  [cite_start]e o número de caixas utilizadas[cite: 21].

## [cite_start]Como Rodar o Programa [cite: 54]

1.  **Pré-requisitos**:
    * Ter o Python 3 instalado em sua máquina.

2.  **Clone o Repositório**:
    ```bash
    git clone [SEU_LINK_DO_GITHUB_AQUI]
    cd [NOME_DO_SEU_REPOSITORIO]
    ```

3.  **Execute o Programa**:
    Abra seu terminal ou VSCode e execute o seguinte comando:

    ```bash
    python gestao_pecas.py
    ```
    Ou (dependendo da instalação do Python):
    ```bash
    python3 gestao_pecas.py
    ```
4.  **Navegue pelo Menu**:
    O menu interativo aparecerá no terminal. Digite o número da opção desejada e pressione Enter.

## [cite_start]Exemplos de Entradas e Saídas [cite: 54]

### Exemplo 1: Cadastrando uma Peça APROVADA
