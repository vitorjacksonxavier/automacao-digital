## 📝 Descrição

Sistema completo de **controle de qualidade e armazenamento** desenvolvido para automatizar a inspeção de peças industriais na linha de produção.

**Disciplina:** Algoritmos e Lógica de Programação 

## 🎯 Funcionalidades

- ✅ Cadastro com **normalização automática** (`.strip()` + `.lower()`)
- ✅ Avaliação: peso **95-105g**, cor **azul/verde**, comprimento **10-20cm**
- ✅ **Correção inteligente** de cores (`difflib.get_close_matches()`)
- ✅ Caixas automáticas (**10 peças/caixa**)
- ✅ Relatórios com **estatísticas de reprovação**

## 🚀 Como Executar

### Via GitHub (Repositório Oficial)

```bash
git clone https://github.com/vitorjacksonxavier/automacao-digital.git
cd automacao-digital
python automacaodigital.py

🖥️ Exemplos de Entradas e Saídas
Teste 1: Peça VÁLIDA

=== CADASTRAR NOVA PEÇA ===
ID: P001 
Peso: 100
Cor: azull    ← Corrigido para "azul"
Comprimento: 15

CONFIRMAÇÃO:
ID: p001
Peso: 100,0g
Cor: azul ✓
Status: Aprovada ✓

Teste 2: Peça REPROVADA (Peso baixo)
text
ID: P002
Peso: 80       ← Fora do padrão
Cor: Verde
Comprimento: 12

CONFIRMAÇÃO:
Status: Reprovada
Motivos: peso fora do padrão (95g a 105g)
Teste 3: Relatório Completo

=== RELATÓRIO FINAL ===
Total peças: 5 | Aprovadas: 3 | Reprovadas: 2
Caixas fechadas: 0 | Em formação: 3

--- MOTIVOS DE REPROVAÇÃO ---
peso fora do padrão (95g a 105g): 1
cor fora do padrão (apenas azul ou verde): 1

--- LISTAR PEÇAS ---
PEÇAS APROVADAS:
ID: p001 | Peso: 100g | Cor: azul | Comprimento: 15cm

Teste 4: Caixas Fechadas

Cadastrar 11 peças aprovadas →
Caixa 1 - FECHADA (10 peças)
Caixa em formação: 1 peça

🏗️ Arquitetura
📊 Constantes → 🔧 Utilitárias → 🧠 Core → ⚙️ CRUD → 🎛️ UI

💎 Boas Práticas
Zero dependências (Python nativo)

Normalização robusta (.strip() + .lower())

DRY (funções genéricas)

UX industrial (formatação BR)

📈 Benefícios Industriais
10x mais rápido que inspeção manual

Zero erros de digitação/formatação

Rastreabilidade completa dos defeitos

🛠️ v1.0 | https://github.com/vitorjacksonxavier/automacao-digital
Production Ready | Algoritmos e Lógica de Programação

