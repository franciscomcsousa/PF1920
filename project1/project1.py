#Francisco Sousa ist195579

#----------------------------#Funcoes Auxiliares#------------------------------#

#funcao tem_repetidos verifica se um tuplo tem elementos repetidos
def tem_repetidos(tup):
    res = ()
    for i in tup:
        if i not in res:
            res = res + (i, )
    return res != tup

#verifica se a posicao pos e corredor num labirinto lab
def eh_corredor(lab, pos):
    if not eh_posicao(pos):
        return False
    if pos[0] > tamanho_labirinto(lab)[0]\
       or pos[1] > tamanho_labirinto(lab)[1]:
        return False
    elif lab[pos[0]][pos[1]] != 0:
        return False
    return True
    

#-----------------------------#Funcoes Principais#-----------------------------#

def eh_labirinto(lab):
#verifica se o labirinto e tuplo com comprimento maior ou igual a 3
    if not isinstance(lab, tuple) or len(lab) < 3:
        return False
#verifica se os subtuplos do labirinto teem comprimento maior ou igual a 3
    for i in lab:                                                               
        if not isinstance(i, tuple) or len(i) < 3:
            return False
#verifica se existe parede esquerda e direita        
        elif i[0] != 1 or i[len(i) - 1] != 1:
            return False
#verifica se os elementos do labirinto sao inteiros 0 ou 1
        for j in i:
            if j != 1 and j != 0 or not isinstance(j, int):
                return False
    for i in range(len(lab) - 1):
#verifica que todos os subtuplos sao de mesmo comprimento
        if len(lab[i]) != len(lab[i + 1]):
            return False
    for i in range(len(lab[0])):
#verifica se existe parede superior e inferior
        if lab[0][i] != 1 or lab[len(lab) - 1][i] != 1:                    
            return False
    return True
#Nota - como todos subtuplos teem o mesmo comprimento
#lab[0] e considerado o comprimento generico dos subtuplos

def eh_posicao(pos):
    if not isinstance(pos, tuple) or len(pos) != 2:
        #se nao for (x, y) nem for tuplo
        return False
    for i in pos:
        if not isinstance(i, int) or i < 0:
        #cordenadas teem de ser positivas inteiras
            return False
    return True

def eh_conj_posicoes(conj):
    #maior_indice = len(conj) - 1
    if not isinstance(conj, tuple):
        return False
    for j in range(len(conj)):
        #cada elemento do conjunto tem que ser tuplo
        if not isinstance(conj[j], tuple):
            return False
    for i in conj:
        #cada subtuplo tem que ser posicao
        if len(i) != 2 or not (eh_posicao(i)):
            return False
    if tem_repetidos(conj):
        #conjunto de posicoes nao pode ter estas repetidas
        return False
    return True

def tamanho_labirinto(lab):
    if not eh_labirinto(lab):
        raise ValueError ("tamanho_labirinto: argumento invalido")
    return (len(lab),(len(lab[0])))

def eh_mapa_valido(lab, cords):
    if not eh_labirinto(lab) or not eh_conj_posicoes(cords):
        raise ValueError ("eh_mapa_valido: algum dos argumentos e invalido")
    for i in cords:
        if not eh_corredor(lab, i):
            #verifica se cada uma das cordenadas eh um corredor
            return False
    return True
#i[0] corresponde a x, i[1] a y  ; das cordenadas
#len(lab) corresponde a x, len(lab[0] corresponde a y ; do labirinto

def eh_posicao_livre(lab, uni, pos):
    if not eh_labirinto(lab)\
       or not eh_posicao(pos)\
       or not eh_conj_posicoes(uni)\
       or not eh_mapa_valido(lab, uni):
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
    if not eh_corredor(lab, pos):
        #funcao eh_corredor verifica se um espaco no labirinto eh corredor
        return False
    for i in uni:
        if i == pos:
            return False
    return True

def posicoes_adjacentes(pos):
    #adjacentes sao as posicoes acima, abaixo, esquerda e direita (validas)
    if not eh_posicao(pos):
        raise ValueError ("posicoes_adjacentes: argumento invalido")
    res = ()
    #conjunto seguinte de 'ifs' verifica se cada adjacentes eh posicao
    if eh_posicao((pos[0], pos[1] - 1)):#posicao acima
        res += ((pos[0], pos[1] - 1),)
        
    if eh_posicao((pos[0] - 1, pos[1])):#posicao esquerda
        res += ((pos[0] - 1, pos[1]), )
        
    if eh_posicao((pos[0] + 1, pos[1])):#posicao direita
        res += ((pos[0] + 1, pos[1]),)
        
    if eh_posicao((pos[0], pos[1] + 1)):#posicao abaixo
        res += ((pos[0], pos[1] + 1),)
    return res

