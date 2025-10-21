email = input("Digite seu email:").lower()
senha = input("Digite sua senha:").lower()

def confirmacao_indentidade(email,senha):
    if email == "admin" and senha == "admin":
        return "Logado com sucesso!"
    else:
        return "email ou senha incorreto!"
    
confirmacao = confirmacao_indentidade(email,senha)
print(confirmacao)