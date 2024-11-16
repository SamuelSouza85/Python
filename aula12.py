nome = str(input('Qual é seu nome? '))
if nome == 'Samuel':
    print('Que nome bonito')
elif nome == 'João' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nomem é bem popular')
elif nome == 'Erick':
    print('Não gosto muito do seu nome')
else:
    print('Seu nome é bem comum')
print('Tenha um bom dia, {}!'.format(nome))