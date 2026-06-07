# Global Solution 2026 - Economia Espacial - Dynamic Programming

## Monitoramento de Riscos Ambientais com Árvores, Grafos e Algoritmos - Enchentes RS

### Integrantes do Grupo

* Felipe Catto – RM 562106
* Kimberly Kristina – RM 564080
* Laura Dantas – RM 564064
* Raphael Aaron – RM 564067

---

# Descrição do Projeto

As enchentes ocorridas no Rio Grande do Sul em 2024 evidenciaram a importância de sistemas computacionais capazes de auxiliar na tomada de decisão durante situações de emergência.

Este projeto propõe a modelagem de uma rede de municípios afetados pelas enchentes utilizando estruturas de dados e algoritmos estudados na disciplina de Dynamic Programming.

O sistema utiliza:

* Árvore Binária de Busca (BST) para organização dos municípios por índice de risco;
* Grafos ponderados para representação das conexões entre municípios;
* Algoritmo Guloso (Dijkstra) para determinação de rotas de menor custo;
* Algoritmo de Força Bruta com Backtracking para comparação de desempenho;
* Ferramentas de monitoramento para análise de tempo de execução e consumo de memória.

---

# Objetivos

O projeto possui os seguintes objetivos:

* Organizar municípios por nível de risco utilizando BST;
* Modelar a malha de municípios através de grafos ponderados;
* Encontrar rotas ótimas para deslocamento de equipes de resgate;
* Comparar uma abordagem exaustiva (Força Bruta) com uma abordagem gulosa (Dijkstra);
* Avaliar desempenho computacional através de métricas experimentais.

---

# Estrutura do Projeto

```text
global-solution-2026-fund/
│
├── data/
│   ├── raw/
│   │   └── municipios_rs.py
│   │
│   └── processed/
│       └── grafo_rs.py
│
├── notebooks/
│   └── analise_resultados.ipynb
│
├── report/
│   ├── grafo_municipios.png
│   ├── tempo_x_n.png
│   └── gap_otimalidade.png
│
├── src/
│   ├── data_structures.py
│   ├── greedy.py
│   ├── brute_force.py
│   ├── graph_generator.py
│   ├── performance_monitor.py
│   └── visualizations.py
│
├── tests/
│   ├── test_algorithms.py
│   ├── teste_bst_completo.py
│   ├── teste_escal.py
│   ├── teste_visualizacao.py
│   └── comparacao_algoritmos.py
│
├── requirements.txt
└── README.md
```

---

# Tecnologias Utilizadas

* Python 3.14
* Matplotlib
* NetworkX
* Pandas
* Pytest
* Tracemalloc

---

# Estruturas de Dados Utilizadas

## Árvore Binária de Busca (BST)

A BST foi utilizada para armazenar os municípios de acordo com seu índice de risco.

Funcionalidades implementadas:

* Inserção
* Busca por intervalo de risco
* Percurso In-Order
* Remoção
* Cálculo de altura

---

## Grafos

Os municípios foram modelados como vértices de um grafo ponderado.

As arestas representam conexões entre municípios e os pesos representam o custo de deslocamento.

Exemplo:

```text
Porto Alegre ----- Novo Hamburgo ----- Caxias do Sul
```

---

# Algoritmos Implementados

## Algoritmo Guloso (Dijkstra)

Utilizado para encontrar o caminho de menor custo entre dois municípios.

Características:

* Complexidade aproximada: O((V + E) log V)
* Garante solução ótima para pesos positivos
* Excelente escalabilidade

---

## Algoritmo de Força Bruta

Implementado utilizando recursão e backtracking.

Características:

* Enumeração de todos os caminhos possíveis
* Garante solução ótima
* Alto custo computacional
* Crescimento exponencial

---

# Experimentos

Foram realizados testes comparando Dijkstra e Força Bruta.

## Tempo Médio de Execução

| N  | Dijkstra (ms) | Força Bruta (ms) |
| -- | ------------: | ---------------: |
| 5  |        0.0185 |           0.0673 |
| 8  |        0.0284 |           0.5949 |
| 10 |        0.0362 |           3.7801 |
| 12 |        0.0481 |          24.2847 |

Observa-se que o algoritmo de Força Bruta apresenta crescimento exponencial, enquanto o algoritmo de Dijkstra mantém desempenho estável mesmo com o aumento da quantidade de vértices.

---

# Resultados Obtidos

## Melhor Caminho Encontrado

Origem:

```text
Porto Alegre
```

Destino:

```text
Caxias do Sul
```

Caminho ótimo:

```text
Porto Alegre
→ Novo Hamburgo
→ Caxias do Sul
```

Custo total:

```text
2.4
```

Tanto o algoritmo de Força Bruta quanto o algoritmo de Dijkstra encontraram a mesma solução ótima.

---

# Visualizações

O projeto gera automaticamente:

* Grafo dos municípios;
* Gráfico Tempo × Número de Vértices;
* Gráfico Gap de Otimalidade;
* Comparações de desempenho.

As imagens são armazenadas na pasta:

```text
report/
```

---

# Como Executar

## 1. Clonar o repositório

```bash
git clone https://github.com/KimKristy/global-solution-2026-fund.git
```

## 2. Acessar a pasta

```bash
cd global-solution-2026-fund
```

## 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## 4. Executar testes

```bash
python tests/teste_bst_completo.py

python tests/teste_visualizacao.py

python tests/teste_escal.py

python tests/comparacao_algoritmos.py
```

---

# Conclusão

Os resultados demonstram que o algoritmo de Dijkstra é significativamente mais eficiente do que a abordagem de Força Bruta para o problema de roteamento entre municípios afetados por enchentes.

Embora ambos os métodos encontrem a solução ótima, a abordagem gulosa apresenta melhor escalabilidade, tornando-se mais adequada para aplicações reais de resposta a desastres naturais.

---

# Referências

CORMEN, T. H. et al. Introduction to Algorithms. MIT Press.

GOODRICH, Michael T.; TAMASSIA, Roberto. Estruturas de Dados e Algoritmos em Java.

Documentação Oficial Python:
https://docs.python.org/

NetworkX Documentation:
https://networkx.org/

Matplotlib Documentation:
https://matplotlib.org/
