from error import Error

class Parser:
    def __init__(self, code: str):
        self.code = code

        self.code = self.parse(self.code)

    def parse(self, code: str) -> str:
        code = self.parseComments(code)

        with open("output.py", "w") as f:
            f.write(code)

        return str(code)
    
    def parseComments(self, code:str) -> str:
        for line in code.splitlines():
            if "'" in line:
                if not self.isInString("'", line):
                    newLine = line.replace("'", "#")
                    code = code.replace(line, newLine)

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
        if leftSide.count("\'") > 0:
            if leftSide.count("\'") % 2 == 0:
                return False
            else:
                return True