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

def vetores_intercalados():
    vetor1 = []
    vetor2 = []
    vetor3 = []

    for i in range(0, 10):
        numero = int(input("Digite um número"))
        vetor1.append(numero)

    for i in range(0, 10):
        numero = int(input("Digite um número"))
        vetor2.append(numero)

    for i in range(0, 10):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])

    print(vetor3)

def vetores_intercalados3():
    vetor1 = []
    vetor2 = []
    vetor3 = []
    vetor4 = []

    for i in range(0, 10):
        numero = int(input("Digite um número"))
        vetor1.append(numero)

    for i in range(0, 10):
        numero = int(input("Digite um número"))
        vetor2.append(numero)

    for i in range(0, 10):
        numero = int(input("Digite um número"))
        vetor3.append(numero)

    for i in range(0, 10):
        vetor4.append(vetor1[i])
        vetor4.append(vetor2[i])
        vetor4.append(vetor3[i])

    print(vetor4)

def altura_idade():
    lista_altura = []
    lista_idade = []
    lista_medias = []


    for i in range(0, 5):
        altura = float(input("Digite a altura "))
        idade = int(input("Digite a idade"))
        lista_altura.append(altura)
        lista_idade.append(idade)
    
    media_altura = sum(lista_altura) / len(lista_altura)
    for i in range(0, len(lista_altura)):
        if lista_altura[i] <= media_altura and lista_idade[i] >=13:
            medias = lista_altura[i]
            lista_medias.append(medias)
    print("Numero de alunos com +13 que estão abaixo da média: {}" .format(len(lista_medias)))

def temperaturas():
    lista_temperatura = [27, 26, 26, 24, 23, 22, 20, 18, 20, 22, 24, 25]
    lista_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    lista_meses_media_temp = []
    media = sum(lista_temperatura) / len(lista_temperatura)
    print(media)

    for i in range(0, len(lista_temperatura)):
        if lista_temperatura[i] >= media:
            media_temp = lista_mes[i]
            lista_meses_media_temp.append(media_temp)
    
    for i in range(1, len(lista_meses_media_temp) + 1):
            print("{} {}" .format(i, lista_meses_media_temp[i]))

def crime():
    lista_classificacao = []
    lista_perguntas = ['Telefonou para a vítima?','Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?' ]
    for i in range(0, len(lista_perguntas)):
        print(lista_perguntas[i])
        resposta = int(input("Sim(1) ou Não(0)"))
        lista_classificacao.append(resposta)

    classificacao = sum(lista_classificacao)
    print(classificacao)

    if classificacao == 0:
        print("inocente")
    elif classificacao <= 2:
        print("Suspeito")
    elif classificacao <= 4:
        print("Cúmplice")
    else:
        print("Culpado")

def qtd_notas():              
    prosseguir = 0
    lista_notas = []
    acima = []
    abaixo = []
    while prosseguir >= 0:
        notas = float(input("Digite a nota"))
        lista_notas.append(notas)
        prosseguir = int(input("Deseja adcionar notas? "))

    qtd_valores_lidos = len(lista_notas)

    reverso = list(reversed(lista_notas))
    for numero in reverso:
        print(numero)

    media = sum(lista_notas) / len(lista_notas)

    for numero in lista_notas:
        if numero >= media:
            acima_media = numero
            acima.append(acima_media)
    qtde_acima_da_media = len(acima)

    for numero in lista_notas:
        if numero < 7:
            abaixo_7 = numero
            abaixo.append(abaixo_7)
    qtde_abaixo_7 = len(abaixo)

    soma = sum(lista_notas)

    print('Quantidade de valores lidos = {}'.format(qtd_valores_lidos))

    for numero in lista_notas:
        print(numero, end=' ')

    for numero in lista_notas:
        print(numero)

    print('soma dos valores: {}' .format(soma))
    print('A média é: {}' .format(media))
    print('Qtde de valores acima da media: {}' .format(qtde_acima_da_media))
    print('Qtde abaixo de sete: {}' .format(qtde_abaixo_7))
    print('Fim do programa')

