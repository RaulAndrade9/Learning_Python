def fibonacci(n):
    fib_sequencia = [0, 1]
    while len(fib_sequencia) < n:
        proximo_numero = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(proximo_numero)

    print(fib_sequencia)
    
def fibonacci2():
    fib_sequencia = [0, 1]
    proximo_numero = 0
    while proximo_numero < 500:
        proximo_numero = fib_sequencia[-1] + fib_sequencia[-2]
        fib_sequencia.append(proximo_numero)

    print(fib_sequencia)

def fatorial(numero):
    resultado = numero
    for i in range(1, numero):
        resultado = resultado * (numero - 1)
        numero -= 1

    print(resultado)

def conjunto_numeros(quantidade):
    lista = []
    for i in range(0, quantidade):
        numero = int(input("Digite um número"))
        lista.append(numero)
    menor = min(lista)
    maior = max(lista)
    soma = sum(lista)
    print("O maior é: {}" .format(maior))
    print("O menor é: {}" .format(menor))
    print("A soma dos números é: {}" .format(soma))


def conjunto_numeros_2(quantidade):
    lista = []
    numero = 0
    for i in range(0, quantidade):
            numero = int(input("Digite um número"))
            if numero < 0 or numero > 1000:
                print("Número inválido")
                numero = int(input("Digite um número"))
            lista.append(numero)
    menor = min(lista)
    maior = max(lista)
    soma = sum(lista)
    print("O maior é: {}" .format(maior))
    print("O menor é: {}" .format(menor))
    print("A soma dos números é: {}" .format(soma))
        
def primo(numero):
    lista = []
    for i in range(2, numero ):
        resultado = numero % i
        print(resultado)
        lista.append(resultado)
    
    for i in range(0, len(lista)):
        if lista[i] == 0:
            primo = "Não é primo"
            break
        else:
            primo = "é primo"
    
    print(primo)
        

def verifica_nota(nota):

    while nota < 0:
        nota = float(input("Digite uma nota válida"))
    
    print("A nota é: {}" .format(nota))

def login_senha(login, senha):
    while login == senha:
        print("A senha não pode ser igual ao login. Informe novamente")
        login = input("Digite o login")
        senha = input("Digite a senha")
    
    print("Login realizado com sucesso")


def valida_informacoes(nome, idade, salario, sexo,):
    while len(nome) <= 3:
        nome = input("Informe um nome válido")
        
    while idade < 0 or idade > 150:
        idade = int(input("Digite uma idade válida"))

    while salario < 0:
        salario = float(input("Informe um salário válido"))

    while sexo != 'm' and sexo != 'f':
        sexo = input("Informe um sexo válido")



    print("Nome: {}\nidade: {}\nsalário: {}\nsexo: {}" .format(nome, idade,salario, sexo))

def populacao_paises(pais_a,taxa_a, pais_b, taxa_b):
    anos = 0
    while pais_a > pais_b:
        pais_a = int(pais_a + (pais_a * (taxa_a / 100)))
        pais_b = int(pais_b + (pais_b * (taxa_b / 100)))
        anos += 1
    
    print("Levará {} anos" .format(anos))
    
def printa_numeros():
    lista = []
    for i in range(1,21):
        lista.append(i)

    for item in lista:
        print(item, end=" ")

    print()

    for item in lista:
        print(item)

def maior_numero():
    lista = []
    for i in range(0,5):
        numero = (int(input("Digite um número")))
        lista.append(numero)

    maior = max(lista)  
    print("O maior número é: {}" .format(maior))                    

def soma_e_media():
    lista = []
    for i in range(0,5):
        numero = (int(input("Digite um número")))
        lista.append(numero)

    soma = sum(lista)
    media = soma / len(lista)

    print("A soma é: {}" .format(soma))
    print("A média é: {}" .format(media))

def verifica_impar():
    for i in range(0, 51):
        if(i % 2 == 1):
            print(i)

def diferenca_dois_inteiros(num_1, num_2):
    soma = 0
    if num_1 > num_2:
        maior = num_1
        menor = num_2
    else:
        maior = num_2
        menor = num_1

    for i in range(menor + 1, maior):
        soma += i
        print(i)
    print("A soma dos números é : {}" .format(soma))

def tabuada(numero):
    for i in range (1, 11):
        mult = i * numero
        print("{} x {} = {}" .format(numero, i, mult))       

def calcula_potencia(base, expoente):
    resultado = base
    for i in range(1, expoente):
        resultado = resultado * base
    print(resultado)

def dez_inteiros():
    lista = []
    for i in range(0, 10):
        numero = int(input("Digite um número"))
        lista.append(numero)
    for i in range(0, len(lista)):
        if (lista[i] % 2 == 0):
            print("{} é par" .format(lista[i]))
        else:
            print("{} é ímpar" .format(lista[i]))

