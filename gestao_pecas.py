# --- Variáveis Globais (Nosso "Banco de Dados" simples) ---
pecas_aprovadas = []
pecas_reprovadas = []
caixas = [[]]  # Começamos com a primeira caixa aberta. Lista de listas.
contador_id_peca = 1
# Dicionário para contar os motivos de reprovação 
contagem_reprovacao = {
    'peso': 0,
    'cor': 0,
    'comprimento': 0
}

# --- Funções do Sistema ---

def cadastrar_nova_peca():
    """
    Função para cadastrar uma nova peça e validar seus critérios.
    """
    global contador_id_peca
    
    print("\n--- 1. Cadastrar Nova Peça ---")
    try:
        # Recebe os dados da peça [cite: 10]
        peso = float(input("Digite o peso (g): "))
        cor = input("Digite a cor (azul/verde/outra): ").lower()
        comprimento = float(input("Digite o comprimento (cm): "))
        
        peca = {
            'id': contador_id_peca,
            'peso': peso,
            'cor': cor,
            'comprimento': comprimento
        }
        
        # Avalia os critérios de qualidade 
        motivos_reprovacao = []
        
        # Critério 1: Peso 
        if not (95 <= peso <= 105):
            motivos_reprovacao.append("Peso fora do padrão")
            contagem_reprovacao['peso'] += 1
            
        # Critério 2: Cor [cite: 14]
        if cor not in ['azul', 'verde']:
            motivos_reprovacao.append("Cor inválida")
            contagem_reprovacao['cor'] += 1
            
        # Critério 3: Comprimento [cite: 15]
        if not (10 <= comprimento <= 20):
            motivos_reprovacao.append("Comprimento fora do padrão")
            contagem_reprovacao['comprimento'] += 1
            
        # Tomada de Decisão
        if not motivos_reprovacao:
            # PEÇA APROVADA
            pecas_aprovadas.append(peca)
            print(f"\n[SUCESSO] Peça ID {peca['id']} APROVADA.")
            armazenar_em_caixa(peca)
        else:
            # PEÇA REPROVADA
            pecas_reprovadas.append({'peca': peca, 'motivos': motivos_reprovacao})
            print(f"\n[FALHA] Peça ID {peca['id']} REPROVADA. Motivos: {', '.join(motivos_reprovacao)}")
            
        # Incrementa o ID para a próxima peça
        contador_id_peca += 1
        
    except ValueError:
        print("\n[ERRO] Entrada inválida. Use apenas números para peso e comprimento.")

def armazenar_em_caixa(peca):
    """
    Armazena uma peça aprovada na caixa atual ou inicia uma nova.
    """
    global caixas
    
    caixa_atual = caixas[-1] # Pega a última caixa (a caixa "aberta")
    
    # Verifica se a caixa atual está cheia (capacidade 10) 
    if len(caixa_atual) >= 10:
        print(f"Caixa {len(caixas)} FECHADA (10/10).")
        caixas.append([]) # Inicia uma nova caixa [cite: 18]
        caixa_atual = caixas[-1] # Atualiza a referência para a nova caixa
    
    # Adiciona a peça na caixa atual
    caixa_atual.append(peca)
    print(f"Peça ID {peca['id']} adicionada à Caixa {len(caixas)} (Peças na caixa: {len(caixa_atual)}/10)")

def listar_pecas():
    """
    Função para listar peças aprovadas e reprovadas. [cite: 48]
    """
    print("\n--- 2. Listar Peças Aprovadas/Reprovadas ---")
    
    print("\n== Peças APROVADAS ==")
    if not pecas_aprovadas:
        print("Nenhuma peça aprovada ainda.")
    else:
        for peca in pecas_aprovadas:
            print(f"  - ID: {peca['id']} (Peso: {peca['peso']}g, Cor: {peca['cor']}, Comp: {peca['comprimento']}cm)")
            
    print("\n== Peças REPROVADAS ==")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada ainda.")
    else:
        for item in pecas_reprovadas:
            peca = item['peca']
            motivos = ', '.join(item['motivos'])
            print(f"  - ID: {peca['id']} (Motivos: {motivos})")

