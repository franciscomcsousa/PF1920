Um programa em Python de simulacao de batalhas entre dois exercitos formados por unidades que se
movimentam e atacam dentro de um labirinto 2D, podendo conter obstaculos.
# 1 Simulacao de batalhas
## 1.1 Labirinto, unidades e exercitos
O labirinto e definido de forma identica a do primeiro projeto, ou seja, e uma estrutura
rectangular com posicoes indexadas a partir do canto superior esquerdo do labirinto, com
paredes nas posicoes do limite exterior, onde as restantes posicoes podem corresponder
a paredes ou a corredores. Os corredores podem ou nao ser ocupados por unidades.
Neste segundo projeto, cada unidade pertence a um de dois possıveis exercitos. As
unidades, para alem de se movimentarem no labirinto, atacam as unidades do exercito
contrario. Cada unidade, para alem da posicao no labirinto e o seu exercito, e caraterizada pelos seus pontos de vida e pela sua forca de ataque.
A ordem de leitura das posicoes do labirinto e definida como no primeiro projeto:
da esquerda para a direita seguida de cima para baixo.
## 1.2 Turno, movimento e ataque das unidades
A simulacao de uma batalha consiste na execucao de multiplos turnos de batalha, ate
que um dos dois exercitos ganhe, isto e, ate todas as unidades de um exercito terem sido
eliminadas, ou ate nao existirem mais movimentos possıveis. Em cada turno de batalha,
cada unidade –seguindo a ordem de leitura do labirinto– realiza um movimento e um
ataque.
O movimento consiste num unico passo para uma posicao adjacente seguindo as
regras de movimento das unidades descritas no primeiro projeto, com a unica diferenca de
que apenas sao consideradas como possıveis posicoes objetivo as posicoes adjacentes
livres de cada uma das unidades inimigas (isto e, do exercito contrario). Tal como no
primeiro projeto, uma unidade fica parada se ja se encontra numa posicao adjacente a
um inimigo ou se nao existir nenhuma posicao objetivo alcancavel.
Apos ter completado um movimento, se a unidade se encontra adjacente a pelo menos
uma unidade inimiga, entao realiza um ataque. Se existir mais de uma unidade inimiga
adjacente, o alvo do ataque e a primeira de acordo com a ordem de leitura do mapa.
O efeito de um ataque consiste em subtrair os pontos de forca de ataque da unidade
atacante aos pontos de vida da unidade atacada. Uma unidade atacada que fique sem
pontos de vida e eliminada, deixando de existir no turno de batalha corrente bem como
nos subsequentes.
