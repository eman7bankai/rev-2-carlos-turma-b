idade = int(input("Digite sua idade:"))

def verificacao_idade(idade):
    if idade >= 18:
        return "Maior idade"
    else:
        return "Menor de idade"
    
resultado = verificacao_idade(idade)
print({resultado})