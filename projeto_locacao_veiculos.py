# Maria Fernanda
from datetime import datetime, date

inventario = {
    'Econômico': {'Fiat Mobi': 1, 'Chevrolet Onix': 3, 'Renault Kwid': 1},
    'Standard': {'Volkswagen Gol': 1, 'Hyundai HB20': 1, 'Fiat Argo': 2},
    'Minivan': {'Fiat Doblò': 4, 'Chevrolet Spin': 1, 'Renault Kangoo': 1},
    'Suv': {'Jeep Renegade': 1, 'Hyundai Creta': 2, 'Chevrolet Tracker': 3},
    'Intermediário': {'Toyota Corolla': 1, 'Honda Civic': 2, 'Nissan Sentra': 3},
    'Utilitário': {'Fiat Toro': 3, 'Chevrolet S10': 1, 'Ford Ranger': 1},
    'Premium': {'BMW Série 3': 4, 'Audi A4': 1, 'Mercedes-Benz Classe C': 2},
    'Cargo': {'Fiat Fiorino': 6, 'Renault Master': 1, 'Peugeot Partner': 1}}

carros_alugados = {('PAULO', 16991198944): [{'modelo': 'Chevrolet Onix', 'data_retirada': '05/05/2024', 'data_devolucao': '09/06/2024'},
                                            {'modelo': 'Toyota Corolla', 'data_retirada': '11/10/2024', 'data_devolucao': '02/12/2024'}],
                   ('PEDRO', 996152625): [{'modelo': 'Fiat Fiorino', 'data_retirada': '19/05/2024', 'data_devolucao': '02/11/2024'}]}
opcao = ''


# Funções de base:

# Maria Fernanda
def cadastro():
    print("-" * 100)

    # Lê o nome e aceita apenas entradas de letras
    n = input('Qual seu nome? ')
    while not n.isalpha():
        n = input('Qual seu nome? ')

    # Lê o telefone e aceita apenas entradas de números inteiros
    t = input('Qual o seu número de telefone? ')
    while not t.isdigit():
        t = input('Qual o seu número de telefone? ')
    t = int(t)

    # Cria uma tupla (id) com os valores nome e telefone.
    # De nome: espaços em branco são retirados e todos caracteres são colocados em letras maiúsculas.
    id = (n.replace(" ", "").upper(), t)

    # nome, telefone e a tupla são retornados
    return n, t, id


# Maria Fernanda
def obter_data(mensagem):
    """
    Os comandos try e except servem para tratar exceções, ou seja, para lidar com erros.

    O bloco try abriga os comando de leitura que podem gerar os erros, caso isto ocorra, o bloco except captura
    a exceção especificada (ValueError neste caso) de modo que o programa prossegue sem apresentar o erro de leitura.

    O loop indefinido só irá parar quando houver o return, então enquanto a leitura não gerar erros, o loop continua.
    """
    while True:
        print("-" * 100)
        try:
            print(mensagem)
            ano = int(input('Ano: '))
            mes = int(input('Mês: '))
            dia = int(input('Dia: '))
            return date(ano, mes, dia)
        except ValueError:
            print('Data inválida! Por favor, insira uma data válida.')
            print('-' * 100)


# Joice
def qual_categoria_desejada():
    print("-" * 100)

    # cria-se uma lista contendo apenas as categorias de carros (através das chaves do dicionário inventário)
    categorias = list(inventario.keys())

    print('Escolha a categoria do carro:')
    # Enumera todos os elementos (categorias) da lista categoria a partir de 1. cat assume o valor de cada elemento
    for i, cat in enumerate(categorias, 1):
        print(f'Digite [{i}] para {cat}')

    escolha = input()

    # Se a leitura de escolha for um número inteiro entre 1 e 8, a função retorna a categoria escolhida
    if escolha.isdigit() and 1 <= int(escolha) <= 8:
        return categorias[int(escolha) - 1]

    # Caso a leitura não seja um inteiro entre 1 e 8, o código prossegue e é retornado None
    print('Escolha inválida!')
    return None


# Funções de funcionamento:

