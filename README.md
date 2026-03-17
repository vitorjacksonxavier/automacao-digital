# Sistema de Gestão de Peças – Automação Digital

## Repositório

Este projeto está associado ao repositório **automacao-digital**:

* Repositório: `https://github.com/vitorjacksonxavier/automacao-digital`
* Arquivo principal de execução: `automacaodigital.py`

## Visão geral

O sistema realiza o cadastro, avaliação e organização de peças industriais com base em critérios de qualidade.

Cada peça é avaliada pelos seguintes parâmetros:

* **Peso:** entre 95 g e 105 g
* **Cor válida para aprovação:** azul ou verde
* **Comprimento:** entre 10 cm e 20 cm

Peças aprovadas são agrupadas automaticamente em caixas com capacidade de **10 unidades**.

## Funcionalidades

* Cadastro de nova peça
* Validação de entradas
* Correção aproximada de cor com `difflib` (apenas para azul ou verde)
* Listagem de peças aprovadas e reprovadas
* Remoção de peça por ID
* Geração de caixas fechadas
* Relatório final consolidado

## Requisitos

* Python 3.10 ou superior

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python automacaodigital.py
```

Em alguns ambientes, pode ser necessário usar:

```bash
python3 automacaodigital.py
```

## Estrutura do menu

Ao iniciar, o sistema exibe o seguinte menu:

```text
1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
0. Sair
```

## Regras de aprovação

Uma peça será **aprovada** somente se atender simultaneamente a todos os critérios abaixo:

1. Peso entre 95 e 105 g
2. Cor igual a `azul` ou `verde`
3. Comprimento entre 10 e 20 cm

Caso algum critério não seja atendido, a peça será **reprovada**, e o sistema registrará os motivos.

## Exemplos de uso

### 1) Cadastro de peça aprovada

Exemplo de interação:

```text
=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça: p001
Informe o peso da peça (em g): 100
Informe a cor da peça: azul
Informe o comprimento da peça (em cm): 15

==================================================
CONFIRMAÇÃO DOS DADOS DA PEÇA
==================================================
Id: p001
Peso: 100,0g
Cor: azul
Comprimento: 15,0cm
Status: Aprovada
==================================================
Confirma o cadastro? (s/n): s
✅ Peça cadastrada com sucesso!
```

### 2) Cadastro de peça reprovada

```text
=== CADASTRAR NOVA PEÇA ===
Informe o ID da peça: p002
Informe o peso da peça (em g): 110
Informe a cor da peça: vermelho
Informe o comprimento da peça (em cm): 25

==================================================
CONFIRMAÇÃO DOS DADOS DA PEÇA
==================================================
Id: p002
Peso: 110,0g
Cor: vermelho
Comprimento: 25,0cm
Status: Reprovada
==================================================
Confirma o cadastro? (s/n): s
✅ Peça cadastrada com sucesso!
```

Nesse caso, a peça será reprovada por:

* peso fora do padrão
* cor fora do padrão
* comprimento fora do padrão

### 3) Correção aproximada de cor digitada

O sistema usa `difflib` para tentar corrigir pequenas variações de digitação nas cores válidas.

Exemplo:

```text
Informe a cor da peça: azu
```

O sistema pode interpretar como:

```text
Cor: azul
```

Isso ajuda em erros simples de digitação, desde que a entrada esteja suficientemente próxima de `azul` ou `verde`.

### 4) Listagem de peças

Exemplo:

```text
=== LISTAR PEÇAS APROVADAS/REPROVADAS ===

--- PEÇAS APROVADAS ---
ID: p001 | Peso: 100.0g | Cor: azul | Comprimento: 15.0cm

--- PEÇAS REPROVADAS ---
ID: p002 | Peso: 110.0g | Cor: vermelho | Comprimento: 25.0cm | Motivos: peso fora do padrão (95g a 105g); cor fora do padrão (apenas azul ou verde); comprimento fora do padrão (10cm a 20cm)
```

### 5) Remoção de peça

```text
=== REMOVER PEÇA CADASTRADA ===
Informe o ID da peça: p002
✅ Peça p002 removida com sucesso.
```

### 6) Formação de caixas

A cada 10 peças aprovadas, o sistema fecha automaticamente uma caixa.

Exemplo conceitual:

* 10 peças aprovadas → 1 caixa fechada
* 23 peças aprovadas → 2 caixas fechadas e 3 peças em formação

Saída esperada:

```text
=== LISTAR CAIXAS FECHADAS ===

Caixa 1 - FECHADA (10 peças)
  ID: p001 | Peso: 100.0g | Cor: azul | Comprimento: 15.0cm
  ...

Caixa em formação: 3 peça(s).
```

### 7) Relatório final

Exemplo:

```text
=== RELATÓRIO FINAL ===
Total peças: 12 | Aprovadas: 10 | Reprovadas: 2
Caixas fechadas: 1 | Em formação: 0

--- MOTIVOS DE REPROVAÇÃO ---
  peso fora do padrão (95g a 105g): 1
  cor fora do padrão (apenas azul ou verde): 2
  comprimento fora do padrão (10cm a 20cm): 1

--- CAIXAS FECHADAS ---
  Caixa 1: 10 peças | IDs: p001, p003, p004, p005, p006, p007, p008, p009, p010, p011
```

## Observações técnicas

* O ID da peça deve ser único.
* Campos numéricos aceitam vírgula ou ponto como separador decimal.
* Campos de texto com `apenas_letras=True` aceitam somente letras e espaços.
* A função `normalizar_cor()` tenta aproximar a cor digitada das cores válidas para fins de avaliação.

##
