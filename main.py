print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

try:
    idade = int(input ("Qual é a sua idade?"))
    if idade < 30:
        print(f"É o/a {nome} e tem menos de 30 anos.")
    else:
        print(f"É o/a {nome} e tem mais de 30 anos.")
except ValueError:
    print("Erro! Introduza um valor válido da idade!")
    