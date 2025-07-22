print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome?\n")
print(f"\nOlá, {nome}!")
while True:
    try:
        idade = int(input ("\nQual é a sua idade?\n"))
        if 0 <= idade < 30:
            print(f"\nÉ o/a {nome} e tem menos de 30 anos.")
            break
        elif idade == 30:
            print(f"\nÉ o/a {nome} e tem 30 anos.")
            break
        elif idade < 0:
            print("Erro! A sua idade não pode ser negativa!")
        else:
            print(f"\nÉ o/a {nome} e tem mais de 30 anos.")
            break
    except ValueError:
        print("Erro! Introduza um valor válido da idade!")
        