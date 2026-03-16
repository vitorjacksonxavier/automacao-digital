# Sistema de Gestão de Peças, Qualidade e Armazenamento
# Regras do desafio:
# - Peso entre 95g e 105g
# - Cor azul ou verde
# - Comprimento entre 10cm e 20cm
# - Peças aprovadas são organizadas em caixas de 10 unidades
# - Menu interativo com 5 opções

CAPACIDADE_CAIXA = 10
pecas = []


def normalizar_cor(cor):
    return cor.strip().lower()


def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("peso fora do padrão (95g a 105g)")

    if normalizar_cor(cor) not in ["azul", "verde"]:
        motivos.append("cor fora do padrão (apenas azul ou verde)")

    if not (10 <= comprimento <= 20):
        motivos.append("comprimento fora do padrão (10cm a 20cm)")

    if len(motivos) == 0:
        return "Aprovada", []
    else:
        return "Reprovada", motivos


def gerar_caixas(pecas_cadastradas):
    aprovadas = [peca for peca in pecas_cadastradas if peca["status"] == "Aprovada"]

    caixas_fechadas = []
    caixa_atual = []

    for peca in aprovadas:
        caixa_atual.append(peca)
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas_fechadas.append(caixa_atual)
            caixa_atual = []

    return caixas_fechadas, caixa_atual


def buscar_peca_por_id(id_peca):
    for indice, peca in enumerate(pecas):
        if peca["id"] == id_peca:
            return indice, peca
    return None, None


def cadastrar_peca():
    print("\n=== CADASTRAR NOVA PEÇA ===")

    id_peca = input("Informe o ID da peça: ").strip()

    if not id_peca:
        print("ID inválido.")
        return

    _, peca_existente = buscar_peca_por_id(id_peca)
    if peca_existente:
        print("Já existe uma peça cadastrada com esse ID.")
        return

    try:
        peso = float(input("Informe o peso da peça (em g): ").replace(",", "."))
        cor = input("Informe a cor da peça: ").strip()
        comprimento = float(input("Informe o comprimento da peça (em cm): ").replace(",", "."))
    except ValueError:
        print("Erro: peso e comprimento devem ser numéricos.")
        return

    status, motivos = avaliar_peca(peso, cor, comprimento)

    nova_peca = {
        "id": id_peca,
        "peso": peso,
        "cor": normalizar_cor(cor),
        "comprimento": comprimento,
        "status": status,
        "motivos": motivos
    }

    pecas.append(nova_peca)

    print("\nPeça cadastrada com sucesso!")
    print(f"Status da peça: {status}")
    if motivos:
        print("Motivos da reprovação:")
        for motivo in motivos:
            print(f"- {motivo}")


def listar_pecas():
    print("\n=== LISTAR PEÇAS APROVADAS/REPROVADAS ===")

    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    aprovadas = [peca for peca in pecas if peca["status"] == "Aprovada"]
    reprovadas = [peca for peca in pecas if peca["status"] == "Reprovada"]

    print("\n--- PEÇAS APROVADAS ---")
    if aprovadas:
        for peca in aprovadas:
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm"
            )
    else:
        print("Nenhuma peça aprovada.")

    print("\n--- PEÇAS REPROVADAS ---")
    if reprovadas:
        for peca in reprovadas:
            motivos_texto = "; ".join(peca["motivos"])
            print(
                f"ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm | "
                f"Motivos: {motivos_texto}"
            )
    else:
        print("Nenhuma peça reprovada.")


def remover_peca():
    print("\n=== REMOVER PEÇA CADASTRADA ===")

    if not pecas:
        print("Não há peças cadastradas para remover.")
        return

    id_peca = input("Informe o ID da peça que deseja remover: ").strip()

    indice, peca = buscar_peca_por_id(id_peca)

    if peca is None:
        print("Peça não encontrada.")
        return

    pecas.pop(indice)
    print(f"Peça de ID {id_peca} removida com sucesso.")


def listar_caixas_fechadas():
    print("\n=== LISTAR CAIXAS FECHADAS ===")

    caixas_fechadas, caixa_atual = gerar_caixas(pecas)

    if not caixas_fechadas:
        print("Nenhuma caixa fechada no momento.")
        if caixa_atual:
            print(f"Há uma caixa em formação com {len(caixa_atual)} peça(s).")
        return

    for numero_caixa, caixa in enumerate(caixas_fechadas, start=1):
        print(f"\nCaixa {numero_caixa} - FECHADA ({len(caixa)} peças)")
        for peca in caixa:
            print(
                f"  ID: {peca['id']} | Peso: {peca['peso']}g | "
                f"Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm"
            )

    if caixa_atual:
        print(f"\nExiste também uma caixa em formação com {len(caixa_atual)} peça(s).")


def gerar_relatorio_final():
    print("\n=== RELATÓRIO FINAL ===")

    total_pecas = len(pecas)
    aprovadas = [peca for peca in pecas if peca["status"] == "Aprovada"]
    reprovadas = [peca for peca in pecas if peca["status"] == "Reprovada"]

    caixas_fechadas, caixa_atual = gerar_caixas(pecas)

    motivos_reprovacao = {}

    for peca in reprovadas:
        for motivo in peca["motivos"]:
            if motivo in motivos_reprovacao:
                motivos_reprovacao[motivo] += 1
            else:
                motivos_reprovacao[motivo] = 1

    print(f"Total de peças cadastradas: {total_pecas}")
    print(f"Total de peças aprovadas: {len(aprovadas)}")
    print(f"Total de peças reprovadas: {len(reprovadas)}")
    print(f"Quantidade de caixas fechadas: {len(caixas_fechadas)}")
    print(f"Peças na caixa em formação: {len(caixa_atual)}")

    print("\n--- MOTIVOS DE REPROVAÇÃO ---")
    if motivos_reprovacao:
        for motivo, quantidade in motivos_reprovacao.items():
            print(f"{motivo}: {quantidade}")
    else:
        print("Nenhuma peça reprovada.")

    print("\n--- RESUMO DAS CAIXAS FECHADAS ---")
    if caixas_fechadas:
        for i, caixa in enumerate(caixas_fechadas, start=1):
            ids = [peca["id"] for peca in caixa]
            print(f"Caixa {i}: {len(caixa)} peças | IDs: {', '.join(ids)}")
    else:
        print("Nenhuma caixa fechada.")


def exibir_menu():
    print("\n" + "=" * 50)
    print("MENU INTERATIVO")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("=" * 50)


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio_final()
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()
