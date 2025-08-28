def karatsuba(numero1: int, numero2: int) -> int:
    """
    Multiplica dois inteiros (podem ser grandes ou negativos) usando Karatsuba.
    """
    if numero1 == 0 or numero2 == 0:
        return 0

    sinal = -1 if (numero1 < 0) ^ (numero2 < 0) else 1

    return sinal * _karatsuba_abs(abs(numero1), abs(numero2))


def _karatsuba_abs(numero1: int, numero2: int) -> int:
    """
    Versão interna de Karatsuba assumindo numero1 >= 0 e numero2 >= 0.
    """
    if numero1 < 10 or numero2 < 10:
        return numero1 * numero2

    num_digitos = max(len(str(numero1)), len(str(numero2)))
    metade = num_digitos // 2

    parte_alta1, parte_baixa1 = divmod(numero1, 10 ** metade)
    parte_alta2, parte_baixa2 = divmod(numero2, 10 ** metade)

    produto_baixas = _karatsuba_abs(parte_baixa1, parte_baixa2)
    produto_altas = _karatsuba_abs(parte_alta1, parte_alta2)
    produto_cruzado = _karatsuba_abs(parte_baixa1 + parte_alta1,
                                     parte_baixa2 + parte_alta2)

    return (produto_altas * 10 ** (2 * metade)) + \
           ((produto_cruzado - produto_altas - produto_baixas) * 10 ** metade) + \
           produto_baixas
