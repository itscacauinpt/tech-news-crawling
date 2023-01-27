import sys

from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_tag, search_by_category
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


menu = '''
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


def func_get_tech_news(user_response):
    amount = int(user_response)
    return get_tech_news(amount)


def func_search_by_category(category): return search_by_category(category)


def func_search_by_title(title): return search_by_title(title)


def func_search_by_date(date): return search_by_date(date)


def func_search_by_tag(tag): return search_by_tag(tag)


def func_top_5_categories(): return top_5_categories()


def func_top_5_news(): return top_5_news()


options_message = {
    '0': {
        'message': 'Digite quantas notícias serão buscadas: ',
        'func': func_get_tech_news
    },
    '1': {
        'message': 'Digite o título: ',
        'func': func_search_by_title
    },
    '2': {
        'message': 'Digite a data no formato aaaa-mm-dd: ',
        'func': func_search_by_date
    },
    '3': {
        'message': 'Digite a tag: ',
        'func': func_search_by_tag
    },
    '4': {
        'message': 'Digite a categoria: ',
        'func': func_search_by_category
    }
}


options_functions = {
    '5': {'func': func_top_5_news},
    '6': {'func': func_top_5_categories}
}


def resolve_input_func(user_option):
    for op in options_functions.keys():
        if user_option == op:
            option = options_functions[user_option]

            return option['func']()


def resolve_input(user_option):
    for op in options_message.keys():
        if user_option == op:
            option = options_message[user_option]
            user_response = input(option['message'])

            return option['func'](user_response)


# Requisito 12
def analyzer_menu():
    print(menu)
    user_option = input('Escolha uma opção: ')

    if user_option == '7':
        return sys.stderr.write('Encerrando script')

    elif user_option in options_message.keys():
        return resolve_input(user_option)

    elif user_option in options_functions.keys():
        return resolve_input_func(user_option)

    else:
        return sys.stderr.write('Opção inválida')
