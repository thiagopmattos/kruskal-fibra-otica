"""Executa o algoritmo de Kruskal no problema da rede de fibra ótica."""

from kruskal import kruskal

# Os 5 laboratórios (vértices)
LABORATORIOS = ["A", "B", "C", "D", "E"]

# Rotas possíveis (laboratório 1, laboratório 2, metros de cabo)
ROTAS = [
    ("D", "E", 5),
    ("A", "B", 10),
    ("B", "C", 15),
    ("A", "C", 20),
    ("C", "D", 30),
    ("C", "E", 40),
    ("B", "D", 50),
]


def main() -> None:
    passos: list = []
    rotas_escolhidas, total = kruskal(LABORATORIOS, ROTAS, passos)

    print("=== PASSO A PASSO ===")
    for (u, v, peso), aceita, acumulado in passos:
        status = "ACEITA   " if aceita else "REJEITADA"
        print(f"{u}-{v} ({peso:>2} m): {status} | custo acumulado: {acumulado} m")

    print("\n=== PROJETO DE REDE DE FIBRA ÓTICA (KRUSKAL) ===")
    print("Rotas aprovadas para instalação:")
    for u, v, peso in rotas_escolhidas:
        print(f" -> Ligar laboratório {u} ao {v} ({peso} metros)")
    print(f"\nGasto total mínimo: {total} metros de cabo.")


if __name__ == "__main__":
    main()
