
import sys
import parser
import dependencies as deps

def main():
    try:
        thefile = sys.argv[1]
    except IndexError:
        print("Use: python3 main.py 'filename'")
        exit(1)
    with open(thefile, mode='r') as f:
        contents = f.read()
    test = parser.Parser(contents)
    parsed = test.parse()
    for (n,test) in enumerate(parsed,1):
        if len(test) == 3:
            a_closure = deps.attrs_closure(test[2],test[1])
        elif len(test) == 2:
            f_closure = deps.deps_closure(test[0],test[1])
        cand_keys = deps.keys(test[0],test[1])
        print("Set {}:".format(n))
        print("R: {}".format(test[0]))
        print_deps(test[1])
        if len(test) == 3:
            print("A: {}".format(test[2]))
            print("A+: {}".format(a_closure))
        elif len(test) == 2:
            print("Cardinality(F+): {}".format(len(f_closure)))
        print_keys(cand_keys)
        print("")


def print_deps(d):
    string = "{"
    for (alfa,beta) in d:
        string = string + "".join(alfa) + '->' + "".join(beta) + ", "
    string = string[:-2] + "}"
    print("F: " + string)

def print_keys(k):
    string = ""
    for key in k:
        string = string + "{" + ", ".join(key) + "} "
    print("Candidate keys: " + string)

if __name__ == '__main__':
    main() 
    
