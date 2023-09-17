import lexer
while True:
    text = input("Advanced> ")
    result, error = lexer.run('<stdn>', text)

    if error:
        print(error.asString())
    else:
        print(result)