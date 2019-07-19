nome = input('nome:')
sobrenome = input('spbrenome:')
login = input('e-mail:')
senha = input('crie uma senha:')

print('certo entao se nome e:' ,nome + sobrenome ,'e seu e-mail e:',login,'e sua senha e:',senha)

def verificaçao():
    if login == 'jessico': 
        if senha == '13465':
            print('logado')
        else:
            print('ta errado!')
    else:
        print('esse usuario nao existe ')
verificaçao()