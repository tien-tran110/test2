from lex import *
from display import *
from rda import *

def __init__(self):
    self.f = open('text.txt', 'r')
    self.data = self.f.read()
    self.analyzer = lexer(self.data)
    print(self.analyzer)