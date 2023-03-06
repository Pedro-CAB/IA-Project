# Projeto de IA - Wana

## 1. Descrição do jogo

* O Wana é um jogo de tabuleiro para 2 jogadores. Cada jogador tem 8 peças da sua cor. Estas peças estão dispostas em torre nas interseções das linhas do tabuleiro. O tabuleiro é composto por 6 linhas - 3 dipostas paralelamente na vertical e as outras 3 dispostas verticalmente na horizontal, que se intersetam nos 9 pontos centrais. Para além destas, existem 3 circunferências que intersetam os restantes pontos.

* Em cada jogada, o jogador deve mexer uma das suas peças. Essa peça pode-se mover ao longo de qualquer linha; contudo, não pode atravessar ou ocupar o mesmo espaço de outra peça, mas caso chegue ao fim do tabuleiro, esta irá aparecer no outro lado opsto.

* Caso um jogador possua uma peça que não pode ser mexida no início da sua jogada, perde o jogo.

> Tabuleiro com as peças dispostas no início do jogo:

![](https://i.imgur.com/faEAVuT.jpg)


## 2. Referências bibliográficas

* A descrição do jogo pode ser encontrada com mais detalhe no seguinte link: https://boardgamegeek.com/boardgame/364012/wana


## 3. Formulação do problema

* No contexto de IA, este jogo pode ser visto como um problema de pesquisa.

### Representação dos estados

* Lista de listas

### Estado inicial

```python

[
  ['/', '/', '/', 'A', 'o', 'A', '\', '\', '\'],
  ['o', 'o', 'o', 'A', 'o', 'A', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'A', 'o', 'A', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'A', 'o', 'A', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'B', 'o', 'B', 'o', 'o', 'o'],
  ['o', 'o', 'o', 'B', 'o', 'B', 'o', 'o', 'o'],
  ['\', '\', '\', 'B', 'o', 'B', '/', '/', '/'],
]
```

### Testagem do objetivo

* Obter uma peça que não se possa mexer no tabuleiro.

### Operadores

* up
    * pré-condições: o espaço imediatamente acima estar desocupado.
    * efeitos: peça avança o maior número de casas possível até colidir.
    * custo: 1.

* down
    * pré-condições: o espaço imediatamente abaixo estar desocupado.
    * efeitos: peça recua o maior número de casas possível até colidir.
    * custo: 1.

* left
    * pré-condições: o espaço imediatamente ao lado esquerdo estar desocupado.
    * efeitos: peça move para o lado esquerdo o maior número de casas possível até colidir.
    * custo: 1.

* right
    * pré-condições: o espaço imediatamente ao lado direiro acima estar desocupado.
    * efeitos: peça move para o lado direito o maior número de casas possível até colidir.
    * custo: 1.


### Heurísticas



## 4. Implementação

### Linguagem de programação e ambiente de desenvolvimento

* O projeto será implementado em Python, em ambiente de consola;

### Estruturas de dados

* Matriz bi-dimentsional para o tabuleiro.

* Árvores de pesquisa

* Struct peças:

```python
class piece:

    def __init_(self):
        self.player = '' #Can be 'A' for Player 1 or 'B' for Player 2
        self.id = 0
        self.x = 0
        self.y = 0
        
    def set_player(self, c):
        self.player = c
```


