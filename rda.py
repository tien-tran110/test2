'''
<stmt> --> <ifstmt> | <while_loop> | <as_s> | <declaration> | <block>
<block> --> START <stmt> `;` FINISH
<if_stmt> --> SELECT <boolexpr> START <stmt> FINISH 
<while_loop> --> LOOP <boolexpr> START <stmt> FINISH
<ident> --> [_a-zA-Z]{6,8}
<as_s> --> 'id' `=` <expr>
<declaration> --> <dtype> 'id' `;`
<dtype> --> {TX, TY, TZ, TT}
<expr> --> <term> { (`+`|`-`) <term> }
<term> --> <factor> { (`*`|`/`|`%`) <factor> }
<factor> --> 'id' | `(` <expr> `)`
'''


class RDA:
  def __init__(self, tokens: list(str)) -> None:
    self.tokens = tokens
    self.current = 0
    self.currentToken = tokens[self.current]

  def getNextToken(self):
    if self.current < len(self.tokens):
      self.current += 1
      self.currentToken = self.tokens[self.current]

  def stmt(self):
    #<stmt> --> <ifstmt> | <while_loop> | <as_s> | <declaration> | <block>
    match self.currentToken:
      case 'SELECT':
        self.if_stmt()
        
      case 'LOOP':
        self.while_loop()
        
      case 'id':
        self.as_s()
        
      case 'START':
        self.block()
        
      case _:
        self.error()
        
  def block(self):
    #<block> --> START <stmt> FINISH
    if self.currentToken == 'START':
      self.getNextToken()
      self.stmt()
      if self.currentToken == 'FINISH':
        self.getNextToken()
      else:
        self.error()
    else: 
      self.error()
      

  def if_stmt(self):
    #<if_stmt> --> SELECT <boolexpr> START <stmt> FINISH 
    if self.currentToken == 'SELECT':
      self.getNextToken()
      self.boolexpr()
      if self.currentToken == 'START':
        self.getNextToken()
        self.stmt()
        if self.currentToken == 'FINISH':
          self.getNextToken()
        else:
          self.error()
      else:
        self.error()
    else:
      self.error()
        

  def while_loop(self):
    #<while_loop> --> LOOP <boolexpr> START <stmt> FINISH
    if self.currentToken == 'LOOP':
      self.getNextToken()
      self.boolexpr()
      if self.currentToken == 'START':
        self.getNextToken()
        self.stmt()
        if self.currentToken == 'FINISH':
          self.getNextToken()
        else:
          self.error()
      else:
        self.error()
    else:
      self.error()

  def as_s(self):
    #<as_s> --> 'id' `=` <expr>
    if self.currentToken == 'id':
      self.getNextToken()
      if self.curentToken == '=':
        self.getNextToken()
        self.expr()
      else:
        self.error()

    else:
      self.error()

  def expr(self):
    #<expr> --> <term> { (`+`|`-`) <term> }
    self.term()
    while self.currentToken == '+' or self.currentToken == '-':
      self.getNextToken()
      self.term()

  def term(self):
    #<term> --> <factor> { (`*`|`/`|`%`) <factor> }
    self.factor()
    while self.currentToken == '*' or self.currentToken == '/'\
    or self.currentToken == '%':
      self.getNextToken()
      self.factor()

  def boolexpr(self):
    pass

  def factor(self):
  #<factor> --> 'id' | `(` <expr> `)`
    if self.currentToken == 'id':
      self.getNextToken()

    elif self.currentToken == '(':
      self.getNextToken()
      self.expr()
      if self.currentToken == ')':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()

  def error():
    pass