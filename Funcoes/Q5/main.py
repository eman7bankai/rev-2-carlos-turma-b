altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

def imc(altura, peso):
    return (peso/(altura*2))

resultado_imc = imc(altura, peso)

def classificacao(resultado_imc):
    if resultado_imc < 18.5:
        return "Abaixo do peso"
    elif resultado_imc >= 18.5 and resultado_imc <= 24.9:
        return "Peso normal"
    else:
        return "Acima do peso"
    
resultado_classificacao = classificacao(resultado_imc)
print(resultado_classificacao)