def remover_peca():
    """
    Função para remover uma peça das listas (aprovadas ou reprovadas). 
    """
    print("\n--- 3. Remover Peça Cadastrada ---")
    try:
        id_remover = int(input("Digite o ID da peça a ser removida: "))
        
        peca_encontrada = None
        lista_origem = None
        
        # Procura em Aprovadas
        for peca in pecas_aprovadas:
            if peca['id'] == id_remover:
                peca_encontrada = peca
                lista_origem = pecas_aprovadas
                break
                
        # Procura em Reprovadas (se não achou)
        if not peca_encontrada:
            for item in pecas_reprovadas:
                if item['peca']['id'] == id_remover:
                    peca_encontrada = item
                    lista_origem = pecas_reprovadas
                    break
        
        if peca_encontrada:
            lista_origem.remove(peca_encontrada)
            print(f"\n[SUCESSO] Peça ID {id_remover} removida.")
            
            # Desafio Bônus: Remover também da caixa (versão simples)
            if lista_origem == pecas_aprovadas:
                for caixa in caixas:
                    if peca_encontrada in caixa:
                        caixa.remove(peca_encontrada)
                        print(f"Peça ID {id_remover} também removida da sua caixa.")
                        break
        else:
            print(f"\n[ERRO] Peça com ID {id_remover} não encontrada.")
            
    except ValueError:
        print("\n[ERRO] ID inválido. Digite um número.")

def listar_caixas_fechadas():
    """
    Função para listar o conteúdo das caixas que já atingiram 10 peças. [cite: 50]
    """
    print("\n--- 4. Listar Caixas Fechadas ---")
    
    # Caixas fechadas são todas, exceto a última (se não estiver cheia)
    caixas_para_listar = caixas[:-1] # Pega todas menos a última
    caixa_atual = caixas[-1]
    
    if len(caixa_atual) == 10:
        caixas_para_listar.append(caixa_atual) # Adiciona a última se ela tb estiver cheia

    if not caixas_para_listar:
        print("Nenhuma caixa foi fechada (10/10) ainda.")
        return

    print(f"Total de caixas fechadas: {len(caixas_para_listar)}")
    for i, caixa in enumerate(caixas_para_listar, 1):
        print(f"\n== Caixa {i} (10 Peças) ==")
        ids_na_caixa = [peca['id'] for peca in caixa]
        print(f"  IDs das Peças: {ids_na_caixa}")

def gerar_relatorio_final():
    """
    Função para gerar o relatório consolidado. 
    """
    print("\n--- 5. Gerar Relatório Final ---")
    
    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas) 
    total_geral = total_aprovadas + total_reprovadas
    
    print(f"Total de Peças Processadas: {total_geral}")
    print(f"Total de Peças APROVADAS: {total_aprovadas}") 
    print(f"Total de Peças REPROVADAS: {total_reprovadas}") 
    
    print("\nMotivos de Reprovação:") 
    print(f"  - Por Peso: {contagem_reprovacao['peso']} peças")
    print(f"  - Por Cor: {contagem_reprovacao['cor']} peças")
    print(f"  - Por Comprimento: {contagem_reprovacao['comprimento']} peças")
    
    print("\nGerenciamento de Caixas:")
    total_caixas_utilizadas = len(caixas) 
    print(f"  - Total de caixas utilizadas: {total_caixas_utilizadas}")
    
    caixa_atual = caixas[-1]
    if len(caixa_atual) == 10:
         print("  - A caixa atual está FECHADA (10/10).")
    else:
         print(f"  - Peças na caixa atual (Caixa {total_caixas_utilizadas}): {len(caixa_atual)}/10")

# --- Loop Principal (Menu Interativo) ---

def menu_principal():
    """
    Exibe o menu e gerencia a entrada do usuário.
    """
    while True:
        print("\n--- Sistema de Gestão Industrial (v1.0) ---")
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_nova_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            remover_peca()
        elif opcao == '4':
            listar_caixas_fechadas()
        elif opcao == '5':
            gerar_relatorio_final()
        elif opcao == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")

# --- Ponto de Entrada ---
if __name__ == "__main__":
    menu_principal()