try:
    divisor = float(input("Digiteo número para ser dividido:"))
    dividendo = float(input("para quanto será dividido?"))

    def divisao(divisor, dividendo):
        return divisor/dividendo

    resultado = divisao(divisor, dividendo)
    print(resultado)

except ZeroDivisionError:
    print("O dividendo nao pode ser 0!")

except ValueError:
    print("Deve ser um número!")