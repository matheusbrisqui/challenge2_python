# Solicitando nome, email
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

# Validando nome e email
validaNome = input(
    f"Seu nome ({nome}) e email ({email}) estão corretos? \nResponda com 'Sim' ou 'Não': ")
while validaNome.lower() != "sim":
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    validaNome = input(
        f"Seu nome ({nome}) e email ({email}) estão corretos?  \nResponda com 'Sim' ou 'Não': ")


# Solicitando uma senha de  no minímo oito digítos
senha = input("Digite sua senha (minímo de oito dígitos): ")

# Validando senha com no mínimo 8 dígitos
while len(senha) < 8:
    senha = input("Digite sua senha (minímo de oito dígitos): ")

# Perguntando se a senha está correta
validaSenha = input(
    f"Sua senha ({senha}) está correta? \nResponda com 'Sim' ou 'Não': ")
while validaSenha.lower() != "sim":
    senha = input("Digite sua senha (minímo de oito dígitos): ")
    validaSenha = input(
        f"Sua senha: {senha} está correta? \nResponda com 'Sim' ou 'Não': ")

# Iniciando o loop
while True:
    # Criando um menu de opções para o usuário
    menu = '''
    [1]- Como você imagina que é para um cadeirante ao pegar um ônibus \n
    [2]- Questionário sobre acessibilidade \n
    [3]- Quiz sobre acessibilidade em transportes públicos \n
    [4]- Encerrar programa
    '''
    print(menu)
    escolha = int(input("Escolha uma das opções acima (de 1 - 4): "))

    # Repetindo a pergunta caso o numero não esteja entre 1 e 4
    while escolha > 4 or escolha < 1:
        escolha = int(input("Escolha uma das opções acima (de 1 - 4): "))

# Encerrando o programa caso o usuário deseje
    if escolha == 4:
        print("Programa encerrado")
        break

# Criando situação 1

# Criando a variável respostas[], para armazenar todas as respostas do usuário
    respostas1 = []

# Iniciando as perguntas
    if escolha == 1:
        for a in range(5):
            opcao1 = input(
                "Digite uma situação em que você imagina que um cadeirante tem dificuldade para pegar um ônibus: ")
            respostas1.append(opcao1)
            
# Perguntando se o usuário quer receber suas respostas de volta
        respostas2 = input(
            f"{nome}, você gostaria de receber suas respostas de volta? \nResponda com 'Sim' ou 'Não': ")
        if respostas2.lower() == "sim":
            print(
                f"Suas respostas foram: {respostas1} \nMuito obrigado, {nome}!")

# Criando situação 2
    if escolha == 2:
        # Fazendo a primeira pergunta
        questionario1 = input(
            '\nVocê já teve que deixar de pegar ônibus por não ser viável à sua condição física? \nResponda com "Sim" ou "Não": ')
        # Criando o loop para a resposta ser sim ou não
        while questionario1.lower() != "sim" and questionario1.lower() != "nao" and questionario1.lower() != "não":
            # Repetindo a pergunta caso necessário
            questionario1 = input(
                '\nVocê já teve que deixar de pegar ônibus por não ser viável à sua condição física? \nResponda com "Sim" ou "Não": ')
        if questionario1.lower() == "sim":
            # Fazendo a segunda pergunta, caso a primeira resposta tenho sido "sim"
            questionario2 = input(
                '\nQuais foram os motivos que tornaram o ônibus inacessível? \nResposta: ')
        # Fazendo a terceira pergunta
        questionario3 = input(
            '\nPela sua experiência, os motoristas de ônibus são capacitados para lidar com passageiros com deficiência física? \nResponda com "Sim" ou "Não": ')
        # Criando o loop para a resposta ser sim ou não
        while questionario3.lower() != "sim" and questionario3.lower() != "nao" and questionario3.lower() != "não":
            # Repetindo a pergunta caso necessário
            questionario3 = input(
                '\nPela sua experiência, os motoristas de ônibus são capacitados para lidar com passageiros com deficiência física? \nResponda com "Sim" ou "Não": ')
        # Fazendo a quarta pergunta, caso a terceira resposta tenha sido "não"
        if questionario3.lower() == "nao" or questionario3.lower() == "não":
            questionario4 = input(
                '\nEm quais aspectos os motoristas deveriam se aprimorar? \nResposta: ')
        # Fazendo a quinta pergunta
        questionario5 = input(
            '\nVocê acredita que existem soluções tecnológicas que poderiam ajudar a melhorar a acessibilidade do transporte público para as pessoas com deficiência física? \nResponda com "Sim" ou "Não": ')
        # Criando o loop para a resposta ser sim ou não
        while questionario5.lower() != "sim" and questionario5.lower() != "nao" and questionario5.lower() != "não":
            # Repetindo a pergunta caso necessário
            questionario5 = input(
                '\nVocê acredita que existem soluções tecnológicas que poderiam ajudar a melhorar a acessibilidade do transporte público para as pessoas com deficiência física? \nResponda com "Sim" ou "Não": ')
        # Fazendo a sexta pergunta, caso a quinta resposta seja "sim"
        if questionario5.lower() == "sim":
            questionario6 = input('\nComo quais? \nResposta: ')
        # Realizando a sétima e última pergunta
        questionario7 = input(
            f'\nObrigado, {nome}, por responder o questionário! \nGostaria de receber suas respostas? \nResponda com "Sim" ou "Não": ')
        # Criando um loop para resposta ser "sim" ou "não"
        while questionario7.lower() != "sim" and questionario7.lower() != "nao" and questionario7.lower() != "não":
            # Repetindo a pergunta caso necessário
            questionario7 = input(
                f'\nObrigado, {nome}, por responder o questionário! \nGostaria de receber suas respostas? \nResponda com "Sim" ou "Não": ')
        # Tornando as perguntas do questionário em variáveis
        a1 = ('Você já teve que deixar de pegar ônibus por não ser viável à sua condição física? ')
        b1 = ('Quais foram os motivos que tornaram o ônibus inacessível? ')
        c1 = ('Pela sua experiência, os motoristas de ônibus são capacitados para lidar com passageiros com deficiência física? ')
        d1 = ('Em quais aspectos os motoristas deveriam se aprimorar? ')
        e = ('Você acredita que existem soluções tecnológicas que poderiam ajudar a melhorar a acessibilidade do transporte público para as pessoas com deficiência física? ')
        i = ('Como quais? ')
        # Devolvendo as respostas ao usuário, caso solicitado
        if questionario7.lower() == "sim":
            print(
                f'1- {a1} \nResposta: {questionario1} \n\n{b1} \nResposta: {questionario2} \n\n')
            print(
                f'2- {c1} \nResposta: {questionario3} \n\n{d1} \nResposta: {questionario4} \n\n')
            print(
                f'3- {e} \nResposta: {questionario5} \n\n{i} \nResposta: {questionario6}')
            print(f'\nObrigado, {nome}! \nQuestionário finalizado.\n\n\n')
        else:
            print(f'Obrigado, {nome}! \nQuestionário finalizado. \n\n\n')

