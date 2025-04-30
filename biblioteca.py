
def imprimenome(nome):
    print(f"Nome: {nome}")

def solicitarnome():
    nome=input("Digite seu nome: ")
    return nome
def piramide(num):
    for x in range (1,num+1,1):
        for i in range (0,x):
            print(x,end=" ")
        print()

def contavogais(texto):
    vogais = "aeiouAEIOU"
    cont=0
    for x in range(len(texto)):
        if texto[x] in vogais:
            cont = cont + 1
    print(cont)

def estoque(produto, qtd, valorunitario):
    valortotal = qtd * valorunitario
    return valortotal

def numero(num):
    if num!=0:
        if num>0:
            return "P"
        else:
            return "N"
    else:
        return "Z"

def soma(a,b):
    resultado=a+b
    print(resultado)

def soma(*a):
    soma=0
    for x in range(len(a)):
        soma=soma+a[x]
    print(soma)


