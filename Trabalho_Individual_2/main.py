from __future__ import annotations
from time import perf_counter
from math import ceil
from typing import List
from maxmin import maxmin_divide_conquer, maxmin_naive


# ---------------------------
# Utilidades de leitura
# ---------------------------
def ler_inteiro(mensagem: str, minimo: int | None = None) -> int:
    while True:
        try:
            valor = input(mensagem).strip()
            valor = valor.replace("_", "").replace(" ", "")
            n = int(valor)
            if minimo is not None and n < minimo:
                print(f"Digite um inteiro ≥ {minimo}.")
                continue
            return n
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_floats(mensagem: str) -> List[float]:
    """
    Lê uma linha com números (separados por espaço e/ou vírgula) e retorna uma lista de floats.
    Ex.: 10, 2.5 -3  7 -> [10.0, 2.5, -3.0, 7.0]
    """
    while True:
        txt = input(mensagem).strip()
        if not txt:
            print("Digite ao menos um número.")
            continue
        txt = txt.replace(",", " ")
        partes = [p for p in txt.split() if p]
        try:
            return [float(p) for p in partes]
        except ValueError:
            print("Entrada inválida. Digite números separados por espaço/vírgula.")


# ---------------------------
# Impressão de resultados
# ---------------------------
def bound_maxmin(n: int) -> int:
    """Limite teórico de comparações: ceil(3n/2) - 2."""
    return int(ceil(3 * n / 2) - 2)


def imprimir_resultado(arr: List[float], comparar_baseline: bool = False) -> None:
    if not arr:
        print("Sequência vazia não é permitida.\n")
        return

    print("\nEntrada:", arr)
    n = len(arr)
    print(f"Tamanho (n): {n} | Limite teórico ≤ ceil(3n/2) - 2 = {bound_maxmin(n)}")

    t0 = perf_counter()
    res = maxmin_divide_conquer(arr)
    dt_ms = (perf_counter() - t0) * 1000

    print(f"\n[Divisão e Conquista]")
    print(f"Min, Max: ({res.min_value}, {res.max_value})")
    print(f"Comparações: {res.comparisons}  | Tempo: {dt_ms:.3f} ms")

    if comparar_baseline:
        t0b = perf_counter()
        base = maxmin_naive(arr)
        dt_ms_b = (perf_counter() - t0b) * 1000

        print(f"\n[Baseline Ingênuo]")
        print(f"Min, Max: ({base.min_value}, {base.max_value})")
        print(f"Comparações: {base.comparisons}  | Tempo: {dt_ms_b:.3f} ms")

        dif = base.comparisons - res.comparisons
        sinal = "+" if dif > 0 else ""
        print(f"\nComparativo (Ingênuo - D&C): {sinal}{dif} comparações")


# ---------------------------
# Modos do menu
# ---------------------------
def modo_manual(comparar_baseline: bool = False) -> None:
    print("\n== Modo manual ==")
    arr = ler_floats("Digite os números (separados por espaço/vírgula): ")
    imprimir_resultado(arr, comparar_baseline=comparar_baseline)
    print()


def modo_aleatorio(comparar_baseline: bool = False) -> None:
    print("\n== Gerar aleatórios ==")
    n = ler_inteiro("Quantidade de números (n ≥ 1): ", minimo=1)
    seed = input("Seed (opcional, Enter para padrão 123): ").strip()
    seed = int(seed) if seed else 123
    import random
    random.seed(seed)
    arr = [random.randint(-1000, 1000) for _ in range(n)]  # 🔹 agora inteiros
    imprimir_resultado(arr, comparar_baseline=comparar_baseline)
    print()


def rodar_testes_prontos(comparar_baseline: bool = False) -> None:
    print("\n== Testes prontos ==")
    casos = [
        [7],
        [2, 2],
        [-5, 0, 12, 12, -5, 3],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [10, -1, 5, 7, -10, 20, 0],
        [5, 3, 9, -2, 9, 10, 10, 4],
        [10, 10, 10, -1, 2],
    ]
    total = len(casos)
    passou = 0
    for i, arr in enumerate(casos, start=1):
        print(f"\n--- Caso {i:02d} ---")
        imprimir_resultado(arr, comparar_baseline=comparar_baseline)
        mn, mx = min(arr), max(arr)
        res = maxmin_divide_conquer(arr)
        if (res.min_value, res.max_value) == (mn, mx):
            passou += 1
    print(f"\nResumo: {passou}/{total} corretos (comparando com min/max do Python).\n")


# ---------------------------
# Menu
# ---------------------------
def menu() -> None:
    while True:
        print("==============================================")
        print("  MaxMin Select (Divisão & Conquista) - Menu")
        print("==============================================")
        print("[1] Rodar manualmente (D&C)")
        print("[2] Rodar manualmente (D&C) + comparar com baseline")
        print("[3] Gerar aleatórios (D&C)")
        print("[4] Gerar aleatórios (D&C) + comparar com baseline")
        print("[5] Rodar testes prontos (D&C)")
        print("[6] Rodar testes prontos (D&C) + baseline")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            modo_manual(False)
        elif opcao == "2":
            modo_manual(True)
        elif opcao == "3":
            modo_aleatorio(False)
        elif opcao == "4":
            modo_aleatorio(True)
        elif opcao == "5":
            rodar_testes_prontos(False)
        elif opcao == "6":
            rodar_testes_prontos(True)
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
