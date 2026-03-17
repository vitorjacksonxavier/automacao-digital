import difflib

# ========================================
# CONFIGURAÇÕES DO SISTEMA (CONSTANTES)
# ========================================
PESO_MIN, PESO_MAX = 95, 105
COMP_MIN, COMP_MAX = 10, 20
CORES_VALIDAS = {"azul", "verde"}
CAPACIDADE_CAIXA = 10
pecas = []


# ========================================
# FUNÇÕES UTILITÁRIAS (GENÉRICAS)
# ========================================
def formatar_numero(valor):
    """Formata número com vírgula como separador decimal (padrão BR)"""
    return f"{valor:.1f}".replace('.', ',')


def ler_numero(mensagem):
    """Lê número com validação robusta"""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        if not entrada:
            print("Erro: campo obrigatório.")
            continue
        try:
            return float(entrada)
        except ValueError:
            print("Erro: informe um número válido.")


def ler_texto(mensagem, apenas_letras=False):
    """Lê texto com validações específicas"""
    while True:
        texto = input(mensagem).strip()
        if not texto:
            print("Erro: campo obrigatório.")
            continue
        if apenas_letras and not texto.replace(" ", "").isalpha():
            print("Erro: deve conter apenas letras.")
            continue
        return texto


def normalizar_cor(cor):
    """Corrige erros de digitação em cores válidas usando difflib"""
    cor_digitada = cor.strip().lower()
    correspondencia = difflib.get_close_matches(cor_digitada, ["azul", "verde"], n=1, cutoff=0.8)
    return correspondencia[0] if correspondencia else cor_digitada


def confirmar_cadastro(dados):
    """Exibe confirmação formatada e aguarda aprovação"""
    print("\n" + "=" * 50)
    print("CONFIRMAÇÃO DOS DADOS DA PEÇA")
    print("=" * 50)
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")
    print("=" * 50)
    
    while True:
        resp = input("Confirma o cadastro? (s/n): ").strip().lower()
        if resp in {'s', 'sim', 'y', 'yes'}:
            return True
        if resp in {'n', 'não', 'nao', 'no'}:
            print("\n❌ Cadastro cancelado pelo usuário.")
            return False
        print("Digite 's' para confirmar ou 'n' para cancelar.")


# ========================================
# LÓGICA DE NEGÓCIO (CORE)
# ========================================
def avaliar_peca(peso, cor, comprimento):
    """Avalia se peça atende aos critérios de qualidade"""
    motivos = []
    
    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append("peso fora do padrão (95g a 105g)")
    
    if normalizar_cor(cor) not in CORES_VALIDAS:
        motivos.append("cor fora do padrão (apenas azul ou verde)")
    
    if not (COMP_MIN <= comprimento <= COMP_MAX):
        motivos.append("comprimento fora do padrão (10cm a 20cm)")
    
    # SEMPRE retorna TUPLA consistente
    if not motivos:
        return "Aprovada", []
    return "Reprovada", motivos



def gerar_caixas(pecas_cadastradas):
    """Gera caixas fechadas e caixa atual a partir das peças aprovadas"""
    aprovadas = [p for p in pecas_cadastradas if p["status"] == "Aprovada"]
    caixas_fechadas, caixa_atual = [], []
    
    for peca in aprovadas:
        caixa_atual.append(peca)
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas_fechadas.append(caixa_atual)
            caixa_atual = []
    
    return caixas_fechadas, caixa_atual


def buscar_peca_por_id(id_peca):
    """Busca peça por ID e retorna índice e objeto"""
    for i, peca in enumerate(pecas):
        if peca["id"] == id_peca:
            return i, peca
    return None, None


# ========================================
# OPERAÇÕES DO SISTEMA (CRUD)
# ========================================
def cadastrar_peca():
    """Cadastra nova peça com validações completas"""
    print("\n=== CADASTRAR NOVA PEÇA ===")
    
    id_peca = ler_texto("Informe o ID da peça: ").lower()
    if not id_peca or buscar_peca_por_id(id_peca)[1]:
        print("❌ ID inválido ou já existe.")
        return

    peso = ler_numero("Informe o peso da peça (em g): ")
    cor = ler_texto("Informe a cor da peça: ", apenas_letras=True)
    comprimento = ler_numero("Informe o comprimento da peça (em cm): ")

    status, motivos = avaliar_peca(peso, cor, comprimento)
    
    dados_confirmacao = {
        "id": id_peca,
        "peso": f"{formatar_numero(peso)}g",
        "cor": normalizar_cor(cor),
        "comprimento": f"{formatar_numero(comprimento)}cm",
        "status": status
    }
    
    if confirmar_cadastro(dados_confirmacao):
        pecas.append({
            "id": id_peca, "peso": peso, "cor": normalizar_cor(cor),
            "comprimento": comprimento, "status": status, "motivos": motivos
        })
        print("✅ Peça cadastrada com sucesso!")


