# Global Solution 2026 - Economia Espacial - Dynamic Programming

## Monitoramento de Riscos Ambientais com Árvores, Grafos e Algoritmos

### Integrantes do Grupo

* Felipe Catto – RM 562106
* Kimberly Kristina – RM 564080
* Laura Dantas – RM 564064
* Raphael Aaron – RM 564067

---

# Descrição do Projeto

Este projeto foi desenvolvido para a Global Solution 2026 com o objetivo de aplicar estruturas de dados e algoritmos estudados na disciplina de Dynamic Programming em cenários de monitoramento de riscos ambientais.

O sistema foi instanciado em dois cenários distintos:

### Cenário 1 – Enchentes no Rio Grande do Sul

Baseado nos impactos causados pelas enchentes ocorridas no estado do Rio Grande do Sul, modelando municípios afetados e suas conexões logísticas.

### Cenário 2 – Seca na Região MATOPIBA

Representando municípios da região MATOPIBA (Maranhão, Tocantins, Piauí e Bahia), área frequentemente afetada por períodos de estiagem e estresse hídrico.

Como não foram disponibilizadas bases oficiais padronizadas para os experimentos da atividade, foram utilizados dados sintéticos construídos com valores plausíveis para fins acadêmicos, preservando as características dos cenários analisados.

---

# Objetivos

* Organizar municípios por nível de risco utilizando Árvore Binária de Busca (BST);
* Modelar redes de municípios através de grafos ponderados;
* Encontrar rotas ótimas para deslocamento entre localidades;
* Comparar uma abordagem gulosa (Dijkstra) com uma abordagem exaustiva (Força Bruta);
* Avaliar desempenho computacional através de métricas experimentais;
* Apoiar processos de tomada de decisão em cenários de desastres naturais.

---

# Estruturas de Dados Utilizadas

## Árvore Binária de Busca (BST)

A BST foi utilizada para organizar os municípios de acordo com seus índices de risco.

Funcionalidades implementadas:

* Inserção;
* Busca por intervalo de risco;
* Percurso In-Order;
* Remoção;
* Cálculo de altura.

---

## Grafos Ponderados

Os municípios foram modelados como vértices de um grafo ponderado.

As arestas representam conexões entre municípios e os pesos representam custos de deslocamento entre localidades.

Essa estrutura permite representar cenários reais de logística e distribuição de recursos em situações emergenciais.

---

# Algoritmos Implementados

## Algoritmo Guloso (Dijkstra)

Utilizado para encontrar o caminho de menor custo entre dois municípios.

Características:

* Complexidade aproximada: O((V + E) log V);
* Garante solução ótima para pesos positivos;
* Excelente escalabilidade;
* Adequado para redes de grande porte.

---

## Algoritmo de Força Bruta

Implementado utilizando recursão e backtracking.

Características:

* Enumeração de todos os caminhos possíveis;
* Garante solução ótima;
* Crescimento exponencial;
* Aplicável apenas em instâncias pequenas.

---

# Estrutura do Projeto

```text
global-solution-2026-fund/
│
├── data/
│   ├── raw/
│   │   ├── municipios_rs.py
│   │   └── municipios_matopiba.py
│   │
│   └── processed/
│       ├── grafo_rs.py
│       └── grafo_matopiba.py
│
├── notebooks/
│   └── analise_resultados.ipynb
│
├── report/
│   ├── bst_matopiba.png
│   ├── bst_municipios.png
│   ├── grafo_municipios.png
│   ├── grafo_matopiba.png
│   ├── tempo_x_n.png
│   ├── gap_otimalidade.png
│   ├── caminhos_x_n.png
│   ├── recursao_x_n.png
│   └── relatorio_final.pdf
│
├── src/
│   ├── brute_force.py
│   ├── data_structures.py
│   ├── graph_generator.py
│   ├── greedy.py
│   ├── performance_monitor.py
│   └── visualizations.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Experimentos Realizados

Foram realizados experimentos para comparar os algoritmos Dijkstra e Força Bruta.

## Tempo Médio de Execução

| N  | Dijkstra (ms) | Força Bruta (ms) |
| -- | ------------- | ---------------- |
| 5  | 0.0185        | 0.0673           |
| 8  | 0.0284        | 0.5949           |
| 10 | 0.0362        | 3.7801           |
| 12 | 0.0481        | 24.2847          |

Os resultados demonstram crescimento controlado para o algoritmo de Dijkstra e crescimento exponencial para a abordagem de Força Bruta.

---

# Resultados Obtidos

## Cenário Rio Grande do Sul

Origem: Porto Alegre

Destino: Caxias do Sul

Melhor caminho encontrado:

Porto Alegre → Novo Hamburgo → Caxias do Sul

Custo total: 2.4

---

## Cenário MATOPIBA

Origem: Balsas

Destino: São Desidério

Melhor caminho encontrado:

Balsas → Uruçuí → Luís Eduardo Magalhães → São Desidério

Custo total: 4.1

---

# Escala de Decisão

| Situação              | Recomendação            |
| --------------------- | ----------------------- |
| Redes pequenas        | Força Bruta ou Dijkstra |
| Redes médias          | Dijkstra                |
| Redes grandes         | Dijkstra                |
| Validação de soluções | Força Bruta             |
| Aplicações reais      | Dijkstra                |

---

# Visualizações Geradas

O projeto gera automaticamente:

* BST dos municípios por índice de risco;
* Grafo do cenário Rio Grande do Sul;
* Grafo do cenário MATOPIBA;
* Gráfico Tempo × Número de Vértices;
* Gráfico Gap de Otimalidade.

Todos os arquivos são armazenados na pasta:

```text
report/
```

---

# Tecnologias Utilizadas

* Python 3.14
* Pandas
* Matplotlib
* NetworkX
* Pytest
* Tracemalloc

---

# Como Executar

## Clonar o repositório

```bash
git clone https://github.com/KimKristy/global-solution-2026-fund.git
```

## Entrar na pasta

```bash
cd global-solution-2026-fund
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar testes

```bash
python -m tests.teste_bst_completo
python -m tests.teste_visualizacao
python -m tests.teste_escal
python -m tests.comparacao_algoritmos
python -m tests.teste_matopiba
```

---

# Conclusão

O projeto demonstrou a aplicação prática de Árvores Binárias de Busca, Grafos Ponderados e algoritmos de otimização em cenários de desastres ambientais.

Os resultados evidenciaram que o algoritmo de Dijkstra apresenta desempenho significativamente superior à abordagem de Força Bruta, mantendo a qualidade das soluções encontradas.

A aplicação em dois cenários distintos — enchentes no Rio Grande do Sul e seca na região MATOPIBA — demonstrou a flexibilidade da solução proposta e sua capacidade de apoiar processos de tomada de decisão em diferentes contextos de risco ambiental.

---

# Referências

CORMEN, T. H. et al. Introduction to Algorithms. MIT Press.

GOODRICH, Michael T.; TAMASSIA, Roberto. Estruturas de Dados e Algoritmos.

Python Software Foundation. Python Documentation.

https://docs.python.org/

NetworkX Documentation.

https://networkx.org/

Matplotlib Documentation.

https://matplotlib.org/