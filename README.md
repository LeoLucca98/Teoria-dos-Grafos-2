# Navegação com Grafo de Visibilidade e Árvore (Prim)

Projeto da disciplina para explorar árvores em um cenário de navegação de robô, seguindo o enunciado: leitura de mapa (texto/imagem), grafo de visibilidade, MST (Prim), vértice mais próximo visível, busca em árvore e plot do caminho.

Este repositório já contém a implementação funcional em Python das etapas principais; abaixo estão as instruções de uso, o formato do mapa e como reproduzir os resultados no Windows (PowerShell).

## Visão geral das etapas (mapeadas ao código)

- Arquivo de mapa (texto) e imagem do mapa:
  - Texto: `data/map_autoral_prof.txt` (pronto).
  - Imagem: adicionar uma imagem ilustrativa do mapa (ex.: `data/map_autoral_prof.png`).
- Leitura do mapa e grafo de visibilidade: `src/map_io.py` e `src/visibility.py`.
- MST (Prim) no grafo de visibilidade: `src/mst.py`.
- Função verticeMaisProximo: `src/nearest.py`.
- Busca na árvore (caminho s→t): `src/search.py`.
- Plot do mapa, grafo e caminho: `src/plot.py` e fluxo em `src/main.py`.

## Requisitos

- Python 3.10+ (recomendado)
- Bibliotecas Python:
  - `matplotlib` (para visualização)
  
Você pode instalar manualmente ou usar `pip` diretamente (ver seção de Execução).

### Arquivo `requirements.txt`

O arquivo `requirements.txt` (na raiz do repositório) centraliza as dependências necessárias para executar o projeto. Atualmente contém:

```
matplotlib
```

Para instalar tudo de uma vez:

Windows (PowerShell):

```powershell
pip install -r requirements.txt
```

Linux/macOS (bash):

```bash
pip install -r requirements.txt
```

Se forem adicionadas novas bibliotecas ao código-fonte, lembre-se de atualizar esse arquivo para manter o ambiente reprodutível.

## Estrutura do repositório

```
Teoria-dos-Grafos-2/
  data/
	 map_autoral_prof.txt  # arquivo de mapa (texto)
  src/
	 main.py               # ponto de entrada (CLI)
	 map_io.py             # leitura do mapa
	 visibility.py         # grafo de visibilidade
	 mst.py                # Prim (MST)
	 nearest.py            # vértice mais próximo visível
	 search.py             # busca na árvore (BFS)
	 plot.py               # funções de plot
  README.md
```

## Formato do arquivo de mapa (texto)

O formato segue o “formato do professor” (comentários iniciados por `#` e linhas em branco são ignorados):

```
x_start, y_start
x_goal, y_goal
N_OBST                  # número de obstáculos (>= 3)

N_VERT_OBST_1           # número de vértices do obstáculo 1
x1, y1
x2, y2
...

N_VERT_OBST_2
...
```

Exemplo real no repositório: `data/map_autoral_prof.txt` (com 3 obstáculos):

```
2.0, 9.0
14.0, 2.0
3
4
3.0, 6.0
5.5, 6.0
5.8, 4.2
3.2, 4.0
5
8.0, 8.5
10.5, 8.0
11.2, 6.6
9.6, 5.6
7.8, 6.8
3
12.5, 3.5
13.8, 1.5
11.6, 1.2
```

Observações importantes do modelo geométrico adotado:

- Segmentos que tocam exatamente nas quinas dos obstáculos são permitidos (apenas interseções “próprias” bloqueiam visibilidade).
- O caminho final é obtido na árvore geradora mínima (MST) do grafo de visibilidade, não no grafo completo.

## Como executar (Windows PowerShell)

1) (Opcional, mas recomendado) criar e ativar um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Instalar dependências mínimas:

```powershell
pip install matplotlib
```

3) Executar o programa apontando para um arquivo de mapa:

```powershell
python -m src.main -m data\map_autoral_prof.txt
```

O script abrirá uma janela com:

- Polígonos dos obstáculos
- Grafo de visibilidade entre quinas
- MST (sobreposto nas mesmas arestas do grafo que forem escolhidas pelo Prim)
- Segmentos conectando posição inicial/final aos vértices mais próximos visíveis
- Caminho na árvore entre os vértices encontrados (com anotações de índice)

Para testar outros pontos iniciais/finais, edite as duas primeiras linhas do arquivo de mapa.

## O que cada etapa faz

1. Leitura do mapa (`map_io.load_map`):
	- Interpreta o arquivo texto e carrega start, goal e obstáculos (polígonos).
2. Grafo de visibilidade (`visibility.build_visibility_graph`):
	- Liga pares de vértices sem interseção própria com arestas dos obstáculos.
3. MST com Prim (`mst.prim_mst`):
	- Constrói uma árvore geradora mínima a partir do grafo de visibilidade.
4. Vértice mais próximo visível (`nearest.verticeMaisProximo`):
	- Dado um ponto (start/goal), conecta ao vértice visível mais próximo.
5. Busca na árvore (`search.path_in_tree`):
	- Faz BFS na árvore para obter o caminho s→t (se existir).
6. Plot do caminho (`plot.plot_path` em `main.run`):
	- Desenha o caminho na figura, com índices de visita opcionais.

## Atendendo ao enunciado

- [x] 1) Arquivos de mapa: texto pronto em `data/map_autoral_prof.txt`. Imagem ilustrativa do mapa ainda deve ser adicionada (ex.: `data/map_autoral_prof.png`).
- [x] 2) Leitura + grafo de visibilidade
- [x] 3) Kruskal ou Prim (implementado Prim)
- [x] 4) verticeMaisProximo
- [x] 5) Busca na árvore (BFS)
- [x] 6) Plot do caminho no mapa (janela interativa)
- [x] 7) Instruções e organização do README (este arquivo)

## Resultados e prints (o que anexar no relatório)

Para avaliação, inclua capturas de tela do programa rodando, por exemplo:

- `docs/mapa_grafo.png` – mapa com grafo de visibilidade
- `docs/mst.png` – MST destacada
- `docs/caminho.png` – caminho na árvore entre start e goal

Sugestão: ao abrir a janela do Matplotlib, salve manualmente a figura (ícone de disquete) e coloque as imagens na pasta `docs/`.

## Notas técnicas e limitações

- A checagem de interseção usa interseção “própria”; tocar quinas é permitido, cruzar arestas bloqueia.
- O caminho é restrito à MST (pode não ser o caminho mais curto do grafo completo, é o caminho na árvore geradora construída por Prim).
- O arquivo de mapa atual já possui 3 obstáculos, como exigido.

