###------------------------Funcoes Auxiliares--------------------------------###
def eh_int_positivo(x):
    '''
    eh_int_positivo recebe um numero e devolve True se este for inteiro
    e positivo.
    
    eh_int_positivo: N -> booleano
    '''
    return isinstance(x, int) and x > 0

###----------------------------TAD Posicao-----------------------------------###

#Construtor
def cria_posicao(x, y):
    '''
    cria_posicao recebe os valores correspondentes as coordenadas de uma
    posicao e devolve a posicao correspondente.
    
    cria_posicao: N2 -> posicao
    '''
    if not isinstance(x, int) or not isinstance(y, int) or not x >= 0 or not y >= 0:
        raise ValueError ("cria_posicao: argumentos invalidos")
    return (x, y) #posicao sera apresentada na forma de tuplo

def cria_copia_posicao(p):
    '''
    cria_copia_posicao recebe uma posicao e devolve uma copia nova da posicao.
    
    cria_copia_posicao: posicao -> posicao
    '''
    return (p[0], p[1]) #p[0] -> x, p[1] -> y

#Seletor
def obter_pos_x(p):
    '''
    obter_pos_x devolve a componente x da posicao p.
    
    obter_pos_x: posicao -> N
    '''
    return p[0] #corresponde ao primeiro valor do tuplo, neste caso, x

def obter_pos_y(p):
    '''
    obter_pos_y devolve a componente y da posicao p.
    
    obter_pos_y: posicao -> N
    '''
    return p[1] #corresponde ao segundo valor do tuplo, neste caso, y

#Reconhecedor
def eh_posicao(arg):
    '''
    eh_posicao devolve True caso o seu argumento seja um TAD posicao e
    False caso contrario.
    
    eh_posicao: universal -> booleano
    '''
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int)\
           and isinstance(arg[1], int) and arg[0] >= 0 and arg[1] >= 0
    #para argumento ser posicao, requer ser tuplo com comprimento 2 e com
    #elementos inteiros maiores ou iguais a 0
#Teste    
def posicoes_iguais(p1, p2):
    '''
    posicoes_iguais devolve True apenas se p1 e p2 sao posicoes iguais.
    
    posicoes_iguais: posicao -> booleano
    '''
    return p1 == p2

#Transformador
def posicao_para_str(p):
    '''
    posicao para str devolve a cadeia de caracteres '(x, y)' que representa o
    seu argumento, sendo os valores x e y as coordenadas de p.
    
    posicao para str: posicao -> str
    '''
    return str((obter_pos_x(p), obter_pos_y(p))) #corresponde a '(x, y)'

#Alto nivel
def obter_posicoes_adjacentes(p):
    '''
    obter_posicoes_adjacentes devolve um tuplo com as posicoes adjacentes a posicao
    p de acordo com a ordem de leitura de um labirinto.
    
    obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    '''
    return tuple(filter(lambda x: obter_pos_x(x) >= 0 and obter_pos_y(x) >= 0\
                        and isinstance(obter_pos_x(x), int)\
                        and isinstance(obter_pos_y(x), int),
                        ((obter_pos_x(p), obter_pos_y(p) - 1),\
                        (obter_pos_x(p) - 1, obter_pos_y(p)),\
                        (obter_pos_x(p) + 1, obter_pos_y(p)),\
                        (obter_pos_x(p), obter_pos_y(p) + 1)),))
#equivale a devolver a posicao acima, esquerda, direita e abaixo repetivamente
#Nota - nao eh utilizado eh posicao pois este quebraria as normas de abstracao

#------------------------------------------------------------------------------#
###-------------------------------TAD Unidade--------------------------------###
#Construtor
def cria_unidade(p, v, f, string):
    '''
    cria_unidade recebe uma posicao p, dois valores inteiros maiores
    que 0 correspondentes a vida e forca da unidade, e uma cadeia de caracteres
    nao vazia correspondente ao exercito da unidade; e devolve a unidade correspondente.
    
    cria_unidade: posicao x N x N x str -> unidade
    '''
    if not eh_posicao(p) or not eh_int_positivo(f) or not eh_int_positivo(v)\
       or not isinstance(string, str) or string == '':
        raise ValueError ("cria_unidade: argumentos invalidos")
    return {'posicao' : p, 'vida' : v, 'forca' : f, 'nome' : string}
