from parse import Parser
from error import Error
import os.path, subprocess, sys, shutil

def runPython(code:str):
    subprocess.call([
        "python", "output.py"
    ])

def getCode(filePath) -> str:
    if os.path.isfile(filePath):
        with open(filePath, 'r') as file:
            return file.read()
    else:
        Error("ADVANCED INTERPRETER: File to run was not found.")

def handleArgs():
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print('''
        ADVANCED COMMAND LINE ARGS:
            --help -h : Prints this message
            --version -v : Prints version installed of ADVANCED
            --run -r (default command) [advanced file] : Run ADVANCED program.
            --transpile -t [advanced file] [python file] : Converts ADVANCED to python and saves it
        ''')

    elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
        print("ADVANCED prototype first development")

    elif sys.argv[1] == "--run" or sys.argv[1] == "-r":
        if len(sys.argv) < 3:
            Error("ADVANCED INTERPRETER: Invalid number of args")
        else: 
            if os.path.isfile(sys.argv[2]):
                parser = Parser(getCode((sys.argv[2])))
                runPython(parser.code)
                os.remove("output.py")
            else:
                Error("ADVANCED INTERPRETER: File not found")

    #this shit maybe confusing, just for making --run default and not compulsory to write --run
    elif os.path.isfile(sys.argv[1]):   
        parser = Parser(getCode((sys.argv[1])))
        runPython(parser.code)
        os.remove("output.py")

    elif sys.argv[1] == "--transpile" or sys.argv[1] == "-t":
        if len(sys.argv) < 4:
            Error("ADVANCED INTERPRETER: Invalid number of args")
        else:
            if os.path.isfile(sys.argv[2]):
                parser = Parser(getCode((sys.argv[2])))

                with open(sys.argv[3], "w") as f:
                    f.write(parser.code)

                    os.remove("output.py")
            else:
                Error("ADVANCED INTERPRETER: File not found")

if __name__ == '__main__':
    handleArgs()