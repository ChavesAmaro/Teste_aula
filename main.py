print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
while True:
    try:
        idade = int(input ("Qual é a sua idade?"))
        if 0 <= idade < 30:
            print(f"É o/a {nome} e tem menos de 30 anos.")
            break
        elif idade == 30:
            print(f"É o/a {nome} e tem 30 anos.")
            break
        elif idade < 0:
            print("Erro! A sua idade não pode ser negativa!")
        else:
            print(f"É o/a {nome} e tem mais de 30 anos.")
            break
    except ValueError:
        print("Erro! Introduza um valor válido da idade!")
        