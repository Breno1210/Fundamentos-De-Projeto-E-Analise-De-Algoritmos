# hamiltonian.py
from typing import Dict, List, Optional

Grafo = Dict[int, List[int]]


def montar_adjacencia(n: int, arestas: List[tuple[int, int]], dirigido: bool) -> Grafo:
    """
    Constrói a lista de adjacência para um grafo com vértices [0..n-1].
    Se 'dirigido' for False, adiciona arestas em ambos os sentidos.
    """
    adj: Grafo = {v: [] for v in range(n)}
    for u, v in arestas:
        if 0 <= u < n and 0 <= v < n:
            adj[u].append(v)
            if not dirigido and u != v:
                adj[v].append(u)

    # remove duplicatas e deixa execução determinística
    for v in adj:
        vistos = set()
        ordenados = []
        for w in adj[v]:
            if w not in vistos:
                vistos.add(w)
                ordenados.append(w)
        adj[v] = ordenados
    return adj


def caminho_hamiltoniano(adj: Grafo, verbose: bool = False) -> Optional[List[int]]:
    """
    Tenta encontrar UM caminho hamiltoniano (visita todos os vértices uma vez).
    Retorna a lista de vértices na ordem do caminho, ou None se não existir.

    Se verbose=True, imprime o passo a passo do backtracking.
    """
    n = len(adj)
    vertices = list(adj.keys())
    step = [0]  # contador simples de passos para log

    def log(depth: int, msg: str) -> None:
        if not verbose:
            return
        step[0] += 1
        indent = "  " * depth
        print(f"[{step[0]:04d}] {indent}{msg}")

    def backtrack(caminho: List[int], visitados: set[int], depth: int) -> bool:
        if len(caminho) == n:
            log(depth, f"✓ Caminho completo: {caminho}")
            return True

        ultimo = caminho[-1]
        candidatos = adj.get(ultimo, [])
        log(depth, f"Na posição {len(caminho)-1}, último={ultimo}, candidatos={candidatos}")

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

            # desfaz
            caminho.pop()
            visitados.remove(viz)
            log(depth + 1, f"Backtrack de {viz}; caminho={caminho}")

        log(depth, f"Sem opções válidas a partir de {ultimo}")
        return False

    # tenta iniciar por cada vértice
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
