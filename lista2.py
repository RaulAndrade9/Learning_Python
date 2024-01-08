def ler_numeros(numeros):
    for i in range(0, len(numeros)):
        print(numeros[i])

def lista_reversa(lista):
    reverso = list(reversed(lista))
    print(reverso)


def notas(notas):
    media = sum(notas) / len(notas)
    print(media)

def consoantes(lista_letras):
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista_consoantes = []


    for i in range(0, len(lista_letras)):
        if lista_letras[i] not in vogais:
            consoante = lista_letras[i]
            lista_consoantes.append(consoante)

    print("Número de consoantes: {}" .format(len(lista_consoantes)))
    print("Consoantes encontradas? {}" .format(lista_consoantes))

def vetor_numeros():
    total_numeros = []
    impar = []
    par = []
    for i in range(0, 10):
        numero = int(input("Digite um número"))
        total_numeros.append(numero)
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

    print("Numeros: {}" .format(total_numeros))
    print("Impar: {}" .format(impar))
    print("Par: {}" .format(par))

def notas_alunos():
    medias = []
    for i in range(0, 4):
        notas = []
        for i in range(0, 4):
            nota_aluno = float(input("Digite a nota"))
            notas.append(nota_aluno)
        media = sum(notas) / 4
        medias.append(media)
        

    maior_que_7 = [numero for numero in medias if numero >= 7]
    print("Médias maior que 7: {}" .format(maior_que_7))
    
def vetor_5_numeros():      
    lista = []
    for i in range(0, 5):
        numero = int(input("Digite um número"))
        lista.append(numero)
    
    soma = sum(lista)
    mult = lista[0]
    for i in range (1, len(lista)):
        mult = mult * lista[i]
    
    print("A lista é: {}\nA soma dos números é: {}\nA multiplicação dos números é: {}" .format(lista, soma, mult))

def idade_altura(num_pessoas):
    lista_idade= []
    lista_altura = []

    for i in range(0, num_pessoas):
        idade = int(input("Digite a idade da pessoa"))
        altura = float(input("Digite a altura da pessoa"))
        lista_altura.append(altura)
        lista_idade.append(idade)
    
    idade_reverso = list(reversed(lista_idade))
    altura_reverso = list(reversed(lista_altura))

    print(idade_reverso)
    print(altura_reverso)


def quadrado_numeros():
    lista_numeros = []
    lista_numeros_quadrado = []
    for i in range(0, 5):
        numero = int(input("Digite um número"))
        lista_numeros.append(numero)
        quadrado = numero * numero
        lista_numeros_quadrado.append(quadrado)
    
    print(lista_numeros_quadrado)



if (__name__ == "__main__"):
    quadrado_numeros()
    