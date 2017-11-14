
from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(1,len(s)+1))



def deps_closure(attrs, deps):

    # Reflexividad
    resultado = deps.copy()
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



def attrs_closure(attrs,deps):
    resultado = attrs.copy()
    agregados = attrs.copy()
    while True:
        for (alfa,beta) in deps:
            if alfa.issubset(resultado):
                agregados = agregados.union(beta)
        if agregados == resultado:
            break
        else:
            resultado = agregados
            continue
    return resultado


def keys(attrs, deps):
    resultado = set()
    for subset in powerset(attrs):
        fsubset = frozenset(subset)
        if attrs_closure(fsubset,deps) == attrs:
            for candidate in resultado:
                if candidate.issubset(fsubset):
                    break
            else:
                resultado.add(fsubset)
    return resultado


