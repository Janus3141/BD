#
#resultado := F;
#for each alfa in P(R) do
#    aplicar las reglas de reflexividad a alfa;
#    a~nadir las nuevas DF obtenidas a resultado;
#while (hay cambios en resultado) do
#    for each DF f in resultado do
#        aplicar las reglas de aumentatividad a f;
#        a~nadir las nuevas DF obtenidas a resultado;
#for each DF f1 in resultado do
#    for each DF f2 in resultado do
#        if f1 y f2 pueden combinarse por transitividad then
#            a~nadir la nueva DF a resultado;
#return resultado
#

#parsed = ( R, DF = {(a,b)} )

from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(1,len(s)+1))


def reflex(alfa):
    alfa = frozenset(alfa)
    ps = powerset(alfa)
    resultado = set()
    for i in ps:
        resultado.add((alfa,frozenset(i)))
    return resultado

def dfs(parsed):
    resultado = parsed[1]
    for alfa in powerset(parsed[0]):
        resultado = resultado.union(reflex(alfa))
    aumento = set()
    for (alfa,beta) in resultado:
        flag = True
        for gamma in powerset(parsed[0]):
            gamma = set(gamma)
            aumento.add((alfa.union(gamma), beta.union(gamma)))
        if aumento.union(resultado) == resultado:
            break
        else:
            resultado = resultado.union(aumento)
    for (alfa,beta) in resultado:
        transitivos = set()
        for (gamma,theta) in resultado:
            if beta == gamma:
                transitivos.add((alfa,theta))
                resultado = resultado.union(transitivos)
        # resultado = resultado.union(transitivos)
    return resultado




# resultado := alfa;
# while (hay cambios en resultado) do
# for each dependencia funcional b → c in F do
# if b ⊆ resultado then
# resultado := resultado ∪ c;
# return resultado;

def cierre(attrs,parsed): # attrs :: Set
    resultado = attrs
    agregados = attrs
    while True:
        for (alfa,beta) in parsed[1]:
            if alfa.issubset(resultado):
                agregados = agregados.union(beta)
        if agregados == resultado:
            break
        else:
            resultado = agregados
            continue
    return resultado


def claves(parsed):
    resultado = set()
    candidatas = list(parsed[0])
    for s in candidatas:
        flag = True
        for elem in s:
            if cierre(s.remove(elem), parsed) == parsed[0]:
                flag = False
                candidatas.append(s)
            s.add(elem)
        if flag:
            resultado.add(tuple(s))
    return resultado




