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


def deps_closure(attrs, deps): # attrs :: Set, deps :: Set

    # Reflexividad
    resultado = deps
    for alfa in powerset(attrs):
        alfaset = frozenset(alfa)
        ps = powerset(alfaset)
        for subset in ps:
            resultado.add((alfaset,frozenset(subset)))

    # Aumentatividad
    aumento = set()
    while True:
        for (alfa,beta) in resultado:
            for gamma in powerset(attrs):
                gamma = set(gamma)
                aumento.add((alfa.union(gamma), beta.union(gamma)))
        if aumento.union(resultado) == resultado:
            break
        else:
            resultado = resultado.union(aumento)

    # Transitividad
    transitivos = set()
    while True:
        for (alfa,beta) in resultado:
            for (gamma,eta) in resultado:
                if beta == gamma:
                    transitivos.add((alfa,eta))
        if transitivos.union(resultado) == resultado:
            break
        else:
            resultado = resultado.union(transitivos)

    return resultado




# resultado := alfa;
# while (hay cambios en resultado) do
# for each dependencia funcional b → c in F do
# if b ⊆ resultado then
# resultado := resultado ∪ c;
# return resultado;

def attrs_closure(attrs,parsed): # attrs :: Set
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




