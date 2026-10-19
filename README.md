# Algoritmo de Kruskal: Rede de Fibra Ótica entre Laboratórios

Trabalho de seminário sobre o **Algoritmo de Kruskal** (Teoria dos Grafos).
O projeto implementa o algoritmo em Python e o aplica a um problema de infraestrutura de rede.

## O problema

A universidade precisa conectar cinco laboratórios de computação (A, B, C, D e E)
com cabos de fibra ótica. O objetivo é conectar todos os laboratórios gastando o
**mínimo de metros de cabo**.

**Modelagem:** grafo não direcionado e ponderado G = (V, E, w), em que

- **V** = {A, B, C, D, E} (laboratórios);
- **E** = rotas possíveis entre prédios;
- **w(e)** = metros de cabo da rota.

Buscamos a **Árvore Geradora Mínima (MST)** de G.

| Rota | Metros |
|------|-------:|
| D–E  | 5  |
| A–B  | 10 |
| B–C  | 15 |
| A–C  | 20 |
| C–D  | 30 |
| C–E  | 40 |
| B–D  | 50 |

## Estrutura do projeto

```
.
├── kruskal.py        # UnionFind e algoritmo de Kruskal
├── main.py           # Executa o algoritmo no problema dos laboratórios
├── test_kruskal.py   # Testes automatizados
└── README.md
```

## Requisitos

- Python **3.9 ou superior** (usa `tuple[...]` e `list[...]` nas anotações de tipo)
- **Nenhuma dependência externa** (apenas a biblioteca padrão)

## Como executar

```bash
# Clonar o repositório
git clone <URL_DO_REPOSITORIO>
cd kruskal-fibra-otica

# Executar o algoritmo sobre o problema
python main.py

# Executar os testes
python -m unittest -v
```

## Saída esperada

```
=== PASSO A PASSO ===
D-E ( 5 m): ACEITA    | custo acumulado: 5 m
A-B (10 m): ACEITA    | custo acumulado: 15 m
B-C (15 m): ACEITA    | custo acumulado: 30 m
A-C (20 m): REJEITADA | custo acumulado: 30 m
C-D (30 m): ACEITA    | custo acumulado: 60 m

=== PROJETO DE REDE DE FIBRA ÓTICA (KRUSKAL) ===
Rotas aprovadas para instalação:
 -> Ligar laboratório D ao E (5 metros)
 -> Ligar laboratório A ao B (10 metros)
 -> Ligar laboratório B ao C (15 metros)
 -> Ligar laboratório C ao D (30 metros)

Gasto total mínimo: 60 metros de cabo.
```

A rota **A–C (20 m)** é rejeitada porque A e C já estão conectados via B, e
aceitá-la formaria o ciclo A–B–C.

## Como o algoritmo funciona

1. Ordene as arestas por peso crescente.
2. Para cada aresta (u, v), em ordem:
   - se u e v estão em componentes diferentes, **aceite** a aresta e una os componentes;
   - caso contrário, **rejeite** (formaria ciclo).
3. Pare ao atingir |V| − 1 arestas.

A verificação de ciclos usa a estrutura **Union-Find** com duas otimizações:

- **Compressão de caminho** (implementação iterativa, sem risco de estouro de pilha);
- **União por rank**.

## Complexidade

- Ordenação das arestas: **O(E log E)**
- Operações Union-Find: **O(E · α(V))**, em que α é a inversa da função de Ackermann (praticamente constante)
- **Total: O(E log E)**

## Decisões de implementação

- `sorted()` em vez de `list.sort()`: a lista de arestas do chamador **não é modificada**.
- `UnionFind.unir()` retorna `bool`, unindo a detecção de ciclo e a união em uma só operação.
- Grafos desconexos lançam `ValueError`, pois não existe árvore geradora.
- O parâmetro opcional `passos` registra cada decisão do algoritmo, usado para gerar o passo a passo.

## Autores

- Thiago mattos 
- Valentim aragão
- Igor brasil
