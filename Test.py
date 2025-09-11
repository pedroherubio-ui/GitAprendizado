#name = input("Insira seu nome ")
#age = int(input("Insira sua idade "))
#print(f"Olá {name} como vai? {f"você tem {age} anos de idade e está apto para o mercado de trabalho" if age >= 18 else "você é de menor, portanto não pode trabalhar"}" )
#nacionalidade = input("Insira sua nacionalidade ")

#if nacionalidade == "Brasileiro":
   # print(f"Que bacana {name}, você é {nacionalidade}, muito legal.")
#elif nacionalidade == "Português":
   # print(f"Que legal {name}, você é {nacionalidade}, muito interessante.")
#else :
    #print(f"Legal {name}, você é {nacionalidade}, interessante.")

try:

    num1 = (int(input(f"Você quer começar com quanto?")))

    num2 = (int(input(f"Você quer contar até quanto?")))

    print("INCIANDO WHILE")

    while num1 < num2:
        print(num1) 
        num1 += 1


    print ("TROCANDO PARA FOR IN RANGE")

    for num1 in range(num2):
        print(num1)

except: 
    print("Valor inserido inválido, insira um numero valido")
finally:
    print("")



#frutas = {"maçã", "banana", "laranja", "maçã"}  
#print(frutas)

#Lista com {} é uma lista desordenada imutavel

#aluno = {
    #"nome": "Pedro",
    #"idade": 21,
    #"curso": "ADS"
#} Coleção de pares {:}