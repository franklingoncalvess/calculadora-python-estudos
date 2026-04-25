nome = input("Nome: ")
idade = int(input("Qual sua idade? ")) # O int() transforma o texto em numero

if idade >= 18:
    print(f"Bem-vindo, {nome}. Voce ja pode ter acesso root (total) ao sistema!")
else:
    print(f"Ola {nome}. Voce ainda e um Padawan, acesso restrito.")

# Isso é uma CONDICIONAL (o famoso IF/ELSE)