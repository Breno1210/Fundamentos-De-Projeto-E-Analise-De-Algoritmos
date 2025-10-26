# main.py
from hamiltonian import montar_adjacencia, caminho_hamiltoniano


def perguntar_verbose() -> bool:
    resp = input("Mostrar passo a passo? (s/n): ").strip().lower()
    return resp == "s"


def imprimir_resultado(adj, dirigido: bool, verbose: bool):
    n = len(adj)
    m = sum(len(v) for v in adj.values())
    m_logico = m if dirigido else m // 2

    print("\n===== Detalhes do Grafo =====")
    print(f"Tipo: {'Dirigido' if dirigido else 'Não dirigido'}")
    print(f"Vértices (n): {n}")
    print(f"Arestas (m): {m_logico}")
    print("=============================\n")

    caminho = caminho_hamiltoniano(adj, verbose=verbose)

    if caminho is None:
        print("\nResultado: Não existe caminho hamiltoniano para este grafo.")
    else:
        trilha = " -> ".join(map(str, caminho))
        print("\nResultado: Caminho Hamiltoniano encontrado!")
        print(trilha)
        print(f"Tamanho do caminho: {len(caminho)} (esperado {n})")


def exemplo_nao_dirigido():
    n = 5
    arestas = [
        (0, 1), (1, 2), (2, 3), (3, 4),
        (0, 2), (1, 3)
    ]
    dirigido = False
    adj = montar_adjacencia(n, arestas, dirigido)
    verbose = perguntar_verbose()
    imprimir_resultado(adj, dirigido, verbose)


def exemplo_dirigido():
    n = 5
    arestas = [
        (0, 1), (1, 2), (3, 4),
        (0, 2), (1, 3)
    ]
    dirigido = True
    adj = montar_adjacencia(n, arestas, dirigido)
    verbose = perguntar_verbose()
    imprimir_resultado(adj, dirigido, verbose)

def grafo_personalizado():
    # Entrada guiada e simples
    try:
        n = int(input("Quantidade de vértices (0..n-1): ").strip())
        if n <= 0:
            print("n deve ser positivo.")
            return

        tipo = input("Grafo dirigido? (s/n): ").strip().lower()
        dirigido = tipo == "s"

        m = int(input("Quantidade de arestas: ").strip())
        if m < 0:
            print("m não pode ser negativo.")
            return

        print("Informe as arestas uma por linha no formato: u v")
        print("Ex.: 0 1  (significa u->v; no não-dirigido vira u<->v)")
        arestas = []
        for i in range(m):
            while True:
                linha = input(f"Aresta {i+1}: ").strip()
                if not linha:
                    print("Entrada vazia, tente novamente.")
                    continue
                try:
                    u_str, v_str = linha.split()
                    u, v = int(u_str), int(v_str)
                    if not (0 <= u < n and 0 <= v < n):
                        print(f"Vértices devem estar entre 0 e {n-1}.")
                        continue
                    arestas.append((u, v))
                    break
                except ValueError:
                    print("Formato inválido. Use: u v (ex.: 0 1)")

        adj = montar_adjacencia(n, arestas, dirigido)
        verbose = perguntar_verbose()
        imprimir_resultado(adj, dirigido, verbose)

    except ValueError:
        print("Entrada inválida. Tente novamente.")

def menu():
    while True:
        print("==============================================")
        print("            Caminho Hamiltoniano ")
        print("==============================================")
        print("[1] Executar exemplo Não dirigido")
        print("[2] Executar exemplo Dirigido")
        print("[3] Criar e rodar Grafo Personalizado")
        print("[0] Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            exemplo_nao_dirigido()
        elif op == "2":
            exemplo_dirigido()
        elif op == "3":
            grafo_personalizado()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
