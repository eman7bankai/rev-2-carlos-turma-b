retorno = 0

while retorno == 0:
    try:  
        divisor = float(input("Digiteo número para ser dividido:"))
        dividendo = float(input("para quanto será dividido?"))

        resultado = divisor/dividendo
        print(resultado)

    except ZeroDivisionError:
        print("O dividendo nao pode ser 0!")
        retorno = 0

    except ValueError:
        print("Deve ser um número!")
        retorno = 0

