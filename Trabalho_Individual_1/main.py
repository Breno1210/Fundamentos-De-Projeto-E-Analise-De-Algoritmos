from time import perf_counter
from app import karatsuba  

def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            valor = input(mensagem).strip()
            valor = valor.replace("_", "").replace(" ", "")
            return int(valor)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

def multiplicar_manual():
    print("\n== Modo manual ==")
    numero1 = ler_inteiro("Digite o primeiro número: ")
    numero2 = ler_inteiro("Digite o segundo número: ")

    inicio = perf_counter()
    resultado = karatsuba(numero1, numero2)
    duracao_ms = (perf_counter() - inicio) * 1000

    print(f"\nResultado (Karatsuba): {resultado}")
    print(f"Verificação (a*b)   : {numero1 * numero2}")
    print(f"Tempo: {duracao_ms:.3f} ms\n")

def rodar_testes():
    casos = [
        (12, 34),
        (123, 456),
        (1234, 5678),
        (9999, 9999),
        (123456789, 987654321),
        (12345678901234567890, 98765432109876543210),
        (-987654321, -123456789),
    ]

    print("\n== Testes prontos ==")
    total_passou = 0

    for indice, (a, b) in enumerate(casos, start=1):
        inicio = perf_counter()
        resultado = karatsuba(a, b)
        duracao_ms = (perf_counter() - inicio) * 1000
        esperado = a * b

        passou = resultado == esperado
        status = "✅ Passou" if passou else "❌ Falhou"

        if passou:
            total_passou += 1

        print(f"[{indice:02d}] {a} * {b}")
        print(f"     -> Resultado: {resultado}")
        print(f"     -> Esperado : {esperado}")
        print(f"     -> {status} | {duracao_ms:.3f} ms\n")

    print(f"Resumo: {total_passou}/{len(casos)} passaram.\n")

def menu():
    while True:
        print("==========================================")
        print("   Algoritmo de Karatsuba - Menu")
        print("==========================================")
        print("[1] Multiplicar manualmente")
        print("[2] Rodar testes prontos (com detalhes)")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            multiplicar_manual()
        elif opcao == "2":
            rodar_testes()
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()