#unidade sera representada na forma de dicionario

def cria_copia_unidade(u):
    '''
    cria_copia_unidade recebe uma unidade u e devolve uma nova copia da
    unidade.
    
    cria_copia_unidade: unidade -> unidade
    '''
    return cria_unidade(u['posicao'], u['vida'], u['forca'], u['nome'])
#cria uma nova unidade com mesma posicao, vida, forca e nome

#Seletor
def obter_posicao(u):
    '''
    obter_posicao devolve a posicao da unidade u.
    
    obter_posicao: unidade -> posicao
    '''
    return u['posicao'] #correponde a posicao (da unidade)

def obter_exercito(u):
    '''
    obter_exercito devolve a cadeia de carateres correspondente ao exercito da
    unidade.
    
    obter_exercito: unidade -> str
    '''
    return u['nome'] #correponde ao nome (do exercito da unidade)

def obter_forca(u):
    '''
    obter_forca devolve o valor corresponde a forca de ataque da unidade.
    
    obter_forca: unidade -> N
    '''
    return u['forca'] #correponde a forca (da unidade)

def obter_vida(u):
    '''
    obter_vida devolve o valor corresponde aos pontos de vida da unidade.
    
    obter_forca: unidade -> N
    '''
    return u['vida'] #corresponde a vida (da unidade)

#Modificador
def muda_posicao(u, p):
    '''
    muda_posicao modica destrutivamente a unidade u alterando a sua
    posicao com o novo valor p, e devolve a propria unidade.
    
    muda_posicao: unidade x posicao -> unidade
    '''
    u['posicao'] = p #altera o valor da chave 'posicao' para a posicao dada p
    return u

def remove_vida(u, v):
    '''
    remove_vida modica destrutivamente a unidade u alterando os seus
    pontos de vida subtraindo o valor v, e devolve a propria unidade.
    
    unidade x N -> unidade
    '''
    u['vida'] = u['vida'] - v #altera o valor da chave 'vida' para este menos o valor dado v 
    return u

#Reconhecedor
def eh_unidade(arg):
    '''
    eh_unidade devolve True caso o seu argumento seja um TAD unidade e
    False caso contrario.
    
    eh_unidade: universal -> booleano
    '''
    return isinstance(arg, dict) and len(arg) == 4\
           and 'posicao' in arg and 'vida' in arg and 'forca' in arg and 'nome' in arg\
           and eh_posicao(arg['posicao']) and eh_int_positivo(arg['forca']) and eh_int_positivo(arg['vida'])\
           and isinstance(arg['nome'], str) and arg['nome'] != ''
#para ser unidade tem de ser um dicionario de comprimento = 4, as respetivas chaves
#teem de estar neste e cada uma destas tem de correponder ao tipo que eh

#Teste
def unidades_iguais(u1, u2):
    '''
    unidades_iguais devolve True apenas se u1 e u2 sao unidades iguais.
    
    unidades_iguais: unidade x unidade -> booleano
    '''
    return u1 == u2

#Trasformadores
def unidade_para_char(u):
    '''
    unidade_para_char( devolve a cadeia de caracteres dum unico elemento,
    correspondente ao primeiro caracter em maiuscula do exercito da unidade
    passada por argumento.
    
    unidade_para_char: unidade -> str
    '''
    return u['nome'][0].upper()
#obtem a primeira letra do nome do exercito da unidade
#funcao .upper tranforma esta letra numa maiuscula

def unidade_para_str(u):
    '''
    unidade_para_str devolve a cadeia de caracteres que representa a unidade
    como mostrado nos exemplos a seguir.
    
    unidade_para_str: unidade -> str
    '''
    return str(unidade_para_char(u)) + str([u['vida'], u['forca']]) + '@' + posicao_para_str(u['posicao'])

