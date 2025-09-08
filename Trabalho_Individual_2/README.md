# Projeto Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select)

Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python.

**Sobre o algoritmo:**
- O algoritmo de seleção simultânea (MaxMin Select) pode ser implementado de forma recursiva, utilizando a técnica de divisão e conquista.
- O problema é dividido em subproblemas menores que são resolvidos recursivamente, e seus resultados são combinados para encontrar o maior e o menor elementos com eficiência.
- Esse método reduz o número de comparações necessárias em comparação com uma abordagem ingênua.

##  Lógica do Algoritmo

O algoritmo utiliza **Divisão e Conquista**:

1. **Casos base**:
   - Para 1 elemento: `min = max`, 0 comparações.
   - Para 2 elementos: 1 comparação decide quem é o menor e quem é o maior.

2. **Passo recursivo**:
   - Divide o vetor em duas metades.
   - Resolve recursivamente cada metade → `(min_esq, max_esq)` e `(min_dir, max_dir)`.
   - Combina os resultados com **2 comparações**:
     - `min = min(min_esq, min_dir)`
     - `max = max(max_esq, max_dir)`

### Número de comparações
- Para `n` potência de 2:
  - `T(1) = 0`, `T(2) = 1`,  
  - `T(n) = 2T(n/2) + 2` → **`T(n) = 3n/2 - 2`**.  
- Para `n` geral:
  - Número de comparações **≤ ⌈3n/2⌉ - 2**, sempre menor que `2(n-1)` da abordagem ingênua.

### Complexidade
- **Tempo**: `O(n)`  
- **Espaço**: `O(log n)` (pela recursão)

## Como executar o projeto

### 1) Rodar manualmente
Permite digitar os números diretamente no terminal:
```bash
python main.py
```
Menu → `[1]` Rodar manualmente (D&C)  
Exemplo de entrada:
```
Digite os números (separados por espaço/vírgula): 5 3 9 -2 10
```

### 2) Rodar manualmente + comparar com baseline
Além do algoritmo otimizado, mostra também o **baseline ingênuo** (O(n)) para comparar o número de comparações.  
Menu → `[2]`.

### 3) Gerar números aleatórios
Permite gerar uma lista de inteiros aleatórios:
```bash
Quantidade de números (n ≥ 1): 6
Seed (opcional, Enter para padrão 123): 42
```
Menu → `[3]` ou `[4]` (se quiser também ver a comparação com baseline).

### 4) Rodar testes prontos
Executa casos fixos de teste e valida os resultados com `min()` e `max()` do Python.
Menu → `[5]` ou `[6]` (com baseline).

## Exemplo do Menu
```
==============================================
  MaxMin Select (Divisão & Conquista) - Menu
==============================================
[1] Rodar manualmente (D&C)
[2] Rodar manualmente (D&C) + comparar com baseline
[3] Gerar aleatórios (D&C)
[4] Gerar aleatórios (D&C) + comparar com baseline
[5] Rodar testes prontos (D&C)
[6] Rodar testes prontos (D&C) + baseline
[0] Sair
```

## Exemplo de saída
```
== Gerar aleatórios ==
Quantidade de números (n ≥ 1): 6
Seed (opcional, Enter para padrão 123): 42

Entrada: [10, -23, 45, 0, 99, -100]
Tamanho (n): 6 | Limite teórico ≤ ceil(3n/2) - 2 = 7

[Divisão e Conquista]
Min, Max: (-100.0, 99.0)
Comparações: 8  | Tempo: 0.005 ms

[Baseline Ingênuo]
Min, Max: (-100.0, 99.0)
Comparações: 10 | Tempo: 0.002 ms

Comparativo (Ingênuo - D&C): +2 comparações
```
