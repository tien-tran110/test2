
#Error

ERROR_TYPES = {
        'IllegalCharError'      : 'Illegal Character',
        'ExpectedCharError'     : 'Expected Character',
        'InvalidSyntaxError'    : 'Expected Character',
    }

class error:
    def __init__(self, err_name, info, pos):
        self.err_name = err_name
        self.info = info
        self.pos = pos
    
    def to_string(self):
        result = f'{self.err_name}: {self.info}\n'
        return result
    
#Token
class Token:
	def __init__(self, type_, value=None):
		self.type = type_
		self.value = value
	

	def __repr__(self):
		if self.value: return f'{self.type}:{self.value}'
		return f'{self.type}'


