# Navegação com Grafo de Visibilidade, MST (Prim) e Caminho

Projeto da disciplina para explorar estruturas de grafos em navegação: leitura de mapa (texto/imagem), construção de grafo de visibilidade, geração de árvore geradora mínima (Prim), conexão de pontos externos ao grafo (vértice visível mais próximo), busca de caminho na MST e visualizações com múltiplos esquemas de cores.

Este README descreve todo o processo: clonagem, configuração do ambiente, execução interativa e geração de variantes de visualização, além do formato dos dados.

## Visão geral das etapas (mapeadas ao código)

- Arquivo de mapa (texto) e imagem do mapa:
  - Texto: `data/map_autoral_prof.txt` (pronto).
  - Imagem: adicionar uma imagem ilustrativa do mapa (ex.: `data/map_autoral_prof.png`).
- Leitura do mapa e grafo de visibilidade: `src/map_io.py` e `src/visibility.py`.
- MST (Prim) no grafo de visibilidade: `src/mst.py`.
- Função verticeMaisProximo: `src/nearest.py`.
- Busca na árvore (caminho s→t): `src/search.py`.
- Plot do mapa, grafo e caminho: `src/plot.py` e fluxo em `src/main.py`.

## Requisitos e Instalação

- Python 3.10+ (recomendado)
- Bibliotecas Python:
  - `matplotlib` (para visualização)
  
Você pode instalar manualmente ou usar `pip` diretamente (ver seção de Execução). Recomenda-se ambiente virtual para isolar dependências.

### Arquivo `requirements.txt`

O arquivo `requirements.txt` (na raiz do repositório) centraliza as dependências necessárias para executar o projeto. Atualmente contém:

```
matplotlib
```

### Passo a passo desde a clonagem

1. Clonar o repositório:

	PowerShell:
	```powershell
	git clone https://github.com/LeoLucca98/Teoria-dos-Grafos-2.git
	cd Teoria-dos-Grafos-2
	```

	Bash (Linux/macOS/Git Bash):
	```bash
	git clone https://github.com/LeoLucca98/Teoria-dos-Grafos-2.git
	cd Teoria-dos-Grafos-2
	```

2. Criar ambiente virtual (opcional, mas recomendado):

	PowerShell:
	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

	Bash:
	```bash
	python -m venv .venv
	source .venv/bin/activate
	```

3. Instalar dependências:

	PowerShell:
	```powershell
	pip install -r requirements.txt
	```

	Bash:
	```bash
	pip install -r requirements.txt
	```

4. Verificar instalação:
	```bash
	python - <<'PY'
import matplotlib
print('matplotlib OK, versão:', matplotlib.__version__)
PY
	```

Se forem adicionadas novas bibliotecas, atualize `requirements.txt` e repita o passo de instalação.

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

## Execução Interativa (abre janela)

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

PowerShell:
```powershell
python -m src.main -m data\map_autoral_prof.txt
```

Bash:
```bash
python -m src.main -m data/map_autoral_prof.txt
```

Ao rodar:

- Abre uma janela Matplotlib com obstáculos, grafo de visibilidade, MST, pernas (start/goal → vértices mais próximos) e caminho na MST numerado.
- Salva automaticamente uma imagem com cores vívidas em `data/map_autoral_prof__run.png`.

- Polígonos dos obstáculos
- Grafo de visibilidade entre quinas
- MST (sobreposto nas mesmas arestas do grafo que forem escolhidas pelo Prim)
- Segmentos conectando posição inicial/final aos vértices mais próximos visíveis
- Caminho na árvore entre os vértices encontrados (com anotações de índice)

Para testar outros pontos iniciais/finais, edite as duas primeiras linhas do arquivo de mapa e reexecute.

### Geração de Variantes (sem abrir janela)

Use `--save-variants` (ou `-o`) para salvar automaticamente várias imagens estilizadas. Exemplo salvando direto em `data/`:

PowerShell:
```powershell
python -m src.main -m data\map_autoral_prof.txt -o data
```

Bash:
```bash
python -m src.main -m data/map_autoral_prof.txt -o data
```

Arquivos gerados (exemplos):
- `data/map_autoral_prof__default.png`
- `data/map_autoral_prof__mst-highlight.png`
- `data/map_autoral_prof__path-highlight.png`
- `data/map_autoral_prof__vis-only.png`
- `data/map_autoral_prof__mst-only.png`
- (Interativo) `data/map_autoral_prof__run.png`

Personalização: edite a lista `variants` em `src/main.py` (função `save_variants`) para mudar cores, alphas, espessuras e ativar/desativar partes (grafo, MST, caminho, pernas).

### Comandos resumidos

PowerShell:
```powershell
git clone https://github.com/LeoLucca98/Teoria-dos-Grafos-2.git
cd Teoria-dos-Grafos-2
python -m venv .venv
\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m src.main -m data\map_autoral_prof.txt           # interativo + salva run
python -m src.main -m data\map_autoral_prof.txt -o data    # variantes
```

Bash:
```bash
git clone https://github.com/LeoLucca98/Teoria-dos-Grafos-2.git
cd Teoria-dos-Grafos-2
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main -m data/map_autoral_prof.txt           # interativo + salva run
python -m src.main -m data/map_autoral_prof.txt -o data   # variantes
```

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

## Resultados e Prints (Relatório)

Para avaliação, inclua capturas de tela do programa rodando, por exemplo:

- `docs/mapa_grafo.png` – mapa com grafo de visibilidade
- `docs/mst.png` – MST destacada
- `docs/caminho.png` – caminho na árvore entre start e goal

Sugestão: ao abrir a janela do Matplotlib, salve manualmente a figura (ícone de disquete) e coloque as imagens na pasta `docs/`.

## Troubleshooting / Notas Técnicas

1. Em alguns ambientes Windows (Git Bash) pode ser necessário: `py -m pip install -r requirements.txt` ou `py -m src.main ...` se `python` não estiver no PATH.
2. A checagem de interseção usa interseção “própria”; tocar quinas é permitido, cruzar arestas bloqueia.
3. O caminho exibido está na MST (não garante o menor caminho do grafo completo).
4. O arquivo de mapa atual já possui 3 obstáculos conforme enunciado; edite para testar outros cenários.
5. Imagem gerada automaticamente na execução interativa: `data/<map>__run.png`.