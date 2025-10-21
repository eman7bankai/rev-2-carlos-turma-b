preco_produto = float(input("Digite o preço do produto:"))

def desconto(preco_produto):
    return preco_produto - (preco_produto*(10/100))

resultado = desconto(preco_produto)

print(f"O valor ficou {resultado}")