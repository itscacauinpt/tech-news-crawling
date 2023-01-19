import sys

options_menu = '''
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
'''

options = {
    '0': 'Digite quantas notícias serão buscadas: ',
    '1': 'Digite o título: ',
    '2': 'Digite a data no formato aaaa-mm-dd: ',
    '3': 'Digite a tag: ',
    '4': 'Digite a categoria: '
}


def resolve_input(user_option):
    for op in options.keys():
        if op == user_option:
            return options[op]


# Requisito 12
def analyzer_menu():
    print(options_menu)
    user_option = input('Escolha uma opção: ')

    if user_option in options.keys():
        resolve_input(user_option)

    else:
        sys.stderr.write('Opção inválida')


analyzer_menu()