#Alto nivel
def unidade_ataca(u1, u2):
    '''
    unidade_ataca modica destrutivamente a unidade u2 retirando o valor de
    pontos de vida correspondente a forca de ataque da unidade u1. A funcao devolve
    True se a unidade u2 for destruida ou False caso contrario.
    
    unidade_ataca: unidade x unidade -> booleano
    '''
    u2 = remove_vida(u2, obter_forca(u1)) #altera destrutivamente u2
    if obter_vida(u2) > 0:
        return False
    else:
        return True
    
def ordenar_unidades(t):
    '''
    ordenar unidades devolve um tuplo contendo as mesmas unidades do tuplo fornecido 
    como argumento, ordenadas de acordo com a ordem de leitura do labirinto.
    
    tuplo_unidades -> tuplo_unidades
    '''
    def eixo_x(u):
        #funcao que recebe uma unidade e devolve a componente x da sua posicao
        return obter_pos_x(obter_posicao(u))
    def eixo_y(u):
        #funcao que recebe uma unidade e devolve a componente y da sua posicao
        return obter_pos_y(obter_posicao(u))
    lst = list(t) #transforma o tuplo t numa lista
    lst.sort(key=eixo_x) #.sort ordena a lista primeiro pela componente y da posicao (crescente)
    lst.sort(key=eixo_y) # depois ordena a lista pela componente x da posicao (crecente)
    return tuple(lst) #converte a lista para tuplo
#------------------------------------------------------------------------------#
###-------------------------------TAD Mapa-----------------------------------###
#Contrutor    
def cria_mapa(d, w, e1, e2): #o mapa vai ser representado na forma de um dicionario
    '''
    cria mapa recebe um tuplo d de 2 valores inteiros correspondentes
    as dimensoes Nx e Ny (ambas maiores que 3), um tuplo w de 0 ou mais posicoes
    correspondentes as paredes que nao sao dos limites exteriores do labirinto, 
    tuplos e1 e e2 de 1 ou mais unidades do mesmo exercito.
    Devolve o mapa que representa internamente o labirinto e as unidades presentes.
    
    cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa
    '''
    mapa = {}
    if isinstance(d, tuple) and isinstance(w, tuple) and isinstance(e1, tuple)\
       and isinstance(e2, tuple) and len(d) == 2 and len(e1) > 0 and len(e2) > 0:
        #verificao dos argumentos dados
        for a in e1:
            if not eh_unidade(a):
                #todas os argumentos em e1 teem que ser unidades
                raise ValueError ("cria_mapa: argumentos invalidos")
        for b in e2:
            if not eh_unidade(b):
                #todas os argumentos em e2 teem que ser unidades
                raise ValueError ("cria_mapa: argumentos invalidos")        
        for a in d:
            if not isinstance(a, int) or not a >= 3:
                #todas os argumentos em d teem que ser inteiros maiores ou iguais a 3
                raise ValueError ("cria_mapa: argumentos invalidos")
        for b in w:
            if not isinstance(b, tuple) or not eh_posicao(b):
                #cada elemento dentro de w tem de ser uma posicao
                raise ValueError ("cria_mapa: argumentos invalidos")
            else:
                if b[0] > d[0] or b[1] > d[1] or b[0] == 0 or b[1] == 0:
                    #cada elemento de w nao pode ser limite do mapa
                    raise ValueError ("cria_mapa: argumentos invalidos")      
        mapa['dimensao'] = d
        mapa['walls'] = w
        mapa['exercito1'] = e1
        mapa['exercito2'] = e2
        return mapa #mapa sera representado na forma de dicionario
    else:
        raise ValueError ("cria_mapa: argumentos invalidos")
    