def media_aritimetica():
    num_notas = int(input("Quantas notas serão ?"))
    lista = []
    for i in range(0, num_notas):
        nota = int(input("Digite a nota"))
        lista.append(nota)

    media  = sum(lista) / len(lista)
    print("A média é: {}" .format(media))

def media_idades(numero_pessoas):
    lista = []
    for i in range(0, numero_pessoas):
        idade = int(input("Digite a idade"))
        lista.append(idade)
    
    media = sum(lista) / len(lista)
    if media < 26:
        texto = 'jovem'
    elif media > 60:
        texto = 'idosa'
    else:
        texto = 'Adulta'
    
    print('A média de idades é: {}' .format(texto))

def votacao(eleitores): 
    lista = []
    for i in range (0, eleitores):
        voto = int(input("Digite o voto 1, 2 ou 3"))
        lista.append(voto)
    cand_1 = lista.count(1)
    cand_2 = lista.count(2)
    cand_3 = lista.count(3)
    
    print("Votos candidato 1 {}" .format(cand_1))
    print("Votos candidato 2 {}" .format(cand_2))
    print("Votos candidato 3 {}" .format(cand_3))        

def alunos_turma(turmas):
    lista = []
    for i in range(0, turmas):
        alunos = int(input("Informe o número de alunos"))
        while alunos > 40:
            alunos = int(input("As turmas não podem ter mais que 40 alunos. Informe o número"))
        lista.append(alunos)
    
    media = sum(lista) / turmas
    print("A média de alunos é: {}" .format(media))

def colecao_cd(numero_de_cd):
    lista = []
    for i in range(1, numero_de_cd + 1):
        valor_cd = float(input("Informe o valor do {} CD" .format(i)))
        lista.append(valor_cd)

    total = sum(lista)
    print("O valor total gasto foi: {}" .format(total))

def tabela_loja(qtde_de_produto):
    valor = 1.99
    for i in range(1, qtde_de_produto + 1):
        preco = valor * i
        print("{} - R$ {}" .format(i, preco))

def preco_pao(num_paes):
    valor = 0.18
    for i in range(1, num_paes + 1):
        preco_pao = valor * i
        preco_formatado = "{: .2f}" .format(preco_pao)
        print("{} - R$ {}" .format(i, preco_formatado))

def loja_tabajara(produtos, dinheiro):
    lista = []
    for i in range(1, produtos + 1):
        preco_unit = float(input("Valor do produto"))
        lista.append(preco_unit)
    
    total = sum(lista)
    troco = dinheiro - total
    print("Lojas Tabajara")
    total_lista = len(lista)
    for i in range(1, total_lista ):
        print("Produto {} : R$ {}" .format(i, lista[i]))
    print("Total: R$ {}" .format(total))
    print("Dinheiro: R$ {}" .format(dinheiro))
    print("Troco: R$ {}" .format(troco))

def grupo_numeros(qtde_numeros):
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    for i in range(0, qtde_numeros):
        numero = int(input("Digite um número"))
        if numero < 26:
            lista1.append(numero)
        elif numero < 51:
            lista2.append(numero)
        elif numero < 76:
            lista3.append(numero)
        else:
            lista4.append(numero)
            
    print("Grupo 1: {}" .format(len(lista1)))
    print("Grupo 2: {}" .format(len(lista2)))
    print("Grupo 3: {}" .format(len(lista3)))
    print("Grupo 4: {}" .format(len(lista4)))

def lanchonete():
    prod1 = 'cachorro-quente'
    preco1 = 1.20
    cod1 = 100
    total_cachorro = 0
    
    prod2 = 'bauru'
    preco2 = 1.30
    cod2 = 101
    total_bauru = 0
    
    prod3 = 'Hamburger'
    preco3 = 1.50
    cod3 = 102
    total_hamburger = 0    
    
    prod4 = 'Refri'
    preco4 = 2
    cod4 = 103
    total_refri = 0

    continua_pedido = 1
    while continua_pedido !=0:
        pedido = int(input("Digite o pedido: 1, 2, 3, 4"))
        if pedido == 1:
            total_cachorro += 1
        elif pedido == 2:
            total_bauru += 1
        elif pedido == 3:
            total_hamburger += 1
        else:
            total_refri += 1
        
        continua_pedido = int(input("Deseja continuar pedindo? Sim(1) Não(0)"))

    preco_total_cachorro = preco1 * total_cachorro
    preco_total_bauru = preco2 * total_bauru
    preco_total_hamburger = preco3 * total_hamburger
    preco_total_refri = preco4 * total_refri
    preco_total_lanches = preco_total_cachorro + preco_total_bauru + preco_total_hamburger + preco_total_refri

    if total_cachorro != 0:
        print('{} {} {} {}' .format(prod1, cod1, preco1, total_cachorro))

    if total_bauru != 0:
        print('{} {} {} {}' .format(prod2, cod2, preco2, total_bauru))
    
    if total_hamburger != 0:
        print('{} {} {} {}' .format(prod3, cod3, preco3, total_hamburger))

    if total_refri != 0:
        print('{} {} {} {}' .format(prod4, cod4, preco4, total_refri))

    print("Valor total = {}" .format(preco_total_lanches))

