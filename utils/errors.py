class Error:
    def __init__(self, posStart, posEnd, errorName, details):
        self.posStart = posStart
        self.posEnd = posEnd
        self.errorName = errorName
        self.details = details

    def asString(self):
        result = f'{self.errorName}: {self.details}'
        result += f'File {self.posStart.fn}, line {self.posStart.ln +1}'
        return result
    
class IllegalCharError(Error):
    def __init__(self, posStart, posEnd, details):
        super().__init__(posStart, posEnd, 'Illegal Character', details)