# Criando a situação 3
    if escolha == 3:
    # Criando uma variável contadora para contar quantas questões o usuário acertou
        cont = 0

    # Fazendo a primeira pergunta com uso de função
        def quiz1():
            questao1 = input(
                "Quantos '%' da população brasileira possui algum tipo de deficiência? \na)35% \nb)20% \nc)24% \nd)25% \nResposta: ")
            return questao1
        populacao = quiz1()
        
    # Conferindo se a resposta está correta e contando
        if populacao.lower() == "a":
            cont += 1

    # Criando a segunda pergunta com uso de função
        def quiz2():
            questao2 = input(
                "Quantos '%' das pessoas com deficiência no Brasil passam por dificuldades ao pegar um transporte público? \na) 50% \nb) 55% \nc) 65% \nd) 63% \nResposta: ")
            return questao2
        dificuldade = quiz2()

    # Conferindo se a resposta está correta e contando
        if dificuldade.lower() == "d":
            cont += 1

    # Fazendo a terceira pergunta com uso de função
        def quiz3():
            questao3 = input(
                "Quantos '%' dos ônibus urbanos você acha que atendem plenamente as necessidades dos deficientes? \na) 1% \nb) 0.9% \nc) 1.5% \nd) 1.3% \nResposta: ")
            return questao3
        onibus = quiz3()

    # Conferindo se a resposta está correta e contando
        if onibus.lower() == "b":
            cont += 1

    # Fazendo a quarta pergunta com uso de função
        def quiz4():
            questao4 = input(
                "Quantos '%' dos deficientes dizem que os ônibus tem uma acessibilidade boa ou muito boa? \na) 20% \nb) 25% \nc) 22% \nd) 18% \nResposta: ")
            return questao4
        acessibilidade = quiz4()

    # Conferindo se a resposta está correta e contando
        if acessibilidade.lower() == "c":
            cont += 1

    # Transformando as questões em variáveis
        a2 = (
            "Quantos '%' da população brasileira possui algum tipo de deficiência? \na)35% \nb)20% \c)24% \nd)25%")
        b2 = (
            "Quantos '%' das pessoas com deficiência no Brasil passam por dificuldades ao pegar um transporte público? \na) 50% \nb) 55% \nc) 65% \nd) 63%")
        c2 = (
            "Quantos '%' dos ônibus urbanos você acha que atendem plenamente as necessidades dos deficientes? \na) 1% \nb)0.9% \nc) 1.5% \nd)1.3%")
        d2 = (
            "Quantos '%' dos deficientes dizem que os ônibus tem uma acessibilidade boa ou muito boa? \na) 20% \nb) 25% \nc) 22% \nd) 18%")

    # Perguntando para o usuário se ele quer receber suas respostas de volta e seu resultado final
        pergunta = input(
            "Você gostaria de receber suas respostas de volta? Além disso seu resultado final? \nResponda com 'Sim' ou 'Não': ")
    
    # Criando um loop para resposta ser "sim" ou "não"
        while pergunta.lower() != "sim" and pergunta.lower() != "não" and pergunta.lower() != "nao":
            pergunta = input(
            "Você gostaria de receber suas respostas de volta? Além disso seu resultado final? \nResponda com 'Sim' ou 'Não': ")

    # Devolvendo as respostas e resultado caso solicitado
        if pergunta.lower() == "sim":
            print(
                f'1- {a2} \nResposta: {populacao} \n\n{b2} \nResposta: {dificuldade} \n\n')
            print(
                f'2- {c2} \nResposta: {onibus} \n\n{d2} \nResposta: {acessibilidade} \n\n')
            print(
                f"Seu resultado foi de {cont}/4")
            print(
                f'\nObrigado, {nome}! \nQuiz finalizado.\n\n\n')
        else:
            print(
                f'\nObrigado, {nome}! \nQuiz finalizado.\n\n\n')