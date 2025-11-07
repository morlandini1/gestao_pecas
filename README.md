# Desafio de Automação Digital: Gestão de Peças (UniFECAF)

Este projeto é um protótipo em Python desenvolvido para a disciplina de Algoritmos e Lógica de Programação, focado em resolver um desafio de automação industrial.

O sistema simula o controle de qualidade e armazenamento de peças em uma linha de montagem, automatizando a inspeção manual que anteriormente gerava atrasos e falhas.

## Funcionalidades

O script `gestao_pecas.py` apresenta um menu interativo  com as seguintes opções:

1 **Cadastrar nova peça** : Recebe os dados da peça (peso, cor, comprimento) e a avalia.
2 **Listar peças aprovadas/reprovadas**: Exibe um resumo de todas as peças processadas.
3 **Remover peça cadastrada**: Permite ao usuário remover uma peça (aprovada ou reprovada) do sistema pelo seu ID.
4 **Listar caixas fechadas** : Mostra as caixas que atingiram a capacidade máxima de 10 peças.
5 **Gerar relatório final** : Apresenta um dashboard consolidado com o total de peças aprovadas, reprovadas (com motivos)e o número de caixas utilizadas.
0 **Sair do sistema** : Sai do sistema.

## Como Rodar o Programa

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

## Exemplos de Entradas e Saídas

### Exemplo 1: Cadastrando uma Peça APROVADA

--- Sistema de Gestão Industrial (v1.0) ---
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
Escolha uma opção: 1

--- 1. Cadastrar Nova Peça ---
Digite o peso (g): 95
Digite a cor (azul/verde/outra): azul
Digite o comprimento (cm): 17

[SUCESSO] Peça ID 1 APROVADA.
Peça ID 1 adicionada à Caixa 1 (Peças na caixa: 1/10)

### Exemplo 2: Cadastrando uma Peça REPROVADA

Escolha uma opção: 1

--- 1. Cadastrar Nova Peça --- Digite o peso (g): 90 Digite a cor (azul/verde/outra): vermelho Digite o comprimento (cm): 15

[FALHA] Peça ID 2 REPROVADA. Motivos: Peso fora do padrão, Cor inválida

### Exemplo 3: Gerando Relatório

Escolha uma opção: 5

--- 5. Gerar Relatório Final --- Total de Peças Processadas: 2 Total de Peças APROVADAS: 1 Total de Peças REPROVADAS: 1

Motivos de Reprovação:

Por Peso: 1 peças

Por Cor: 1 peças

Por Comprimento: 0 peças

Gerenciamento de Caixas:

Total de caixas utilizadas: 1

Peças na caixa atual (Caixa 1): 1/10
