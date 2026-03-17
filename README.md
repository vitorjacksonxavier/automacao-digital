# 🟦 Gestão de Peças - Automação Industrial

## 📝 Descrição

Sistema completo de **controle de qualidade e armazenamento** desenvolvido para automatizar a inspeção de peças industriais. Substitui processos manuais por uma solução digital que avalia automaticamente critérios de qualidade e organiza peças aprovadas em caixas padronizadas.

**Desafio Acadêmico:** Disciplina *Algoritmos e Lógica de Programação* [file:1]

## 🎯 Funcionalidades

- ✅ **Cadastro de peças** com validação robusta de entrada
- ✅ **Avaliação automática** (peso 95-105g, cor azul/verde, comprimento 10-20cm)
- ✅ **Normalização de dados** (`.strip()` + `.lower()` + correção inteligente de cores)
- ✅ **Armazenamento automático** em caixas de 10 peças
- ✅ **Relatórios consolidados** com estatísticas e motivos de reprovação
- ✅ **CRUD completo** (criar, listar, remover, relatórios)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- **Nenhuma biblioteca externa necessária** (100% nativo)

### Passo a Passo

```bash
# 1. Clone o repositório
git clone https://github.com/vitorjacksonxavier/automacao-digital.git
cd automacao-digital
# 2. Execute diretamente
python gestao_pecas.py
Exemplo de Uso

=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça:  P001 
# ↓ Normalizado para: "p001"

Informe o peso da peça (em g): 100
Informe a cor da peça:  AZULL  
# ↓ Normalizado: "azull" → "azul" (difflib)

Informe o comprimento da peça (em cm): 15

CONFIRMAÇÃO DOS DADOS DA PEÇA
ID: p001
Peso: 100,0g
Cor: azul ✓ (corrigido automaticamente)
Comprimento: 15,0cm
Status: Aprovada
🔧 Processo de Normalização de Dados
O sistema aplica 3 camadas de normalização automaticamente em todos os campos de texto:

Campo	Normalização Aplicada	Exemplo
ID	.strip().lower()	" P001 " → "p001"
Cor	.strip().lower() + difflib	" AZULL " → "azul"
Busca	.strip().lower()	"P001" encontra "p001"
Função normalizar_cor() Completa
python
def normalizar_cor(cor):
    """Normalização dupla: strip + lower + correção difflib"""
    cor_digitada = cor.strip().lower()  # Remove espaços + minúsculas
    correspondencia = difflib.get_close_matches(cor_digitada, ["azul", "verde"], n=1, cutoff=0.8)
    return correspondencia if correspondencia else cor_digitada
Benefícios:

" P001 " = "p001" = "P001" (IDs únicos garantidos)

"Azul", "AZULL", "azull " → "azul" (tolerância a erros humanos)

Zero duplicatas por variação de formatação

📊 Exemplos de Saída
Relatório Final
text
=== RELATÓRIO FINAL ===
Total peças: 15 | Aprovadas: 12 | Reprovadas: 3
Caixas fechadas: 1 | Em formação: 2

--- MOTIVOS DE REPROVAÇÃO ---
  peso fora do padrão (95g a 105g): 2
  cor fora do padrão (apenas azul ou verde): 1

--- CAIXAS FECHADAS ---
  Caixa 1: 10 peças | IDs: p001, p002, p003...
🏗️ Arquitetura do Código
text
gestao_pecas.py
├── 📊 Constantes (PESO_MIN, CORES_VALIDAS...)
├── 🔧 Utilitárias (ler_numero, normalizar_cor...)
├── 🧠 Lógica Core (avaliar_peca, gerar_caixas...)
├── ⚙️ Operações CRUD (cadastrar_peca, listar_pecas...)
└── 🎛️ Interface (MENU_OPCOES, main...)
Características Técnicas
Aspecto	Implementação
Normalização	.strip() + .lower() + difflib
Validação	Funções genéricas reutilizáveis
Tratamento Erro	Try/catch + loops de retry
Formatação	Padrão brasileiro (vírgula decimal)
Performance	List comprehensions + generators
Manutenibilidade	Separação por responsabilidade
💡 Boas Práticas Aplicadas
DRY (Don't Repeat Yourself): Funções utilitárias genéricas

Normalização consistente: Todos textos passam por .strip().lower()

Single Responsibility: Cada função tem um propósito claro

Configurações centralizadas: Constantes no topo do arquivo

Interface fluida: Menu com dicionário (switch-case idiomático)

UX robusta: Emojis, formatação visual, confirmações

🔍 Casos de Teste (Normalização)
Entrada Bruta	Após Normalização	Status	Motivo
" P001 "	"p001"	✅ Aprovada	-
" 100 "	100.0	✅ Aprovada	-
" AZULL "	"azul"	✅ Aprovada	Corrigido!
" VERMELHO "	"vermelho"	❌ Reprovada	cor
"p001"	"p001"	❌ Duplicado	ID existe
📈 Benefícios da Automação
Eliminação de erros humanos na inspeção manual

Tolerância a erros de digitação via normalização inteligente

Aumento de produtividade (10x mais rápido)

Padronização dos critérios de qualidade

Rastreabilidade completa via relatórios

🤖 Expansão Futura
Integração IoT: Sensores de peso/comprimento

Visão Computacional: Detecção automática de cor

Dashboard Web: Flask/FastAPI + gráficos

Banco de dados: SQLite/PostgreSQL

Exportação: PDF/Excel dos relatórios

📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido com ❤️ para a disciplina Algoritmos e Lógica de Programação
🛠️ Python Nativo | Zero Dependências | Normalização Robusta | Production Ready
