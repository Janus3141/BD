
import sys


class ParseError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class Parser():
    def __init__(self,string):
        self.tokens = self.toTokens(string)
    
    def toTokens(self,string):
        parsed = []
        for char in string:
            if char.isspace():
                continue
            else:
                parsed.append(char)
        return parsed

    def head(self):
        self.tokens[0]

    def tail(self):
        self.tokens[1:]

    def parse_alpha(self):
        if (self.tokens[0]).isalpha():
            alpha = self.tokens[0]
            self.tokens = self.tokens[1:]
            return alpha
        else:
            err = "Se esperaba un caracter alfabetico"
            raise ParseError(err)

    def parse_many_alpha(self): # Al menos uno
        theset = set()
        theset.add(self.parse_alpha())
        while True:
            try:
                theset.add(self.parse_alpha())
            except ParseError:
                return theset

    def parse_char(self,char):
        if self.tokens[0] == char:
            self.tokens = self.tokens[1:]
        else:
            err = "Se esperaba '{0}'".format(char)
            raise ParseError(err)

    def parse_any_char(self,*args):
        for char in args:
            if self.tokens[0] == char:
                self.tokens = self.tokens[1:]
                return
        raise ParseError("Error sintactico")

    def parse_arrow(self):
        self.parse_char('-')
        self.parse_char('>')

    def parse_attrs(self):
        theset = set()
        self.parse_char('{')
        while True:
            theset.add(self.parse_alpha())
            try:
                self.parse_char(',')
            except ParseError:
                self.parse_char('}')
                return theset

    def parse_fds(self):
        theset = set()
        self.parse_char('{')
        while True:
            left = self.parse_many_alpha()
            self.parse_arrow()
            right = self.parse_many_alpha()
            theset.add((frozenset(left),frozenset(right)))
            try:
                self.parse_char(',')
            except ParseError:
                self.parse_char('}')
                return theset

    def parse_set(self):
        try:
            self.parse_char('R')
            self.parse_char('=')
            return ('R',self.parse_attrs())
        except ParseError:
            try:
                self.parse_char('F')
                self.parse_char('=')
                return ('F',self.parse_fds())
            except ParseError:
                self.parse_char('A')
                self.parse_char('=')
                return ('A',self.parse_attrs())

    def parse_all_set(self):
        a = self.parse_set()
        b = self.parse_set()
        try:
            self.parse_char(';')
            return [x for (y,x) in sorted([a,b], reverse=True)]
        except ParseError:
            c = self.parse_set()
            self.parse_char(';')
            return [x for (y,x) in sorted([a,b,c], reverse=True)]

    def parse(self):
        result = list()
        while len(self.tokens) != 0:
            result.append(self.parse_all_set())
        return result



def main():
    with open("test", mode='r') as thefile:
        contents = thefile.read()
    test = Parser(contents)
    parsed = test.parse()
    return parsed