# Joice
def listar_modelos_disponiveis():
    print('-' * 100)
    print('Modelos de carros disponíveis:')

    modelos_disponiveis = False

    # Percorre todos items de inventario
    for categoria, modelos in inventario.items():
        print(f"Categoria: {categoria}")

        # Percorre cada par modelo:quantidade dos modelos cadastrados
        for modelo, quantidade in modelos.items():

            # Se a quantidade for diferente de zero, será impresso o modelo do automóvel e sua respectiva quantidade
            # As condicionais abaixo servem para corrigir a escrita (singular ou plural) e
            # tornar modelos_disponiveis verdadeiro, de modo que existe algum modelo_disponivel
            if quantidade == 1:
                print(f" - {modelo:<30} {quantidade:>3} automóvel disponível")
                modelos_disponiveis = True
            elif quantidade > 1:
                print(f" - {modelo:<30} {quantidade:>3} automóveis disponíveis")
                modelos_disponiveis = True

    # Caso modelos_disponiveis == False: então não existe nenhum modelo com quantidade diferente de zero.
    if not modelos_disponiveis:
        print('Nenhum modelo disponível no momento.')


# Paulo
def alugar_carro():
    # Registra os dados da pessoa
    nome, telefone, identificacao = cadastro()

    # Registra a data de retirada e devolução do veículo
    data_retirada = obter_data('Digite a data de retirada do veículo:')
    data_devolucao = obter_data('Digite a data de devolução do veículo:')
    # O loop a seguir não permite que a data de retirada seja superior a data de revolução
    while data_retirada > data_devolucao:
        print('-' * 100)
        data_retirada = obter_data('Digite a data de retirada do veículo:')
        data_devolucao = obter_data('Digite a data de devolução do veículo:')

    # A diferença de dias entre as datas + 1 é o total de diárias que devem ser pagas
    data_dif = (data_devolucao - data_retirada).days + 1
    print('-' * 100)
    print(f'{nome}, você irá retirar o carro em {data_retirada} e devolver em {data_devolucao}')
    input(f'Assim, terá que pagar {data_dif} diárias, aperte qualquer tecla se deseja prosseguir com a locação')

    # categoria assume o valor da categoria escolhida pelo usuário
    categoria = qual_categoria_desejada()
    print('-' * 100)
    # Essa condicional evita erro no programa caso o usuário selecione uma categoria inexistente
    if not categoria:
        return

    modelos_disponiveis = []
    # Uma lista de modelos_disponiveis é criada
    # Os items do inventario na categoria escolhida são percorridos
    for modelo, quantidade in inventario[categoria].items():
        # A tupla (modelo, quantidade) é adicionada a lista criada se a quantidade for maior ou igual a 1
        if quantidade >= 1:
            modelos_disponiveis.append((modelo, quantidade))

    # Se modelo_disponiveis for vazia, a função se encerra e uma mensagem é dada
    if not modelos_disponiveis:
        print('Nenhum modelo disponível na categoria escolhida.')
        return

    # Os modelos disponiveis sao enumerados e apresentados (bem como a quantidade)
    print('Modelos disponíveis: (Digite o número correspondente ao carro desejado)')
    for i, (modelo, quantidade) in enumerate(modelos_disponiveis, 1):
        print(f'[{i}] - {modelo} - {quantidade} carros disponíveis')

    escolha = input()
    # Se a leitura de escolha for um numero inteiro pertencente ao intervalo [1, quantidade de modelos disponiveis]
    if escolha.isdigit() and 1 <= int(escolha) <= len(modelos_disponiveis):
        # O modelo é definido
        modelo_escolhido, _ = modelos_disponiveis[int(escolha) - 1]

        # O dicionário carro alugado recebe valores para as chaves modelo, data de retirada e data de devolução
        carro_alugado = {
            'modelo': modelo_escolhido,
            'data_retirada': data_retirada.strftime('%d/%m/%Y'),
            'data_devolucao': data_devolucao.strftime('%d/%m/%Y')}

        # Se o cadastro do usuário é uma chave que já está contida no dicionário de carros alugados,
        # os dados do carro alugado são adicionados a este cadastro (dentro de uma lista)
        # Se não, a chave de cadastro é criada e os dados são adicionados a esta chave (também em uma lista)
        if identificacao in carros_alugados:
            carros_alugados[identificacao].append(carro_alugado)
        else:
            carros_alugados[identificacao] = [carro_alugado]

        print('-' * 100)
        print(f'Carro {modelo_escolhido} alugado por {data_dif} dias com sucesso! Retire o carro na data de {data_retirada}')

        # Por fim, é necessário remover uma unidade do inventário da quantidade referente ao modelo escolhido
        inventario[categoria][modelo_escolhido] -= 1
    else:
        print('Escolha inválida!')


