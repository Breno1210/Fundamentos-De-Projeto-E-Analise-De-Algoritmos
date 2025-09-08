from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class Result:
    min_value: float
    max_value: float
    comparisons: int  # total de comparações realizadas


def _maxmin_rec(arr: List[float], lo: int, hi: int) -> Result:
    n = hi - lo
    if n == 1:
        # um único elemento: min = max = arr[lo]; 0 comparações
        v = arr[lo]
        return Result(v, v, 0)
    if n == 2:
        # dois elementos: 1 comparação
        a, b = arr[lo], arr[lo + 1]
        if a <= b:
            return Result(a, b, 1)
        else:
            return Result(b, a, 1)

    mid = lo + n // 2
    L = _maxmin_rec(arr, lo, mid)
    R = _maxmin_rec(arr, mid, hi)

    # combinar com 2 comparações
    comparisons = L.comparisons + R.comparisons
    if L.min_value <= R.min_value:
        mn = L.min_value
        comparisons += 1
    else:
        mn = R.min_value
        comparisons += 1

    if L.max_value >= R.max_value:
        mx = L.max_value
        comparisons += 1
    else:
        mx = R.max_value
        comparisons += 1

    return Result(mn, mx, comparisons)


def maxmin_divide_conquer(numbers: Iterable[float]) -> Result:
    """
    Retorna (min, max, comparacoes) usando Divisão & Conquista.
    Levanta ValueError se a sequência estiver vazia.
    """
    arr = list(numbers)
    if not arr:
        raise ValueError("Sequência vazia: não é possível obter min e max.")
    return _maxmin_rec(arr, 0, len(arr))


def maxmin_naive(numbers: Iterable[float]) -> Result:
    """
    Baseline O(n) com 2(n-1) comparações: encontra min e max varrendo uma vez.
    """
    it = iter(numbers)
    try:
        first = next(it)
    except StopIteration:
        raise ValueError("Sequência vazia: não é possível obter min e max.")
    mn = mx = first
    comps = 0
    for v in it:
        comps += 1
        if v < mn:
            mn = v
        else:
            comps += 1
            if v > mx:
                mx = v
    return Result(mn, mx, comps)