def mapa_str(lab, uni):
    if not eh_labirinto(lab)\
       or not eh_conj_posicoes(uni)\
       or not eh_mapa_valido(lab, uni):
        #Nota - se eh_labirinto e eh_conj_posicoes nao fossem confirmados,
        #o erro poderia ser de 'eh_mapa_valido'
        raise ValueError ("mapa_str: algum dos argumentos e invalido")
    string = ''
    salta_subtuplo = False #variavel que avanca para o proximo subtuplo

    for j in range(len(lab[0])):           
        for i in range(len(lab)):           
            for u in uni:
                if u[0] == i and u[1] == j:
                    string += 'O'
                    #se for unidade, apresenta um 'O'
                    salta_subtuplo = True
                    #sendo unidade, nao adiciona ".", e 'salta' para seguinte
            if salta_subtuplo:
                i += 1             
            elif lab[i][j] == 1:
                    string += '#'
                    #se for parede, apresenta um '#'
            elif lab[i][j] == 0:
                string += '.'
                #se for corredor, apresenta um '.'
            salta_subtuplo = False
        string += '\n'
        #depois de percorrer o primeiro elemento de cada subtuplo, muda a linha
    return string[:len(string) - 1]
    #na string existe um '\n' em excesso, nao le ultimos 2 caracteres da string

def obter_objetivos(lab,uni,partida):
    if not eh_labirinto(lab)\
       or not eh_conj_posicoes(uni)\
       or not eh_mapa_valido(lab, uni)\
       or not (partida in uni):
        raise ValueError ("obter_objetivos: algum dos argumentos e invalido")
    adjacentes = ()  #tuplo de todos os adjacentes a unidades
    resultado = ()   #objetivo
    for i in uni:
        if i != partida:
            #filtra partida do conjunto de unidades
            adjacentes += posicoes_adjacentes(i)
    for e in adjacentes:
        if eh_posicao_livre(lab,uni,e) and e not in resultado:
            resultado += (e,)
        #objetivos sao os adjacentes de todas as unidades excepto a partida 
    return resultado
    

def obter_caminho(lab,uni,unidade):
    #unidade eh a unidade de partida
    #uni eh o conjunto de unidades
    if not eh_labirinto(lab)\
       or not eh_conj_posicoes(uni)\
       or not eh_mapa_valido(lab, uni)\
       or unidade not in uni:
        raise ValueError ("obter_caminho: algum dos argumentos e invalido")
    
    if uni == (unidade,):
        return ()
    #se o conjunto de unidades apenas tiver a unidade, nao ha caminho
    
    objetivos = obter_objetivos(lab,uni,unidade)
    visitadas = () #tuplo que armazena posicoes visitadas
    lista_exploracao = [(unidade,()),]
    #lista de exploracao inicia apenas com a unidade de partida
    
    while len(lista_exploracao) != 0:
        if lista_exploracao[0][0] in visitadas: #se a posicao foi visitada
            del lista_exploracao[0] #remove essa posicao e caminho da lista
        if lista_exploracao != []: #se for vazia nao faz o proximo procedimento
            pos_atual = lista_exploracao[0][0] #primeira posicao da lista
            caminho = lista_exploracao[0][1] #primeiro caminho da lista
        if pos_atual not in visitadas: #se pos_atual foi visitada, refaz ciclo
            visitadas += (pos_atual,) #pos_atual passa a ser visita
            caminho += (pos_atual,) #pos_atual eh adicionada ao caminho
            if pos_atual in objetivos:
                return caminho
            #se pos_atual eh um objetivo, retorna caminho que leva ate la
            else:
                for e in posicoes_adjacentes(pos_atual):
                    #para todas as posicoes_adjacentes a atual
                    if eh_posicao_livre(lab, uni, e):
                        lista_exploracao += ((e,(caminho)),)
                        #adiciona as adjacentes e o caminho ate elas a lista
    return ()
                        
def mover_unidade(lab, uni, unidade):
    if not eh_labirinto(lab)\
       or unidade not in uni\
       or not eh_mapa_valido(lab, uni):
        raise ValueError ("mover_unidade: algum dos argumentos e invalido")
    res = ()
    if obter_caminho(lab, uni, unidade) == ():
        #se nao existir caminho unidade nao se move
        return uni
    for i in uni:
        if i in posicoes_adjacentes(unidade):
            #se unidades estiverem adjacentes
            return uni #manteem-se no mesmo lugar
        if i == unidade: #identifica a unidade nas unidades
            res += (obter_caminho(lab, uni, unidade)[1],)
            #segundo elemento do seu caminho para onde a unidade se desloca
        else:
            res += (i,)
    return res