# Paulo
def devolver_carro():
    # Registra os dados da pessoa
    nome, telefone, identificacao = cadastro()

    # Se a identificação do usuário não estiver no dicionário ou se estiver vazia, ele não tem carros alugados.
    if identificacao not in carros_alugados or not carros_alugados[identificacao]:
        print(f'{nome} de telefone {telefone} não possui carros alugados.')
        return

    # Obtem a data de hoje
    # Carros assume o valor da lista contendo os dicionários de cada carro alugado
    data_atual = date.today()
    carros = carros_alugados[identificacao]

    # Enumerar quantos carros estão alugados e exibir os dados
    for idx, carro in enumerate(carros, 1):
        print(
            f'[{idx}] - {carro["modelo"]} - Retirado em {carro["data_retirada"]}, para devolver em {carro["data_devolucao"]}')

    # Ler e validar qual carro (modelo) será devolvido
    escolha = input('Digite o número do carro que deseja devolver: ')
    while not escolha.isdigit() or not (1 <= int(escolha) <= len(carros)):
        escolha = input('Escolha inválida! Digite novamente o número do carro que deseja devolver: ')
    escolha = int(escolha)

    # O modelo selecionado é removido da lista de carros, ou seja, carros_alugados (Shallow)
    # Além disso, carro_devolver recebe este valor
    carro_devolver = carros.pop(int(escolha) - 1)

    # Converte as datas de strings para objetos date
    data_retirada = datetime.strptime(carro_devolver['data_retirada'], '%d/%m/%Y').date()
    data_devolucao = datetime.strptime(carro_devolver['data_devolucao'], '%d/%m/%Y').date()

    # Encontra a categoria e o modelo do carro devolvido e aumenta a quantidade em carros_disponiveis
    modelo = carro_devolver['modelo']
    for categoria, carros_categoria in inventario.items():
        if modelo in carros_categoria:
            carros_categoria[modelo] += 1
            break

    print("-" * 100)
    # Análise das datas de retirada e devolução em relação à data atual
    if data_atual < data_retirada:
        print('O carro ainda não foi retirado. Locação cancelada.')
    elif data_atual > data_devolucao:
        dias_atraso = (data_atual - data_devolucao).days
        print(f'Houve um atraso de {dias_atraso} dias na devolução.')
        print('Carro devolvido com sucesso!')
    elif data_atual < data_devolucao:
        dias_adiantamento = (data_devolucao - data_atual).days
        print(f'Você devolveu o carro {dias_adiantamento} dias antes do previsto.')
        print('Carro devolvido com sucesso!')
    else:
        print('Você devolveu o carro na data correta.')
        print('Carro devolvido com sucesso!')

    # Se após a devolução, a lista de carros alugados estiver vazia, a identificação do usuário é removida
    if not carros:
        del carros_alugados[identificacao]


# Paulo
def adicionar_carro_inventario():
    # categoria assume o valor da categoria escolhida pelo usuário
    categoria = qual_categoria_desejada()
    print("-" * 100)

    # Se a categoria for vazia, a função é retornada
    if not categoria:
        return

    # Validar a leitura de modelo e quantidade
    modelo = input('Digite o modelo do carro que deseja adicionar: ')
    while not modelo.replace(" ", "").isalpha():
        modelo = input('Digite o modelo do carro que deseja adicionar: ')

    quantidade = input('Digite a quantidade de carros a serem adicionados: ')
    while not quantidade.isdigit():
        quantidade = input('Digite a quantidade de carros a serem adicionados: ')
    quantidade = int(quantidade)

    carro_existente = False
    # Se o modelo digitado existe na categoria dada de carros_disponiveis, a quantidade dada é adicionada.
    if modelo in inventario[categoria]:
        inventario[categoria][modelo] += quantidade
        carros_existente = True

    # Se o modelo não existe na categoria dada, um dicionário {modelo: quantidade} é criado.
    if not carro_existente:
        inventario[categoria][modelo] = quantidade

    print("-" * 100)
    print(f'{quantidade} unidades do veículo {modelo} de categoria {categoria} foram adicionadas com sucesso!')


