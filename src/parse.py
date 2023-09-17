from error import Error

from AdvancedFunctions.systemfunctions.clean import CleanSystemFunction
from AdvancedFunctions.systemfunctions.exit import ExitSystemFunction

class Parser:
    def __init__(self, code: str):
        self.code = code

        self.code = self.parse(self.code)

    def parse(self, code: str) -> str:
        code = self.parseComments(code)
        code = self.CLSFfunction(code)
        code = self.INPUTfunction(code)
        code = self.PRINTFunction(code)
        code = self.EXITFunction(code)

        with open("output.py", "w") as f:
            f.write(code)

        return str(code)
    
    def parseComments(self, code:str) -> str:

        # COMMENTS, usage: ' example
        for line in code.splitlines():
            if "'" in line:
                if not self.isInString("'", line):
                    newLine = line.replace("'", "#")
                    code = code.replace(line, newLine)

        return code
    
    def CLSFfunction(self, code: str) -> str:
        # SYSTEM CLS FUNCTION, usage: CLS
        for line in code.splitlines():
            if "CLS" in line:
                if not self.isInString("CLS", line):
                    clsPython = CleanSystemFunction()
                    code = code.replace(line, str(clsPython))
        return code
    
    def INPUTfunction(self, code: str):
        # SYSTEM INPUT FUNCTION, usage: INPUT " Enter your name" name
        for line in code.splitlines():
            words = line.split()
            INPUTText = ""

            for wordNo, word in enumerate(words):
                if words[wordNo] == "INPUT" and not self.isInString(words[wordNo], line):
                    if words[wordNo + 1].startswith('"'):
                        def getinputmsg(lista):
                                contenido = []
                                in_quotes = False
                                for elemento in lista:
                                    if '"' in elemento:
                                        if not in_quotes:
                                            contenido.append(elemento)
                                            in_quotes = True
                                        else:
                                            contenido[-1] += ' ' + elemento
                                            in_quotes = False
                                    elif in_quotes:
                                        contenido[-1] += ' ' + elemento

                                return ' '.join(contenido)
                        
                        INPUTText = getinputmsg(words)
                        variableToAdd = words[-1]
                        
                        newLine = f"{variableToAdd} = input({INPUTText})"
                        
                        words = newLine
                        code = code.replace(line, newLine)

        return code
    
    def PRINTFunction(self, code:str) -> str:
        for line in code.splitlines():
            words = line.split()
            printtext = ""

            for wordNo, word in enumerate(words):
                if words[wordNo] == "PRINT" and not self.isInString(words[wordNo], line):
                    def getprintmsg(lista):
                        contenido = []
                        del lista[0]
                        for elemento in lista:
                            contenido.append(elemento)

                        return ' '.join(contenido)

                    printtext = getprintmsg(words)
                    newLine = f"print({printtext})"
                    words = newLine
                    code = code.replace(line, newLine)

        return code
    
    def EXITFunction(self, code:str) -> str:
        for line in code.splitlines():
            if "EXIT" in line and not self.isInString("EXIT", line):
                exitfn = ExitSystemFunction()
                code  = code.replace(line, str(exitfn))

        return code

    def isInString(self, phrase : str, line : str, returnIfMultiple = False) -> bool:
        # thanks chadderbox

        if not phrase in line:
            return False
        if line.count(phrase) > 1:
            return returnIfMultiple
        leftSide = line.partition(phrase)[0]
        if leftSide.count("\"") > 0:
            if leftSide.count("\"") % 2 == 0:
                return False
            else:
                return True