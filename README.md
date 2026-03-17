Gestão de Peças - Automação Digital Industrial
==============================================

Descrição
---------
Sistema completo de controle de qualidade e armazenamento desenvolvido para automatizar a inspeção de peças industriais na linha de produção.

Disciplina: Algoritmos e Lógica de Programação

Funcionalidades
---------------
- Cadastro com normalização automática (.strip() + .lower())
- Avaliação: peso 95-105g, cor azul/verde, comprimento 10-20cm
- Correção inteligente de cores (difflib.get_close_matches())
- Caixas automáticas (10 peças/caixa)
- Relatórios com estatísticas de reprovação

Como Executar
-------------
Via GitHub (Repositório Oficial):
git clone https://github.com/vitorjacksonxavier/automacao-digital.git
cd automacao-digital
python automacao-digital


Exemplos de Entradas e Saídas
-----------------------------
==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 1

=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça: 1
Informe o peso da peça (em g): 100
Informe a cor da peça: azull
Informe o comprimento da peça (em cm): 15

==================================================
CONFIRMAÇÃO DOS DADOS DA PEÇA
==================================================
Id: 1
Peso: 100,0g
Cor: azul
Comprimento: 15,0cm
Status: Aprovada
==================================================
Confirma o cadastro? (s/n): s
✅ Peça cadastrada com sucesso!

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 1

=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça: 2
Informe o peso da peça (em g): 80 
Informe a cor da peça: laranja
Informe o comprimento da peça (em cm): 21

==================================================
CONFIRMAÇÃO DOS DADOS DA PEÇA
==================================================
Id: 2
Peso: 80,0g
Cor: laranja
Comprimento: 21,0cm
Status: Reprovada
==================================================
Confirma o cadastro? (s/n): s
✅ Peça cadastrada com sucesso!

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 2

=== LISTAR PEÇAS APROVADAS/REPROVADAS ===

--- PEÇAS APROVADAS ---
ID: 1 | Peso: 100.0g | Cor: azul | Comprimento: 15.0cm

--- PEÇAS REPROVADAS ---
ID: 2 | Peso: 80.0g | Cor: laranja | Comprimento: 21.0cm | Motivos: peso fora do padrão (95g a 105g); cor fora do padrão (apenas azul ou verde); comprimento fora do padrão (10cm a 20cm)

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 3

=== REMOVER PEÇA CADASTRADA ===
Informe o ID da peça: 1
✅ Peça 1 removida com sucesso.

AGORA SUPONHA A INSERÇÃO DE 11 PEÇAS, SENDO QUE SOMENTE ALGUMAS FORAM APROVADAS

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 1

=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça: 11
Informe o peso da peça (em g): 13
Informe a cor da peça: ciano
Informe o comprimento da peça (em cm): 200

==================================================
CONFIRMAÇÃO DOS DADOS DA PEÇA
==================================================
Id: 11
Peso: 13,0g
Cor: ciano
Comprimento: 200,0cm
Status: Reprovada
==================================================
Confirma o cadastro? (s/n): s
✅ Peça cadastrada com sucesso!

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 2

=== LISTAR PEÇAS APROVADAS/REPROVADAS ===

--- PEÇAS APROVADAS ---
ID: 1 | Peso: 95.0g | Cor: azul | Comprimento: 10.0cm
ID: 2 | Peso: 95.0g | Cor: azul | Comprimento: 10.0cm
ID: 3 | Peso: 95.0g | Cor: verde | Comprimento: 11.0cm
ID: 4 | Peso: 95.0g | Cor: azul | Comprimento: 11.0cm
ID: 5 | Peso: 96.0g | Cor: azul | Comprimento: 11.0cm

--- PEÇAS REPROVADAS ---
ID: 6 | Peso: 1.0g | Cor: azul | Comprimento: 7.0cm | Motivos: peso fora do padrão (95g a 105g); comprimento fora do padrão (10cm a 20cm)
ID: 7 | Peso: 14.0g | Cor: verde | Comprimento: 14.0cm | Motivos: peso fora do padrão (95g a 105g)
ID: 8 | Peso: 1.0g | Cor: azul | Comprimento: 200.0cm | Motivos: peso fora do padrão (95g a 105g); comprimento fora do padrão (10cm a 20cm)
ID: 9 | Peso: 13.0g | Cor: roxo | Comprimento: 150.0cm | Motivos: peso fora do padrão (95g a 105g); cor fora do padrão (apenas azul ou verde); comprimento fora do padrão (10cm a 20cm)
ID: 10 | Peso: 13.0g | Cor: amarelo | Comprimento: 12.0cm | Motivos: peso fora do padrão (95g a 105g); cor fora do padrão (apenas azul ou verde)
ID: 11 | Peso: 13.0g | Cor: ciano | Comprimento: 200.0cm | Motivos: peso fora do padrão (95g a 105g); cor fora do padrão (apenas azul ou verde); comprimento fora do padrão (10cm a 20cm)

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 4

=== LISTAR CAIXAS FECHADAS ===
Nenhuma caixa fechada.
Caixa em formação: 5 peça(s).

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 5

=== RELATÓRIO FINAL ===
Total peças: 11 | Aprovadas: 5 | Reprovadas: 6
Caixas fechadas: 0 | Em formação: 5

--- MOTIVOS DE REPROVAÇÃO ---
  peso fora do padrão (95g a 105g): 6
  comprimento fora do padrão (10cm a 20cm): 4
  cor fora do padrão (apenas azul ou verde): 3

--- CAIXAS FECHADAS ---

==================================================
🟦 GESTÃO DE PEÇAS - AUTOMACÃO INDUSTRIAL
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
==================================================
Escolha: 0
👋 Encerrando sistema. Até logo!


Normalização de Dados
---------------------
Campo        | Normalização      | Exemplo
-------------|-------------------|-----------
ID           | .strip().lower()  | " P001 " -> "p001"
Cor          | difflib + lower() | " AZULL " -> "azul"
Busca        | .lower()          | "P001" encontra "p001"

Arquitetura 
------------------------
Constantes -> Utilitárias -> Core -> CRUD -> UI

Boas Práticas
-------------
- Zero dependências (Python nativo)
- Normalização robusta (.strip() + .lower())
- DRY (funções genéricas)
- UX industrial (formatação BR)

Benefícios Industriais
----------------------
- 10x mais rápido que inspeção manual
- Zero erros de digitação/formatação
- Rastreabilidade completa dos defeitos

Repositório: https://github.com/vitorjacksonxavier/automacao-digital
v1.0 | Production Ready | Algoritmos e Lógica de Programação