def salarios(vendas):
    lista_salarios = []
    min = 200
    max = 299

    salario = 200 + (vendas * 0.09)

    for i in range(0, 9):
        lista_salarios.append([min, max])
        min += 100
        max += 100

    for i, intervalo in enumerate(lista_salarios):
        if intervalo[0] <= salario <= intervalo[1]:
            print("O salário está no : {}".format(lista_salarios[i]))

def saltos():
    lista_ordem_saltos = ['Primeiro Salto', 'Segundo Salto', 'Terceiro Salto', 'Quarto Salto', 'Quinto Salto']
    nome = input("Informe o nome")
    while nome != '':
        lista_saltos = []
        for i in range(0, 5):
            salto = float(input("Informe a altura do salto"))
            lista_saltos.append(salto)
           
        for i in range(0, 5):
             print('{} : {} m' .format(lista_ordem_saltos[i], lista_saltos[i]))   
        media = sum(lista_saltos) / len(lista_saltos)
        print('Resultado Final')
        print('Atleta: {}' .format(nome))
        print('Saltos: {}' .format(lista_saltos))
        print('Média dos saltos: {} m' .format(media))
        nome = input("Informe um nome")
    
    print('Fim do programa')
        
def votos_jogadores():  
    lista_votos = []
    lista_contagem = []
    confirmacao = 1
    while confirmacao != 0:
        voto = int(input("Qual o melhor jogador ?"))
        if voto < 1 or voto > 23:
            print("Voto inválido. Informe um número entre 1 e 23")
        else:
            lista_votos.append(voto)
        confirmacao = int(input("Deseja continuar votando? Sim (1)  Não (0)"))
    
    total_votos = len(lista_votos)
    
    #adciona em uma lista uma sublista com o número de votos, jogador votado
    for i in range(0, len(lista_votos)):
        contagem_item = lista_votos.count(lista_votos[i])
        numero_votado = lista_votos[i]
        lista_contagem.append([contagem_item, numero_votado])     
    
    #quantidade de votos por jogador
    jogadores_processados = set()
    for votos_totais in lista_contagem:
        jogador = votos_totais[1]
        porcentagem_votos = (votos_totais[0] / total_votos) * 100
        # Verifica se o jogador já foi processado
        if jogador not in jogadores_processados:
            print("Jogador: {} Quantidade de votos: {} Porcentagem de votos: {} %".format(jogador, votos_totais[0], porcentagem_votos))
            jogadores_processados.add(jogador)



    #verifica qual foi o jogador mais votado e quantos votos teve
    maior_voto = max(lista_contagem, key=lambda x:x[0])
    jogador_maior_voto = maior_voto[1]

    print("Maior número de votos: {}\nJogador com mais votos: {}" .format(maior_voto[0], jogador_maior_voto))   

def sistemas_operacionais():
    lista_so = [['Microsoft'], ['Unix'], ['Linux'], ['Netware'], ['Mac OS'], ['Outros']]
    lista_votos = []
    confirmacao = 1
    #cria a lista com os votos
    while confirmacao != 0:
        voto = int(input("Digite o voto"))
        if voto >= 1 and voto <= 6:
            lista_votos.append(voto)
        confirmacao = int(input("Deseja continuar votando? Sim(1) Não (0)"))

    total_votos = len(lista_votos)
    num_cont = 1
    #adciona os votos aos índices correspondentes na lista de so
    for i in range(0, 6): 
        contagem = lista_votos.count(num_cont)
        lista_so[i].append(contagem)
        media = (lista_so[i][1] / total_votos) * 100
        lista_so[i].append(media)
        num_cont += 1

    #verifica qual foi o so que teve mais votos
    maior = 0
    for i in range(0, 6):
        if lista_so[i][1] > maior:
            maior = lista_so[i][1]

    for sublista in lista_so:
        if maior in sublista:
            indice = lista_so.index(sublista)

            

    for i in range(0, 6):
        print("{}     {}     {}%\n" .format(lista_so[i][0], lista_so[i][1], lista_so[i][2]))

    print("O sistema operacional mas votado foi o {} com {} votos, correspondendo a {}% dos votos" .format(lista_so[indice][0],lista_so[indice][1], lista_so[indice][2] ))



if (__name__ == "__main__"):
    sistemas_operacionais()
    