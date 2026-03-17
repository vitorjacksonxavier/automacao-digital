# 🏭 Sistema de Gestão de Peças – Automação Digital

## 📦 Repositório
Este projeto está associado ao repositório **automacao-digital**:

- Repositório: https://github.com/vitorjacksonxavier/automacao-digital
- Arquivo principal de execução: automacaodigital.py

---

## 🔎 Visão geral
O sistema realiza o cadastro, avaliação e organização de peças industriais com base em critérios de qualidade.

Cada peça é avaliada pelos seguintes parâmetros:

- ⚖️ Peso: entre 95 g e 105 g  
- 🎨 Cor válida para aprovação: azul ou verde  
- 📏 Comprimento: entre 10 cm e 20 cm  

Peças aprovadas são agrupadas automaticamente em caixas com capacidade de 10 unidades.

---

## ⚙️ Funcionalidades
- ➕ Cadastro de nova peça  
- ✅ Validação de entradas  
- 🎯 Correção aproximada de cor com difflib  
- 📄 Listagem de peças aprovadas e reprovadas  
- 🗑️ Remoção de peça por ID  
- 📦 Geração de caixas fechadas  
- 📊 Relatório final consolidado  

---

## 🧩 Requisitos
- Python 3.10 ou superior  

---

## ▶️ Como executar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/vitorjacksonxavier/automacao-digital.git
```

### 2️⃣ Acessar a pasta do projeto
```bash
cd automacao-digital
```

### 3️⃣ Executar o programa
```bash
python automacaodigital.py
```

ou:

```bash
python3 automacaodigital.py
```

---

## 📋 Estrutura do menu
```text
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
```

---

## ✅ Regras de aprovação
Uma peça será aprovada somente se:

1. Peso entre 95 e 105 g  
2. Cor igual a azul ou verde  
3. Comprimento entre 10 e 20 cm  

Caso contrário → Reprovada

---

## 🧪 Exemplos de uso

### ✔️ Cadastro aprovado
```text
ID: p001
Peso: 100
Cor: azul
Comprimento: 15
→ Aprovada
```

### ❌ Cadastro reprovado
```text
ID: p002
Peso: 110
Cor: vermelho
Comprimento: 25
→ Reprovada
```

Motivos:
- peso fora do padrão  
- cor fora do padrão  
- comprimento fora do padrão  

### 🎯 Correção de cor
Entrada: azu  
Saída: azul  

---

### 📦 Caixas
- 10 aprovadas → 1 caixa  
- 23 aprovadas → 2 caixas + 3 peças  

---

### 📊 Relatório
```text
Total: 12
Aprovadas: 10
Reprovadas: 2
Caixas: 1
```

---

## 🧠 Observações
- ID deve ser único  
- Aceita vírgula ou ponto  
- Correção de cor é aproximada  

---

## 🚀 Melhorias futuras
- Persistência (JSON/DB)  
- Edição de peças  
- Exportação de relatórios  
- Testes automatizados  
- Interface gráfica  

---

## 📜 Licença
Definir conforme necessidade  
