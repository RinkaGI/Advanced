class CleanSystemFunction:
    def __init__(self):
        import os
        if os.name == 'nt': 
            os.system('cls')
        else: 
            os.system('clear')

    def __str__(self):
        return "import os \nif os.name == 'nt':\n     os.system('cls')\nelse:\n    os.system('clear')"