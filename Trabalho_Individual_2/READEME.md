# Projeto: Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select)

## Enunciado
Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select) em Python.

**Objetivo:**
1. Desenvolver um programa em Python que implemente o algoritmo de seleção simultânea do maior e do menor elementos (MaxMin Select) de uma sequência de números, utilizando a abordagem de divisão e conquista.  
2. O projeto deverá ser entregue por meio de um link para o repositório do GitHub no CANVAS.

**Sobre o algoritmo:**
- O algoritmo de seleção simultânea (MaxMin Select) pode ser implementado de forma recursiva, utilizando a técnica de divisão e conquista.
- O problema é dividido em subproblemas menores que são resolvidos recursivamente, e seus resultados são combinados para encontrar o maior e o menor elementos com eficiência.
- Esse método reduz o número de comparações necessárias em comparação com uma abordagem ingênua.


## 📌 Objetivo da Implementação
Dado um array de números, encontrar `(min, max)` realizando **menos comparações** do que a abordagem ingênua (que usa `2(n-1)` comparações).

## 🧠 Ideia do Algoritmo (Divisão e Conquista)

1. **Caso base**:
   - `n = 1` → `(a, a)` sem comparações.
   - `n = 2` → 1 comparação para ordenar o par `(min, max)`.
2. **Passo recursivo**:
   - Dividir a sequência em duas metades esquerda/direita.
   - Resolver recursivamente cada metade → `(min_L, max_L)` e `(min_R, max_R)`.
   - **Combinar** com **2 comparações**:
     - `min = min(min_L, min_R)`
     - `max = max(max_L, max_R)`

## 🔢 Análise do Número de Comparações

Para `n` potência de 2, a recorrência é:

- `T(1) = 0`, `T(2) = 1`
- `T(n) = 2·T(n/2) + 2`

Resolvendo, obtemos: **`T(n) = 3n/2 - 2`**.

Para `n` geral (não necessariamente potência de 2), o limite permanece **≤ ⌈3n/2⌉ − 2** comparações, que é **bem menor** do que as `2(n−1)` da solução ingênua.

**Complexidade de tempo**: `O(n)`  
**Complexidade de espaço**: `O(log n)` (profundidade da recursão).  

## 🚀 Como executar (CLI)

```bash
# Usando números passados em linha de comando
python -m src.main 5 3 9 -2 9 10 10 4

# Lendo de arquivo (um número por linha ou separados por espaço)
python -m src.main --file dados.txt

# Gerando aleatórios (útil para testar)
python -m src.main --random 15 --seed 42
