.Markdown# 🟦 Gestão de Peças - Automação Digital Industrial

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Production--Ready-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Sistema completo de controle de qualidade e logística de armazenamento desenvolvido para automatizar a inspeção de peças industriais em linhas de produção. O software aplica critérios técnicos rigorosos de aprovação, correção de dados via lógica fuzzy e gestão automatizada de embalagens.

---

## 🛠️ Funcionalidades Core

* **Cadastro com Normalização:** Tratamento automático de strings (`.strip()` + `.lower()`).
* **Avaliação Técnica (QA):**
    * **Peso:** 95g a 105g.
    * **Comprimento:** 10cm a 20cm.
    * **Cores:** Azul ou Verde.
* **Correção Inteligente:** Uso de `difflib.get_close_matches()` para corrigir erros de digitação em cores (ex: "azull" -> "azul").
* **Gestão de Caixas:** Agrupamento automático de peças aprovadas (10 peças por caixa).
* **Business Intelligence:** Relatórios detalhados com estatísticas e motivos de reprovação.

---

## 🚀 Como Executar

O sistema é **Zero Dependency** (utiliza apenas bibliotecas nativas do Python).

```bash
# Clone o repositório
git clone [https://github.com/vitorjacksonxavier/automacao-digital.git](https://github.com/vitorjacksonxavier/automacao-digital.git)

# Acesse o diretório
cd automacao-digital

# Execute a aplicação
python automacao-digital.py
🖥️ Exemplos de Uso1. Inclusão de Peça AprovadaO sistema valida os dados e aplica a correção ortográfica automática.Plaintext=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça: 101
Informe o peso da peça (em g): 100
Informe a cor da peça: azull
Informe o comprimento da peça (em cm): 15

Id: 101 | Peso: 100.0g | Cor: azul | Comprimento: 15.0cm | Status: Aprovada
Confirma o cadastro? (s/n): s
✅ Peça cadastrada com sucesso!
2. Inclusão de Peça ReprovadaOs motivos do descarte são registrados para o relatório final.Plaintext=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça: 102
Informe o peso da peça (em g): 80
Informe a cor da peça: laranja
Informe o comprimento da peça (em cm): 25

Id: 102 | Peso: 80.0g | Cor: laranja | Comprimento: 25.0cm | Status: Reprovada
Confirma o cadastro? (s/n): s
✅ Peça cadastrada com sucesso!
3. Remoção de RegistroExclusão rápida de itens via ID único.Plaintext=== REMOVER PEÇA CADASTRADA ===
Informe o ID da peça: 101
✅ Peça 101 removida com sucesso.
🏗️ Arquitetura e Boas PráticasModularização: Estrutura organizada em Constantes -> Utilitárias -> Core -> CRUD -> UI.Princípio DRY: Funções genéricas para evitar repetição de código.UX Industrial: Formatação numérica e visual adaptada para o padrão brasileiro (BR).Tabela de NormalizaçãoCampoNormalizaçãoExemploID.strip().lower()" P001 " → "p001"Cordifflib + lower()" VERDEE " → "verde"Busca.lower()Case-insensitive📊 Benefícios IndustriaisVelocidade: 10x mais rápido que a inspeção manual.Precisão: Erro zero em digitação e formatação de dados.Dados: Rastreabilidade completa dos motivos de falha na produção.Desenvolvido por Vitor Jackson v1.0 | Disciplina: Algoritmos e Lógica de Programação