def listar_pecas():
    """Lista peças aprovadas e reprovadas"""
    print("\n=== LISTAR PEÇAS APROVADAS/REPROVADAS ===")
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    aprovadas = [p for p in pecas if p["status"] == "Aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "Reprovada"]

    print("\n--- PEÇAS APROVADAS ---")
    [print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm") 
     for p in aprovadas] or print("Nenhuma peça aprovada.")

    print("\n--- PEÇAS REPROVADAS ---")
    for p in reprovadas:
        motivos = "; ".join(p["motivos"])
        print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm | Motivos: {motivos}")
    if not reprovadas:
        print("Nenhuma peça reprovada.")


def remover_peca():
    """Remove peça por ID"""
    print("\n=== REMOVER PEÇA CADASTRADA ===")
    if not pecas:
        print("Não há peças cadastradas.")
        return

    id_peca = ler_texto("Informe o ID da peça: ").lower()
    indice, peca = buscar_peca_por_id(id_peca)
    
    if peca:
        pecas.pop(indice)
        print(f"✅ Peça {id_peca} removida com sucesso.")
    else:
        print("❌ Peça não encontrada.")


def listar_caixas_fechadas():
    """Lista caixas fechadas e caixa em formação"""
    print("\n=== LISTAR CAIXAS FECHADAS ===")
    caixas_fechadas, caixa_atual = gerar_caixas(pecas)
    
    if not caixas_fechadas:
        print("Nenhuma caixa fechada.")
        if caixa_atual:
            print(f"Caixa em formação: {len(caixa_atual)} peça(s).")
        return

    for i, caixa in enumerate(caixas_fechadas, 1):
        print(f"\nCaixa {i} - FECHADA ({len(caixa)} peças)")
        for p in caixa:
            print(f"  ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
    
    if caixa_atual:
        print(f"\nCaixa em formação: {len(caixa_atual)} peça(s).")


def gerar_relatorio_final():
    """Gera relatório consolidado"""
    print("\n=== RELATÓRIO FINAL ===")
    total = len(pecas)
    aprovadas = sum(1 for p in pecas if p["status"] == "Aprovada")
    reprovadas = total - aprovadas
    caixas_fechadas, caixa_atual = gerar_caixas(pecas)

    motivos_reprovacao = {}
    for p in (p for p in pecas if p["status"] == "Reprovada"):
        for motivo in p["motivos"]:
            motivos_reprovacao[motivo] = motivos_reprovacao.get(motivo, 0) + 1

    print(f"Total peças: {total} | Aprovadas: {aprovadas} | Reprovadas: {reprovadas}")
    print(f"Caixas fechadas: {len(caixas_fechadas)} | Em formação: {len(caixa_atual)}")

    print("\n--- MOTIVOS DE REPROVAÇÃO ---")
    for motivo, qtd in motivos_reprovacao.items():
        print(f"  {motivo}: {qtd}")
    if not motivos_reprovacao:
        print("  Nenhuma reprovação.")

    print("\n--- CAIXAS FECHADAS ---")
    for i, caixa in enumerate(caixas_fechadas, 1):
        ids = ", ".join(p["id"] for p in caixa)
        print(f"  Caixa {i}: {len(caixa)} peças | IDs: {ids}")


# ========================================
# INTERFACE DO USUÁRIO
# ========================================
MENU_OPCOES = {
    "1": cadastrar_peca,
    "2": listar_pecas,
    "3": remover_peca,
    "4": listar_caixas_fechadas,
    "5": gerar_relatorio_final
}


def exibir_menu():
    """Exibe menu formatado"""
    print("\n" + "=" * 50)
    print("🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("=" * 50)


def main():
    """Loop principal do sistema"""
    print("🚀 Iniciando Sistema de Gestão de Peças...")
    while True:
        exibir_menu()
        opcao = input("Escolha: ").strip()
        
        if opcao == "0":
            print("👋 Encerrando sistema. Até logo!")
            break
        elif opcao in MENU_OPCOES:
            MENU_OPCOES[opcao]()
        else:
            print("❌ Opção inválida!")

main()