name = input("Insira seu nome ")
age = int(input("Insira sua idade "))
print(f"Olá {name} como vai? {f"você tem {age} anos de idade e está apto para o mercado de trabalho" if age >= 18 else "você é de menor, portanto não pode trabalhar"}" )
nacionalidade = input("Insira sua nacionalidade ")

if nacionalidade == "Brasileiro":
    print(f"Que bacana {name}, você é {nacionalidade}, muito legal.")
elif nacionalidade == "Português":
    print(f"Que legal {name}, você é {nacionalidade}, muito interessante.")
else :
    print(f"Legal {name}, você é {nacionalidade}, interessante.")