def cria_copia_mapa(mapa):
    '''
    cria_copia_mapa recebe um mapa e devolve uma nova copia do mapa.
    
    cria_copia_mapa: mapa -> mapa
    '''
    #Nota - de forma a tornar a copia do mapa independente do original,
    #eh necessario executar um ciclo for para cada uma das cheves do dicionario
    nova_dimensao = cria_copia_posicao(obter_tamanho(mapa))
    #dimensao nao necessita de ciclo pois apenas eh uma posicao
    nova_walls = ()
    nova_exercito1 = ()
    nova_exercito2 = ()
    for w in mapa['walls']:
        nova_walls += (cria_copia_posicao(w),)
        #para cada elemento do novo w eh criada uma nova posicao
    for e1 in mapa['exercito1']:
        nova_exercito1 += (cria_copia_unidade(e1),)
        #para cada elemento do novo e1 eh criada uma nova unidade
    for e2 in mapa['exercito2']:
        nova_exercito2 += (cria_copia_unidade(e2),)
        #para cada elemento do novo e2 eh criada uma nova unidade
    return cria_mapa(nova_dimensao, nova_walls, nova_exercito1, nova_exercito2)

#Seletores
def obter_tamanho(mapa):
    '''
    obter_tamanho devolve um tuplo de dois valores inteiros correspondendo
    o primeiro deles a dimensao Nx e o segundo a dimensao Ny do mapa.
    
    obter_tamanho: mapa -> tuplo
    '''
    return mapa['dimensao'] #chave que contem a dimensao do mapa

def obter_nome_exercitos(mapa):
    '''
    obter_nome_exercitos devolve um tuplo ordenado com duas cadeias de
    caracteres correspondendo aos nomes dos exercitos do mapa.
    
    obter_nome_exercitos mapa -> tuplo
    '''
    #obter_exercito(mapa['exercito1/exercito2'][0]) corresponde ao nome do exercito
    # a < z, permite organizar os nomes de forma alfabetica
    if obter_exercito(mapa['exercito1'][0]) < obter_exercito(mapa['exercito2'][0]): 
        #nome de exercito1 < nome de exercito2
        return (obter_exercito(mapa['exercito1'][0]), obter_exercito(mapa['exercito2'][0]))
    else:
        return (obter_exercito(mapa['exercito2'][0]), obter_exercito(mapa['exercito1'][0]))
    
def obter_unidades_exercito(mapa, e):
    '''
    obter_unidades_exercito devolve um tuplo contendo as unidades do
    mapa pertencentes ao exercito indicado pela cadeia de caracteres e, ordenadas
    em ordem de leitura do labirinto.
    
    obter_unidades_exercito: mapa x str -> tuplo unidades
    '''
    #obter_exercito(mapa['exercito1/exercito2'][0]) corresponde ao nome do exercito
    #len(mapa['exercito1']/mapa['exercito2']) != 0 -> exercitos nao podem ser ordenados se sao vazios
    if len(mapa['exercito1']) != 0 and e in obter_exercito(mapa['exercito1'][0]):
        return ordenar_unidades(mapa['exercito1'])
    elif len(mapa['exercito2']) != 0 and e in obter_exercito(mapa['exercito2'][0]):
        return ordenar_unidades(mapa['exercito2'])
    else:
        return ()
                            
    
def obter_todas_unidades(mapa):
    '''
    obter_todas_unidades devolve um tuplo contendo todas as unidades do
    mapa, ordenadas em ordem de leitura do labirinto.
    
    obter_todas_unidades: mapa -> tuplo
    '''
    return ordenar_unidades(mapa['exercito1'] + mapa['exercito2'])
#junta as unidades do exercito 1 e 2 e organiza-as

def obter_unidade(mapa, posicao):
    '''
    obter_unidade devolve a unidade do mapa que se encontra na posicao p.
    
    obter_unidade: mapa x posicao -> unidade
    '''
    for unidade in obter_todas_unidades(mapa):
        #percorre todas as unidades
        if obter_posicao(unidade) == posicao:
            #verifica se alguma tem a posicao igual a fornecida como argumento
            return unidade
        