def votacao():
    votos = []
    continua_votando = 1
    while continua_votando !=0:
        voto = int(input("Digite um voto"))
        votos.append(voto)
        continua_votando = int(input("continuar votando? "))

    candidato_1 = votos.count(1)
    candidato_2 = votos.count(2)
    brancos = votos.count(3)
    nulos = votos.count(4)
    votos_total = len(votos)
    porcent_brancos = brancos / (votos_total / 100)
    porcent_nulos = nulos / (votos_total / 100)

    print("votos candidato 1: {}" .format(candidato_1))
    print("Votos candidato 2: {}" .format(candidato_2))
    print("votos em branco: {}" .format(brancos))
    print("votos nulos: {}" .format(nulos))
    print("Porcentagem de votos brancos: {}" .format(porcent_brancos))
    print("Porcentagem de votos nulos: {}" .format(porcent_nulos))

def prova():
    gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
    num = 1
    acertos_totais = 0
    total_alunos = 0
    maior = -1
    menor = 300
    

    while num != 0:
        acertos_erros = []
        respostas = []
        total_alunos +=1
        for i in range(0,10):
            alternativa = input("Digite a alternativa da questão")
            respostas.append(alternativa)

        for i in range(0, len(gabarito)):
            if respostas[i] == gabarito[i]:
                acertos_erros.append(1)
            else:
                acertos_erros.append(0)
        if maior < sum(acertos_erros):
            maior = sum(acertos_erros)
        if menor > sum(acertos_erros):
            menor = sum(acertos_erros)

        print(acertos_erros)
        acertos_totais += sum(acertos_erros)        
        num = int(input("Há algum outro aluno para fazer a prova? Sim(1) Não(0)"))


    alunos_total = total_alunos
    media = acertos_totais / alunos_total

    print("Maior acerto {}" .format(maior))
    print("menor acerto {}" .format(menor))
    print("Total de alunos {}" .format(alunos_total))
    print("Média da turma {}" .format(media))

def prova2(gabarito):
    num = 1
    acertos_totais = 0
    total_alunos = 0
    maior = -1
    menor = 300
    

    while num != 0:
        acertos_erros = []
        respostas = []
        total_alunos +=1
        for i in range(0,10):
            alternativa = input("Digite a alternativa da questão")
            respostas.append(alternativa)

        for i in range(0, len(gabarito)):
            if respostas[i] == gabarito[i]:
                acertos_erros.append(1)
            else:
                acertos_erros.append(0)
        if maior < sum(acertos_erros):
            maior = sum(acertos_erros)
        if menor > sum(acertos_erros):
            menor = sum(acertos_erros)

        print(acertos_erros)
        acertos_totais += sum(acertos_erros)        
        num = int(input("Há algum outro aluno para fazer a prova? Sim(1) Não(0)"))


    alunos_total = total_alunos
    media = acertos_totais / alunos_total

    print("Maior acerto {}" .format(maior))
    print("menor acerto {}" .format(menor))
    print("Total de alunos {}" .format(alunos_total))
    print("Média da turma {}" .format(media))

def salto():
    nome = input("Digite o nome do atleta")
    
    posicao = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
    while nome != '':
        saltos = []
        for i in range(0, 5):
            altura = float(input("Informe a altura do salto"))
            saltos.append(altura)
        melhor = max(saltos)
        pior = min(saltos)
        media = sum(saltos) / len(saltos)

        print("Atleta: {}" .format(nome))
        for i in range(0, len(saltos)):
            print("{} Salto: {}" .format(posicao[i], saltos[i]))
        print("Melhor salto: {}" .format(melhor))
        print("Pior salto: {}" .format(pior))
        print("Média dos demais saltos: {}" .format(media))
        print("Resultado Fina:\n{} {}" .format(nome, melhor))
        nome = input("Digite o nome do atleta")

def inversao(numero):
    inverso = ""
    num_string = str(numero)
    for char in num_string:
        inverso = char + inverso
    
    print(inverso)

def serie(n):
    posicao_1 = 1
    posicao_2 = 1
    lista = []
    lista.append([posicao_1, posicao_2])
    
    for i in range(1, n):
        posicao_1 += 1
        posicao_2 += 2
        lista.append([posicao_1, posicao_2])

    soma = sum([sum(sublista) for sublista in lista])
    print(lista)
    print("Soma: {}" .format(soma))

def serie_2(n):
    posicao_1 = 1
    posicao_2 = 1
    lista = []
    lista.append([posicao_1, posicao_2])

    for i in range(1, n):
        posicao_2 += 1
        lista.append([posicao_1, posicao_2])

    soma = sum([sum(sublista) for sublista in lista])
    print(lista)
    print(soma)    



if(__name__ == "__main__"):
    serie_2(5)