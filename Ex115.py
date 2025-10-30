from time import sleep

c = ['\033[m',          # 0 - sem cor
     '\033[31m',        # 1 - vermelho
     '\033[32m',        # 2 - verde
     '\033[33m',        # 3 - amarelo
     '\033[34m',        # 4 - azul
     '\033[35m',        # 5 - roxo
     '\033[36m']        # 6 - cinza


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as error:
        print(c[1], f'Houve um erro na criação do arquivo! \n#ERR {error}', c[0])
    else:
        print(c[0], f'Arquivo {nome} criado com Sucesso!', c[0])


def lerArquivo(arq):
    try:
        with open(arq, 'r') as arquivo:
            return arquivo.readlines()
    except Exception as error:
        print(c[1], f'Falha ao acessar arquivo!!! \n# ERR {error}', c[0])


def salvarArquivo(arq, n='desconhecido', i=0):
    try:
        with open(arq, 'at') as arquivo:
            arquivo.write(f'{n};{i}\n')
    except Exception as error:
        print(c[1], f'Falha ao acessar arquivo!!! \n# ERR {error}', c[0])


def leiaInt(val=''):
    while True:
        try:
            x = int(input(val))
        except (ValueError, TypeError):
            print(c[1], 'ERRO! Digite um numero inteiro válido', c[0])
        except KeyboardInterrupt:
            print(c[1], '\nO usuário preferiu não digitar este número', c[0])
            x = 0
            break
        else:
            break
    return x


def leiaOp(val='', qtd=0):
    while True:
        try:
            x = int(input(val))
        except (ValueError, TypeError):
            print(c[1], 'ERRO! Digite uma opção válida', c[0])
        except KeyboardInterrupt:
            print(c[1], '\nO Execução interrompida. Saindo do Sistema', c[3])
            x = qtd
            break
        else:
            if x <= qtd:
                break
            else:
                print(c[1], 'ERRO! Digite uma opção válida', c[3])
    return x


def titulo(msg, cor=0, tam=40):
    print(c[cor], end='')
    print('-' * tam)
    print(f'{msg:^{tam}}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


def menu(lista, tam=40):
    titulo('MENU PRINCIPAL', 0, tam)
    cont = 1
    for item in lista:
        print(c[3], cont, ' -', c[4], item)
        cont += 1
    print(c[0], end='')
    print('-'*tam)
    print(c[3], end='')
    x = leiaOp('Sua opção: ', len(lista))
    print(c[0], end='')
    return x


def listaCadastro(tam=40):
    titulo('PESSOAS CADASTRADAS', 0, tam)
    arq = lerArquivo(file)
    for linha in arq:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<{tam - 8}}{dado[1]:>3} anos')


def novoCadastro(tam=40):
    titulo('NOVO CADASTRO', 0, tam)
    nome = str(input('Nome: '))
    idade = leiaInt('Idade: ')
    salvarArquivo(file, nome, idade)
    print(f'Novo Registro {nome} adicionado.')


def sairSistema(tam=40):
    titulo('Saindo do Sistema... Até Logo!', 1, tam)


# MAIN
t = 60
file = 'cadastro.txt'
if not arquivoExiste(file):
    criarArquivo(file)
while True:
    op = menu(['Listar Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'], t)
    if op == 1:
        listaCadastro(t)
    elif op == 2:
        novoCadastro(t)
    elif op == 3:
        sairSistema(t)
        break