#Modificadores
def eliminar_unidade(mapa, unidade):
    '''
    eliminar_unidade modica destrutivamente o mapa m eliminando a unidade u 
    do mapa e deixando livre a posicao onde se encontrava a unidade.
    Devolve o proprio mapa.
    
    eliminar_unidade: mapa x unidade -> mapa
    '''
    mapa['exercito1'] = tuple(filter(lambda x: x != unidade, mapa['exercito1']))
    mapa['exercito2'] = tuple(filter(lambda x: x != unidade, mapa['exercito2']))
    #filter filtra (remove) todos os elementos do tuplo que sejam iguais a unidade dada
    return mapa

def mover_unidade(mapa, unidade, posicao):
    '''
    mover_unidade modica destrutivamente o mapa m e a unidade u alterando
    a posicao da unidade no mapa para a nova posicao p e deixando livre a 
    posicao onde se encontrava. Devolve o proprio mapa.
    
    mover_unidade: mapa x unidade x posicao -> mapa
    '''
    def altera(x):
        if x == unidade:
            #se x for igual a unidade dada, muda a posicao da unidade para a posicao dada
            return muda_posicao(x, posicao)
        else:
            #senao, x mantem-se o mesmo (apenas modifica x se este for igual a unidade dada)
            return x
    mapa['exercito1'] = tuple(map(lambda x: altera(x), mapa['exercito1']))
    mapa['exercito2'] = tuple(map(lambda x: altera(x), mapa['exercito2']))
    #map aplica a funcao altera a todos os elementos do tuplo
    return mapa

#Reconhecedores
def eh_posicao_unidade(mapa, posicao):
    '''
    eh_posicao_unidade devolve True apenas no caso da posicao p do mapa
    estar ocupada por uma unidade.
    
    eh_posicao_unidade: mapa x posicao -> booleano
    '''
    return eh_unidade(obter_unidade(mapa, posicao))
#para uma posicao ser unidade basta que uma unidade correponda a essa posicao

def eh_posicao_corredor(mapa, posicao):
    '''
    eh_posicao_corredor devolve True apenas no caso da posicao p do mapa
    corresponder a um corredor no labirinto (independentemente de estar
    ou nao ocupado por uma unidade).
    
    eh_posicao_corredor: mapa x posicao -> booleano
    '''
    return obter_tamanho(mapa)[0] - 1 > obter_pos_x(posicao) and\
           obter_tamanho(mapa)[1] - 1 > obter_pos_y(posicao)  and\
           not eh_posicao_parede(mapa, (obter_pos_x(posicao), obter_pos_y(posicao)))
#para ser corredor, a posicao tem que estar dentro dos limites do mapa
#e nao pode ser uma parede

def eh_posicao_parede(mapa, posicao):
    '''
    eh_posicao_parede devolve True apenas no caso da posicao p do mapa
    corresponder a uma parede do labirinto.
    
    eh_posicao_parede: mapa x posicao -> booleano
    '''
    return ((obter_pos_x(posicao) == 0 or obter_pos_x(posicao) == obter_tamanho(mapa)[0] - 1) or\
           (obter_pos_y(posicao) == 0 or obter_pos_y(posicao) == obter_tamanho(mapa)[1] - 1) or\
           posicao in mapa['walls'])
#para ser parede, a posicao ou esta nos limites do mapa, ou o x e/ou o y com o valor 0
#ou faz parte do conjunto de 'walls' do mapa

#Testes
def mapas_iguais(m1, m2):
    '''
    mapas_iguais devolve True apenas se m1 e m2 forem mapas iguais.
    
    mapas_iguais: mapa x mapa -> booleano
    '''
    return m1 == m2

