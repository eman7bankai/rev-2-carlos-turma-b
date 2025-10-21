preco_produto = float(input("Digite o valor do produto:"))

def imposto(preco_produto):
    return (preco_produto + (preco_produto * (15/100)))

resultado_imposto = imposto(preco_produto)
print(resultado_imposto)