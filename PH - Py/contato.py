import re


def validar_email(email):
    # Regex para verificar o formato do email
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False


def coletar_dados():
    nome = input("Digite seu nome: ").strip()
    while not nome:
        print("O nome não pode estar vazio.")
        nome = input("Digite seu nome: ").strip()

    email = input("Digite seu email: ").strip()
    while not email or not validar_email(email):
        if not email:
            print("O email não pode estar vazio.")
        else:
            print("Formato de email inválido.")
        email = input("Digite seu email: ").strip()

    mensagem = input("Escreva sua mensagem: ").strip()
    while not mensagem:
        print("A mensagem não pode estar vazia.")
        mensagem = input("Escreva sua mensagem: ").strip()

    return nome, email, mensagem


nome, email, mensagem = coletar_dados()
print(f"Obrigado pelo contato, {nome}! Estaremos entrando em contato em breve!")