#Transformador
def mapa_para_str(mapa):
    '''
    mapa_para_str devolve uma cadeia de caracteres que representa o mapa como 
    descrito no primeiro projeto, neste caso, com as unidades representadas
    pela sua representacao externa.
    
    mapa_para_str: mapa -> str
    '''
    mapa_aux = {} #mapa auxiliar, que eh um dicionario
    for x in range(obter_tamanho(mapa)[0]):
        mapa_aux[x] = []
        #cada chave (coluna) de mapa_aux correponde a uma lista (linha)
        for y in range(obter_tamanho(mapa)[1]):
            if eh_posicao_parede(mapa, (x, y)):
                #paredes representadas por '#'
                mapa_aux[x] += ['#',]
            elif eh_posicao_corredor(mapa, (x, y)) and not eh_posicao_unidade(mapa, (x, y)):
                #corredores representados por '.'
                mapa_aux[x] += ['.',]            
            elif eh_posicao_unidade(mapa, (x, y)):
                #unidades representradas pela primeira letra (maiuscula) do seu nome
                mapa_aux[x] += [unidade_para_char(obter_unidade(mapa, (x, y))),]
    mapa_str = '' #mapa_str -> string
    for lines in range(obter_tamanho(mapa)[1]):
        for columns in range(obter_tamanho(mapa)[0]):
            mapa_str += mapa_aux[columns][lines]
        mapa_str += '\n'
        #mapa_string eh as colunas de cada linha de mapa_aux seperadas por '\n'
    return mapa_str[0 : len(mapa_str) - 1]
# [0 : len(mapa_str) - 1] remove '\n' do fim (em excesso)

#Alto nivel
def obter_inimigos_adjacentes(mapa, unidade):
    '''
    obter_inimigos_adjacentes devolve um tuplo contendo as unidades inimigas
    adjacentes a unidade u de acordo com a ordem de leitura do labirinto.
    
    obter_inimigos_adjacentes: mapa x unidade -> tuplo unidades
    '''
    adjacentes = ()
    for posicao in obter_posicoes_adjacentes(obter_posicao(unidade)):
        #para cada posicao nas posicoes adjacentes
        if eh_posicao_unidade(mapa, posicao):
            #verifica se existe uma unidade nessa posicao
            adjacentes += (obter_unidade(mapa, posicao),)
    return ordenar_unidades(tuple(filter(lambda x: obter_exercito(x) != \
                                         obter_exercito(unidade), adjacentes)))
#filtra (remove) as unidades que sao do mesmo exercito, depois disto ordena-as

def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''
    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

#------------------------------------------------------------------------------#
###----------------------------Funcoes Adicionais----------------------------###
def calcula_pontos(mapa, e):
    '''
    calcula_pontos recebe um mapa e uma cadeia de caracteres correspondente ao nome
    de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao dum exercito e
    o total dos pontos de vida de todas as unidades do exercito.
    
    calcula_pontos: mapa x str -> int
    '''
    res = 0
    for u in obter_unidades_exercito(mapa, e):
        #soma a vida de cada uma das unidades do exercito e
        res += obter_vida(u)
    return res

def simula_turno(mapa):
    '''
    simula_turno modifica o mapa fornecido como argumento de acordo com a 
    simulacao  de um turno de batalha completo, e devolve o proprio mapa. 
    Isto e, seguindo a ordem de leitura do labirinto, cada unidade (viva) realiza 
    um unico movimento e (eventualmente) um ataque de acordo com as regras descritas.
    
    simula_turno: mapa -> mapa
    '''
    exercitoA = obter_nome_exercitos(mapa)[0] #nome do primeiro exercito (antes de alterar mapa)
    exercitoB = obter_nome_exercitos(mapa)[1] #nome do segundo exercito (antes de alterar mapa)
    #Nota - a criacao das variaveis anteriores serve para guardar os nomes dos exercitos antes que fiquem (possivelmente) vazios
    for unidade in obter_todas_unidades(mapa):
        #percorre todas as unidades do mapa
        if obter_unidades_exercito(mapa, exercitoA) != () and obter_unidades_exercito(mapa, exercitoB) != ():
            #unidade apenas se move para o seu objetivo se ambos os exercitos existirem, senao devolve mapa
            mapa = mover_unidade(mapa, unidade, obter_movimento(mapa, unidade))
            if eh_unidade(unidade) and obter_inimigos_adjacentes(mapa, unidade) != ():
                #se a unidade ainda existir e tiver inimigos adjacentes
                inimigo_a_atacar = obter_inimigos_adjacentes(mapa, unidade)[0]
                #ataca o primeiro inimigo adjacente (ordem de leitura)
                if unidade_ataca(unidade, inimigo_a_atacar):
                    eliminar_unidade(mapa, inimigo_a_atacar)
                    #elimina unidade se esta for destruida
    return mapa

