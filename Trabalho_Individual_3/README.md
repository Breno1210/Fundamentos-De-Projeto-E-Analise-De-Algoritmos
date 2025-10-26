# Caminho Hamiltoniano — Grafos dirigidos e não dirigidos

Implementação, uso e análise de um algoritmo por **backtracking** para decidir/extrair um **caminho hamiltoniano** (visita cada vértice exatamente uma vez) em grafos **dirigidos** e **não dirigidos**.

## Sumário
1. [Descrição do projeto](#descrição-do-projeto)  
   1.1 [Ideia do algoritmo](#ideia-do-algoritmo)  
   1.2 [Estrutura do código](#estrutura-do-código)  
   1.3 [Explicação “linha a linha”](#explicação-linha-a-linha)  
2. [Como executar o projeto](#como-executar-o-projeto)  
3. [Relatório técnico](#relatório-técnico)  
   3.1 [Classes de complexidade: P, NP, NP-Completo, NP-Difícil](#31-classes-de-complexidade-p-np-np-completo-np-difícil)  
   3.2 [Complexidade temporal do algoritmo](#32-complexidade-temporal-do-algoritmo)  
   3.3 [Teorema Mestre — aplicabilidade](#33-teorema-mestre--aplicabilidade)  
   3.4 [Casos: melhor, médio e pior](#34-casos-melhor-médio-e-pior)

## Descrição do projeto

### Ideia do algoritmo
Usamos **backtracking**: construímos incrementalmente um caminho. Começamos por um vértice inicial, tentamos estender para um vizinho ainda **não visitado** e recursamos. Se travar, fazemos **backtrack** (desfaz o último passo e tenta outro vizinho). Se o caminho atingir `n` vértices (onde `n` é o total do grafo), encontramos um **caminho hamiltoniano**.

- Funciona para **dirigido** (usa a direção da aresta) e **não dirigido** (duplica as arestas em ambos sentidos).
- É **exponencial** no pior caso (problema NP-completo); mantivemos a implementação **simples e didática**.

### Estrutura do código
```
.
├── hamiltonian.py   
└── main.py          
```

### Explicação “linha a linha”

#### `hamiltonian.py`
```python
from typing import Dict, List, Optional

Grafo = Dict[int, List[int]]
```
- Define um tipo simples de grafo: dicionário `v -> lista_de_vizinhos`.

```python
def montar_adjacencia(n: int, arestas: List[tuple[int, int]], dirigido: bool) -> Grafo:
    adj: Grafo = {v: [] for v in range(n)}
    for u, v in arestas:
        if 0 <= u < n and 0 <= v < n:
            adj[u].append(v)
            if not dirigido and u != v:
                adj[v].append(u)
```
- Cria **lista de adjacência** com vértices `0..n-1`.  
- Se **não dirigido**, adiciona a aresta inversa também.

```python
    for v in adj:
        vistos = set()
        ordenados = []
        for w in adj[v]:
            if w not in vistos:
                vistos.add(w)
                ordenados.append(w)
        adj[v] = ordenados
    return adj
```
- Remove duplicatas simples e devolve a adjacência.

```python
def caminho_hamiltoniano(adj: Grafo, verbose: bool = False) -> Optional[List[int]]:
    n = len(adj)
    vertices = list(adj.keys())
    step = [0]
```
- Guarda `n`, lista de vértices e um **contador de passos** (para logs).

```python
    def log(depth: int, msg: str) -> None:
        if not verbose:
            return
        step[0] += 1
        indent = "  " * depth
        print(f"[{step[0]:04d}] {indent}{msg}")
```
- Função auxiliar de **log**, indentada por profundidade da recursão (ativa quando `verbose=True`).

```python
    def backtrack(caminho: List[int], visitados: set[int], depth: int) -> bool:
        if len(caminho) == n:
            log(depth, f"✓ Caminho completo: {caminho}")
            return True
```
- **Caso base**: caminho já contém todos os `n` vértices.

```python
        ultimo = caminho[-1]
        candidatos = adj.get(ultimo, [])
        log(depth, f"Na posição {len(caminho)-1}, último={ultimo}, candidatos={candidatos}")
```
- Pega o último vértice do caminho e lista de **vizinhos candidatos**.

```python
        for viz in candidatos:
            if viz in visitados:
                log(depth, f"Ignora {ultimo}->{viz} (já visitado)")
                continue

            log(depth, f"Tenta {ultimo}->{viz}")
            visitados.add(viz)
            caminho.append(viz)
            log(depth + 1, f"Entrou: caminho={caminho}")

            if backtrack(caminho, visitados, depth + 1):
                return True
```
- **Escolha**: tenta um vizinho ainda não visitado, marca como visitado e recursa.

```python
            caminho.pop()
            visitados.remove(viz)
            log(depth + 1, f"Backtrack de {viz}; caminho={caminho}")
```
- **Backtrack**: desfaz a escolha se não levou à solução.

```python
        log(depth, f"Sem opções válidas a partir de {ultimo}")
        return False
```
- Se nenhum vizinho funcionou, sinaliza fracasso nesta ramificação.

```python
    for inicio in vertices:
        caminho = [inicio]
        visitados = {inicio}
        log(0, f"Iniciando por {inicio}")
        if backtrack(caminho, visitados, 1):
            log(0, "✓ Solução encontrada")
            return caminho
        log(0, f"X Sem solução iniciando em {inicio}")
    log(0, "X Nenhum início levou a solução")
    return None
```
- **Laço externo**: tenta começar de cada vértice.  
- Retorna o primeiro caminho encontrado, ou `None` se não existir.

#### `main.py` (principais funções)

- `perguntar_verbose()`: pergunta **(s/n)** se quer o passo a passo.  
- `imprimir_resultado(...)`: mostra tipo do grafo, `n`, número de arestas lógicas, roda `caminho_hamiltoniano(...)` e imprime o resultado.  
- `exemplo_nao_dirigido()` e `exemplo_dirigido()`: constroem pequenos grafos de exemplo.  
- `grafo_personalizado()`: permite informar `n`, se é dirigido, `m` e as `m` arestas (`u v`).  
- `menu()`: loop de opções (1 — não dirigido, 2 — dirigido, 3 — personalizado, 0 — sair).

---

## Como executar o projeto

**Pré-requisitos**  
- Python **3.10+**  
- Sem bibliotecas externas.

**Passos**
```bash
# Na pasta do projeto:
python main.py
```

**Menu**
```
==============================================
            Caminho Hamiltoniano 
==============================================
[1] Rodar exemplo Não dirigido 
[2] Rodar exemplo DIRIGIDO
[3] Criar e rodar Grafo Personalizado
[0] Sair
```

- Em cada opção, você pode escolher **Mostrar passo a passo? (s/n)**.
- No **personalizado**, informe `n`, se é dirigido, `m` e as arestas `u v` (uma por linha).

**Exemplo rápido (personalizado)**
```
Quantidade de vértices (0..n-1): 5
Grafo dirigido? (s/n): n
Quantidade de arestas: 6
Aresta 1: 0 1
Aresta 2: 1 2
Aresta 3: 2 3
Aresta 4: 3 4
Aresta 5: 0 2
Aresta 6: 1 3
Mostrar passo a passo? (s/n): s
```
## Relatório técnico

### 3.1 Classes de complexidade: P, NP, NP-Completo, NP-Difícil

- **P**: problemas decidíveis em tempo polinomial por um algoritmo determinístico.  
- **NP**: problemas cujas soluções podem ser **verificadas** em tempo polinomial.  
- **NP-Completo**: problemas em NP para os quais **todo** problema em NP reduz-se polinomialmente a eles (são os “mais difíceis” dentro de NP).  
- **NP-Difícil**: pelo menos tão difíceis quanto os NP-completos; **não precisam** estar em NP (podem nem ser decidíveis em tempo polinomial de verificação).

**Caminho Hamiltoniano (decisão: “existe um caminho que visita todos os vértices exatamente uma vez?”)**  
- Está em **NP**: dado um caminho candidato, verificamos em tempo polinomial se é válido.  
- É **NP-completo** tanto em **grafos não dirigidos** quanto em **dirigidos** (reduções clássicas a partir de problemas NP-completos como Hamiltonian Cycle, 3-SAT, etc.).

**Relação com o TSP (Problema do Caixeiro Viajante)**  
- O TSP (decisão) pergunta se existe um ciclo que visita cada cidade uma vez com custo ≤ B; é **NP-completo**.  
- **Hamiltoniano** pode ser reduzido ao **TSP**: atribui-se peso 1 às arestas do grafo e peso 2 às que não existem; existe ciclo/caminho hamiltoniano ⇔ existe tour de custo `n` (ou caminho ajustando o modelo).

### 3.2 Complexidade temporal do algoritmo

**Algoritmo implementado**: backtracking que tenta estender um caminho, marcando visitados, e recuando quando necessário.

- **Pior caso**: precisa explorar essencialmente **permutações** dos vértices.  
  - No nível 1 há até `n` escolhas de início; no nível 2, até `n-1` escolhas, e assim por diante.  
  - Ordem de grandeza: **O(n!)** (fatorial), desconsiderando pequenos fatores de poda por adjacência.
- **Como foi determinado**:  
  - **Contagem do tamanho da árvore de busca** (número de sequências possíveis de vértices sem repetição) → aproximação por `n!`.  
  - Recorrência qualitativa `T(n) ≈ (n-1)T(n-1)` (não resolvida por Teorema Mestre).

> Observação: podas por ausência de aresta reduzem o espaço explorado em muitos grafos, mas a **classe assintótica** de pior caso permanece **exponencial**.

### 3.3 Teorema Mestre — aplicabilidade

O **Teorema Mestre** trata recorrências do tipo:
```
T(n) = a·T(n/b) + f(n)
```
com divisão “regular” do problema em subproblemas de **tamanho fracionário** `n/b` (padrão **dividir-para-conquistar**).

- Nosso backtracking **não** se encaixa nesta forma: não dividimos `n` em partes `n/b`. Em vez disso, exploramos uma **árvore de busca combinatória** cujo número de nós cresce ~**fatorialmente**.  
- **Conclusão**: **não aplicável** o Teorema Mestre a este algoritmo.

### 3.4 Casos: melhor, médio e pior

- **Melhor caso**: logo no primeiro início (ou nos primeiros), o algoritmo segue um encadeamento de arestas que **já** visita todos os `n` vértices sem ramificações.  
  - Custo próximo a **O(n + m)** para construir/percorrer uma única trilha e validar (linear no tamanho do grafo).
- **Caso médio**: depende fortemente da **densidade** e **estrutura** do grafo. Em geral, ainda **exponencial**, mas com muito menos nós explorados que o pior caso devido às **podas** (arestas faltantes, dead-ends precoces).  
- **Pior caso**: grafos que induzem grande número de tentativas antes de concluir inexistência (ou encontrar uma solução muito tarde).  
  - Ordem de grandeza: **O(n!)**.