# Sara
def listar_carros_alugados():
    print("-" * 100)
    print('Dados de carros alugados:')

    if not carros_alugados:
        print('Nenhum carros está alugado no momento.')
    else:
        # Se todos_carros_alugados não for vazia
        # Percorrer todos os clientes e seus carros alugados
        for identificacao, carros in carros_alugados.items():
            nome, telefone = identificacao
            print(f'Nome: {nome}, Telefone: {telefone}')
            # Percorrer cada indíce de carros
            for carro in carros:
                print(
                    f' - Modelo: {carro["modelo"]}, Retirado em {carro["data_retirada"]}, Devolução em {carro["data_devolucao"]}')


# Sara
def listar_carros_devolucao_hoje():
    print('-' * 100)
    data_atual = date.today()
    print(f'Carros que devem ser devolvidos hoje ({data_atual}):')
    carros_hoje = []

    # Percorrer todos os clientes e seus carros alugados
    for identificacao, carros in carros_alugados.items():
        # Percorrer cada indíce de carros
        for carro in carros:
            # Verificar se a data de devolução do carro é hoje. Se sim, adicionar a lista criada
            if carro['data_devolucao'] == data_atual.strftime('%d/%m/%Y'):
                carros_hoje.append((identificacao, carro))

    # Se haver algum carro a ser devolvido hoje:
    if carros_hoje:
        # Enumera a lista de carros a ser devolvidos hoje e percorre cada usuário e seu modelo
        for idx, (identificacao, carro) in enumerate(carros_hoje, 1):
            nome, telefone = identificacao
            print(f'{idx}. Nome: {nome}, Telefone: {telefone}, Modelo: {carro["modelo"]}')
    else:
        print('Nenhum carro deve ser devolvido hoje')


# Sara
def listar_carros_devolucao_atrasada():
    print('-' * 100)
    data_atual = date.today()
    print('Carros com devolução atrasada:')
    carros_atrasados = []

    # Percorrer todos os clientes e seus carros alugados
    for identificacao, carros in carros_alugados.items():
        # Percorrer cada indíce de carros
        for carro in carros:
            data_devolucao = datetime.strptime(carro['data_devolucao'], '%d/%m/%Y').date()
            # Verificar se a data de devolução do carro está atrasada
            if data_atual > data_devolucao:
                carros_atrasados.append((identificacao, carro))

    # Se haver algum carro atrasado:
    if carros_atrasados:
        # Enumera a lista de carros a ser atrasados e percorre cada usuário e seu modelo
        for idx, (identificacao, carro) in enumerate(carros_atrasados, 1):
            nome, telefone = identificacao
            print(
                f'{idx}. Nome: {nome}, Telefone: {telefone}, Modelo: {carro["modelo"]}, Data de devolução: {carro["data_devolucao"]}')
    else:
        print('Nenhum carro está com devolução atrasada.')


# Maria Fernanda
# Menu de execução
while opcao != '8':
    print("-" * 100)
    print("1. Exibir carros disponíveis")
    print("2. Alugar carro")
    print("3. Devolver carro")
    print("4. Adicionar carro ao inventário")
    print("5. Listar carros alugados")
    print("6. Verificar carros que devem ser devolvidos hoje")
    print("7. Verificar carros com devolução atrasada")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        listar_modelos_disponiveis()
    elif opcao == '2':
        alugar_carro()
    elif opcao == '3':
        devolver_carro()
    elif opcao == '4':
        adicionar_carro_inventario()
    elif opcao == '5':
        listar_carros_alugados()
    elif opcao == '6':
        listar_carros_devolucao_hoje()
    elif opcao == '7':
        listar_carros_devolucao_atrasada()
    elif opcao == '8':
        print("-" * 100)
        print("Saindo do sistema...")
        print(carros_alugados)
        print("-" * 100)