def simula_batalha(ficheiro, boolean):
    '''
    simula_batalha permite simular uma batalha completa. A batalha termina quando
    um dos exercitos vence. A funcao simula batalha recebe uma cadeia de
    caracteres e um valor booleano e devolve o nome do exercito ganhador.
    A cadeia de caracteres passada por argumento corresponde ao ficheiro de conguracao do simulador. 
    O argumento booleano ativa o modo verboso (True) ou o modo quiet (False).
    
    simula_batalha -> str x booleano -> str
    '''
    #abre ficheiro, le e avalia cada uma das linhas
    t = open(ficheiro, 'r', encoding = 'UTF-8')
    d = eval(t.readline())
    e1 = eval(t.readline())
    e2 = eval(t.readline())
    w = eval(t.readline())    
    str_p_exercito1 = eval(t.readline())
    str_p_exercito2 = eval(t.readline())
    t.close() #fecha ficheiro
    
    exercito1 = ()
    exercito2 = ()
    
    for pos in str_p_exercito1:
        #cria o conjunto de unidades do exercito 1
        exercito1 += ((cria_unidade(cria_posicao(pos[0], pos[1]),\
                                 e1[1], e1[2], e1[0])),)
    for pos in str_p_exercito2:
        #cria o conjunto de unidades do exercito 2
        exercito2 += ((cria_unidade(cria_posicao(pos[0], pos[1]),\
                                 e2[1], e2[2], e2[0])),)
        
    mapa = cria_mapa(d, w, exercito1, exercito2) #cria mapa com parametros do ficheiro
    exercitoA = obter_nome_exercitos(mapa)[0] #nome do primeiro exercito (antes de alterar o mapa)
    exercitoB = obter_nome_exercitos(mapa)[1] #nome do segundo exercito (antes de alterar o mapa)
    
    
    print(mapa_para_str(mapa) + '\n'\
              + '[ ' + str(exercitoA) + ':' + str(calcula_pontos(mapa, exercitoA))\
              + ' '+ str(exercitoB) + ':' + str(calcula_pontos(mapa, exercitoB)) + ' ]')
    
    while calcula_pontos(mapa, exercitoA) != 0 and calcula_pontos(mapa, exercitoB) != 0:
        #enquanto nenhuma das equipas tiver 0 pontos
        mapa_anterior = cria_copia_mapa(mapa) #salva mapa anterior
        mapa = simula_turno(mapa) #simula turno do mapa
        
        if mapa == mapa_anterior: #se mapa for igual ao anterior, eh empate
            if not boolean: #para modo verboso
                print(mapa_para_str(mapa) + '\n'\
                      + '[ ' + str(exercitoA) + ':' + str(calcula_pontos(mapa, exercitoA))\
                      + ' '+ str(exercitoB) + ':' + str(calcula_pontos(mapa, exercitoB)) + ' ]') 
                return str('EMPATE')
            else: #para modo silencioso
                return str('EMPATE')
            
        else:
            if boolean or calcula_pontos(mapa, exercitoA) == 0 or calcula_pontos(mapa, exercitoB) == 0:
                #print mapa se chegar ao fim ou se modo verboso estiver ativo
                print(mapa_para_str(mapa) + '\n'\
                          + '[ ' + str(exercitoA) + ':' + str(calcula_pontos(mapa, exercitoA))\
                          + ' '+ str(exercitoB) + ':' + str(calcula_pontos(mapa, exercitoB)) + ' ]')     
              
    if calcula_pontos(mapa, exercitoA) > calcula_pontos(mapa, exercitoB):
        return exercitoA #mais pontos do exercitoA
    else:
        return exercitoB #mais pontos do exercitoA