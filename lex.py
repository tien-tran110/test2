import string
from display import *
DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS
#list of tokens
KEYWORD = 'KEYWORD'
ID = 'ID'
STRING = 'STRING'
PLUS = '+'
MINUS = '-'
MUL = '*'
DIV = '/'
MOD = '%'
LPARENT = '('
RPARENT = ')'
LCURLB = '{'
RCURLB = '}'
SEMICOLON = ';'
EQ = '='
NE = '!='
EE = '=='
LT = '<'
GT = '>'
LTE = '<='
GTE = '>='


#list of keywords
KEYWORDS = [ 
	'START',
  'FINISH',
  'LOOP',
  'IDENT',
  'SELECT'
]
#lexer anyalyzer
class lexer:
    def __init__(self,text):
        self.text = text
        self.position = -1
        self.current_char = None
        self.to_next_char()
        self.tokens = self.list_tokens()


    def to_next_char(self):
        self.position += 1
        if self.position < len(self.text):
             self.current_char = self.text[self.position]
        else:
            self.current_char = None

    def list_tokens(self):
        tokens = []
      
        while self.current_char != None:
            if self.current_char in LETTERS:
                tokens.append(self.make_identifier())

            match self.current_char:
                case ' '|'\t'|'\n':
                    self.to_next_char()
                case '#':
                    self.skip_comment()
                case ';':
                    tokens.append(Token(SEMICOLON))
                    self.to_next_char()
                case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
                    tokens.append(self.tokenize_number())                   
                    self.to_next_char()
                case '"':
                    tokens.append(self.tokenize_string)
                case '+':
                    tokens.append(Token(PLUS))
                    self.to_next_char()
                case '-':
                    tokens.append(Token(MINUS))
                    self.to_next_char()
                case '*':
                    tokens.append(Token(MUL))
                    self.to_next_char()
                case '/':
                    tokens.append(Token(DIV))
                    self.to_next_char()
                case '(':
                    tokens.append(Token(LPARENT))
                    self.to_next_char()
                case ')':
                    tokens.append(Token(RPARENT))
                    self.to_next_char()
                case '!':
                    token, possible_error = self.tokenize_NE()
                    if possible_error:
                        return [], possible_error
                    tokens.append(token)
                case '=':
                    tokens.append(self.EQ_or_ASS())
                case '<':
                    tokens.append(self.LT_or_LTE())
                case '>':
                    tokens.append(self.GT_or_GTE())
                case _:
                    char = self.current_char
                    self.to_next_char()
                    e = error('Illegal Character Error', str("'"+str(char)+"'"), self.position)
                    print('Error: ', e.err_name, ': ', char,'at position: ',e.pos)
                    return tokens, e
        
        return tokens, None

    def tokenize_number(self):
        number = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS:
            number += self.current_char
            self.to_next_char()
        
        return Token(DIGITS)

    def tokenize_string(self):
        string = ''
        start_pos = self.pos.copy()
        is_escape_character = False
        self.to_next_char()

        escape_characters = {
            'n': '\n',
            't': '\t'
        }

        while self.current_char != None and (self.current_char != '"' or is_escape_character):
            if is_escape_character:
                string += escape_characters.get(self.current_char, self.current_char)
            else:
                if self.current_char == '\\':
                    is_escape_character = True
                else:
                    string += self.current_char
            self.to_next_char()
            is_escape_character = False
    
        self.to_next_char()
        return Token(STRING, string)

    def make_identifier(self):
        id = ''

        while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
            id += self.current_char
            self.to_next_char()

        token_type = KEYWORD if id in KEYWORDS else ID
        return Token(token_type, id)
 
    def tokenize_NE(self):

        start_pos = self.pos.copy()
        self.to_next_char()

        if self.current_char == '=':
            self.to_next_char()
            return Token(NE), None

        self.to_next_char()
        return None, error('ExpectedCharError', "'=' (after '!')")

    def EQ_or_ASS(self):
        tok_type = EQ
        self.to_next_char()

        if self.current_char == '=':
            self.to_next_char()
            tok_type = EE

        return Token(tok_type)
    

    def LT_or_LTE(self):
        tok_type = LT
        self.to_next_char()

        if self.current_char == '=':
            self.to_next_char()
            tok_type = LTE

        return Token(tok_type)


    def GT_or_GTE(self):
        tok_type = GT
        self.to_next_char()

        if self.current_char == '=':
            self.to_next_char()
            tok_type = GTE

        return Token(tok_type)

    def skip_comment(self):
        self.to_next_char()

        while self.current_char != '\n':
            self.to_next_char()

        self.to_next_char()
