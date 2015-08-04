import os
import json

from nthu_library.library import NTHULibrary, UserPayload


__author__ = 'salas'


def get_newest_books(lib, **kwargs):
    """
        :param lang: default is `None` to get both languages,
                     'en' for English; or 'zh' for Chinese
    """
    return lib.get_newest_books(**kwargs)


def get_top_circulations(lib, **kwargs):
    """
        :param year: 4-digit number
        :param type: 'loaned' or 'reserved'
    """
    return lib.get_top_circulated_materials(**kwargs)


def get_personal_info(lib):
    result = lib.get_info()
    info = {
        'personal': result,
        '借閱歷史': lib.get_bowrrow_history(result),
        '借閱中': lib.get_current_bowrrow(result),
        '預約紀錄': lib.get_reserve_history(result),
    }
    return info

if __name__ == '__main__':

    id = os.getenv('NTHU_LIBRARY_ID') or input('ID: ')
    pwd = os.getenv('NTHU_LIBRARY_PWD') or input('PWD: ')

    user = UserPayload(id, pwd)
    library = NTHULibrary(user)

    funcs = {
        'personal': get_personal_info,
        'new': get_newest_books,
        'top': get_top_circulations,
    }

    print('''
        `personal`: get personal data
        `new`: get newest books
        `top`: get top circulated materials
    ''')

    instr = input('What do you want to do > ').strip()
    results = funcs[instr](library)

    with open('my-library-data.json', 'w', encoding='utf8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False, sort_keys=True)
