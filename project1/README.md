Neste primeiro projecto de Fundamentos da Programacao os alunos irao desenvolver
as funcoes que permitam implementar um programa para simular o movimento de uma
unidade atraves de um labirinto 2D contendo obstaculos e outras unidades. Esta unidade
movimenta-se sempre para um espa¸co adjacente de forma a aproximar-se de uma das
unidades alcancaveis mais proximas restantes no labirinto.
# 1 Movimento num labirinto
## 1.1 O labirinto e as unidades
O labirinto e uma estrutura rectangular de tamanho Nx × Ny, sendo Nx o tamanho
maximo do eixo de abcissas e Ny o tamanho maximo do eixo de ordenadas. Cada posicao
(x, y) do labirinto e indexada a partir da posicao de origem (0, 0) que corresponde ao
canto superior esquerdo do labirinto. Num labirinto, todas as posicoes do limite exterior
sao paredes, ou seja, correspondem a posicoes que nao podem ser ocupadas. As restantes
posicoes podem corresponder a paredes ou a corredores. Corredores (ou espacos vazios)
sao posicoes passıveis de serem ocupadas por unidades que se movimentam no labirinto.
A ordem de leitura das posicoes do labirinto e sempre feita da esquerda para a direita
seguida de cima para baixo.
## 1.2 Regras de movimento das unidades
O movimento de uma unidade e calculado atraves da aplicacao das seguintes regras:
• Uma unidade movimenta-se dando passos. Um passo e definido como sendo um
unico movimento realizado para uma posicao adjacente. O conjunto de posicoes
adjacentes a uma unidade e definido como sendo as posicoes situadas imediatamente acima, abaixo, a direita ou a esquerda dela. As unidades nao podem
atravessar paredes nem outras unidades.
• Para escolher a posicao seguinte de uma dada unidade, comeca-se por identificar
o conjunto de possıveis posicoes objetivo, sendo estas as posicoes adjacentes
livres de cada uma das restantes unidades. Se inicialmente a unidade ja se encontra
adjacente a uma outra unidade, fica parada. 
• De seguida, determina-se o caminho de numero mınimo de passos desde a
unidade ate a posicao objetivo. A posicao objetivo e aquela (dentre as possıveis
posicoes objetivo) que se encontra a numero mınimo de passos. Se mais do que
uma posicao objetivo estiver a mesma distˆancia (numero de passos) mınima, entao
a posicao objetivo e a primeira seguindo a ordem de leitura do labirinto. Se nao
existe nenhum caminho possıvel entre a unidade e as possıveis posicoes objetivo, a
unidade nao se move.
• Na processo de determinacao do caminho de numero mınimo de passos, se multiplas
posicoes adjacentes colocam a unidade a exactamente a mesma distˆancia do objetivo (multiplos caminhos mınimos), entao a posicao seguinte escolhida e a primeira
de acordo com a ordem de leitura do labirinto. 
• Finalmente, a unidade avanca uma posicao seguindo o caminho de numero mınimo
de passos encontrado
## 1.3 Procura do caminho de numero mınimo de passos
Existem diversos algoritmos que permitem resolver o problema para a obtencao do caminho de numero mınimo de passos entre duas posicoes num labirinto. Uma possıvel
abordagem e o algoritmo de Lee1 que se baseia no Breadth-First Search ,um algoritmo para atravessar ou procurar em grafos.
O algoritmo BFS baseia-se em garantir a exploracao, ou visita, em primeiro lugar
de todas as posicoes atingıveis com igual numero de passos, antes de passar a explorar
posicoes atingıveis com um numero de passos maior. Para isso, recorre a uma estrutura de dados linear conhecida como fila onde as novas posicoes a serem exploradas
sao acrescentadas no final da fila. Chamamos a esta estrutura a fila de exploracao.
Inicialmente, a fila de exploracao contem apenas a posicao inicial. De seguida, o algoritmo processa em ciclo as posicoes encontradas na fila de exploracao retirando sempre
aquela que se encontra na primeira posicao ate atingir a condicao de terminacao (por
exemplo, a posicao retirada e a de destino) ou ate que a fila de exploracao se encontrar
vazia (neste caso, nao se conseguiu atingir a condicao de terminacao). Para cada posicao
da fila de exploracao, o ciclo de processamento comeca por verificar se a posicao ja foi
visitada previamente. Se sim, a posicao e retirada da fila e passa-se a proxima posicao.
Se nao, explora-se a posicao e assinala-se como visitada. Para que isto seja possıvel, e
preciso guardar as posicoes ja visitadas numa estrutura chamada posicoes visitadas.
A exploracao de uma posicao consiste em acrescentar a fila de exploracao as posicoes
adjacentes vazias. De forma a poder recuperar o caminho quando atinjamos a posicao
destino, e necessario guardar a sequˆencia de posicoes adjacentes que nos levou ate
cada posicao explorada.
Neste primeiro projecto o objetivo e encontrar o caminho de numero mınimo
de passos desde uma posicao dada ate uma das possıveis posicoes objetivo, de acordo com
as regras de desempate e de movimento descritas na seccao anterior. O algoritmo BFS
garante que a primeira posicao visitada que corresponder a uma das possıveis posicoes
objetivo encontra-se a numero mınimo de passos. Por outro lado, para garantir que se cumprem as regras de desempate na escolha da posicao seguinte e da posicao objetivo,
basta que na fase de exploracao sejam acrescentadas as posicoes a fila de exploracao pela
ordem adequada (de menor a maior ordem de leitura).


