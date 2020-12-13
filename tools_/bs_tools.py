from bs4 import BeautifulSoup as bs

def bs_elem_clean(bs_elem):
    '''
    эта функция должна очистить bs элемент от мусорных тегов на
    глубину одного уровня вложенности 
    '''
    for elem in bs_elem.contents:
        print(type(elem))
        if elem.string is None or not elem.string.strip():
            elem.extract()

    return bs_elem


def bs_elem_type(bs_elem):

    """
    Эта функция возвращает тип блока
    """

    tag_name = bs_elem.name

    elem_type = {
        'figure': 'img',
        'img': 'img',
        'div': 'text_block',
        'blockquote': 'text_block',
        'address': 'text_block',
        'article': 'text_block',
        'aside': 'text_block',
        'body': 'text_block',
        'footer': 'text_block',
        'header': 'text_block',
        'main': 'text_block',
        'nav': 'text_block',
        'section': 'text_block',
        'figcaption': 'text_inline',
        'p': 'text_inline',
        'a': 'text_inline',
        'abbr': 'text_inline',
        'b': 'text_inline',
        'big': 'text_inline',
        'em': 'text_inline',
        'i': 'text_inline',
        'small': 'text_inline',
        'span': 'text_inline',
        'strong': 'text_inline',
        'sub': 'text_inline',
        'sup': 'text_inline',
        'del': 'text_inline',
        'ins': 'text_inline',
    }

    return elem_type.get(tag_name, 'text_block')
