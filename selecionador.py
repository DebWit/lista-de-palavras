def seleciona_palavras_cinco_letras(nome_do_arquivo:str):

    #1. abrir o arquivo
    lista_completa = []
    conteudo = open(nome_do_arquivo, 'r', encoding = "UTF-8")

    #2. ler o arquivo
    conteudo = conteudo.read()

    #3. separar a string gigante por espaços / criar a lista completa de palavras
    lista_completa = conteudo.split()

    #4. criar nova lista com apenas as palavras com 5 letras
    lista_cinco_letras = []

    for palavra in lista_completa:
        if len(palavra) == 5:
            lista_cinco_letras.append(palavra)
            lista_cinco_letras.append("\n")

    print(lista_cinco_letras)

    #5. salvar em um novo arquivo

    novo_conteudo = open(nome_do_arquivo + "_de_cinco_letras","x", encoding = "UTF-8")
    novo_conteudo.writelines(lista_cinco_letras)


seleciona_palavras_cinco_letras("dicio")
