class ExitSystemFunction:
    def __init__(self):
        import sys
        sys.exit(0)
    def __str__(self):
        return "import sys\nsys.exit(0)"