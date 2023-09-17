from utils.tokens import *
from utils.constants import DIGITS
from utils.errors import *
from utils.position import *

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.currentChar = None
        self.advance()

    def advance(self):
        self.pos.advance(self.currentChar)
        self.currentChar = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def makeNumber(self):
        numStr = ''
        dotCount = 0

        while self.currentChar is not None and self.currentChar in DIGITS + '.':
            if self.currentChar == '.':
                if dotCount == 1:
                    break

                dotCount += 1
                numStr += '.'
            else:
                numStr += self.currentChar

            self.advance()

        if dotCount == 0:
            return Token(TT_INT, int(numStr))
        else:
            return Token(TT_FLOAT, float(numStr))

    def makeToken(self):
        tokens = []

        while self.currentChar is not None:
            if self.currentChar in ' \t':
                self.advance()
            elif self.currentChar in DIGITS:
                tokens.append(self.makeNumber())
                # self.advance()
            elif self.currentChar == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.currentChar == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.currentChar == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.currentChar == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.currentChar == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.currentChar == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()

            else:
                posStart = self.pos.copy()
                char = self.currentChar
                self.advance()
                return [], IllegalCharError(posStart, self.pos, f'"{char}"')


        return tokens, None
    
def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.makeToken()

    return tokens, error