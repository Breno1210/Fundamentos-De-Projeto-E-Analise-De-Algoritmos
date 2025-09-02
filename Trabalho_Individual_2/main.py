from __future__ import annotations
import argparse
from pathlib import Path
from typing import List
from maxmin import maxmin_divide_conquer, maxmin_naive


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="MaxMin Select (Divide & Conquer)")
    p.add_argument("numbers", nargs="*", type=float, help="Números da sequência")
    p.add_argument("--file", type=Path, help="Arquivo contendo números (separados por espaço/linhas)")
    p.add_argument("--random", type=int, metavar="N", help="Gerar N números aleatórios uniformes em [-1e3,1e3]")
    p.add_argument("--seed", type=int, default=123, help="Seed p/ gerador aleatório (quando usar --random)")
    p.add_argument("--baseline", action="store_true", help="Também calcular baseline ingênuo para comparar comparações")
    return p.parse_args()


def load_numbers(args: argparse.Namespace) -> List[float]:
    if args.file:
        txt = args.file.read_text(encoding="utf-8")
        return [float(tok) for tok in txt.replace("\n", " ").split() if tok.strip()]
    if args.random is not None:
        import random
        random.seed(args.seed)
        return [random.uniform(-1e3, 1e3) for _ in range(args.random)]
    if args.numbers:
        return list(args.numbers)
    raise SystemExit("Forneça números, --file ou --random N")


def main() -> None:
    args = parse_args()
    arr = load_numbers(args)

    res = maxmin_divide_conquer(arr)
    print("Entrada:", arr)
    print(f"Min, Max: ({res.min_value}, {res.max_value})")
    print("Comparações:", res.comparisons)

    if args.baseline:
        base = maxmin_naive(arr)
        print("\n[Baseline Ingênuo]")
        print(f"Min, Max: ({base.min_value}, {base.max_value})")
        print("Comparações:", base.comparisons)


if __name__ == "__main__":
    main()
