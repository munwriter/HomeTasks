dictoflatters = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'i',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ч': 'cz',
    'ш': 'sh',
    'щ': 'she',
    'ъ': '',
    'ы': 'y',
    'ь': 'b',
    'э': 'e',
    'ю': 'yu',
    'я': 'ya',
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'C',
    'Ч': 'Cz',
    'Ш': 'Sh',
    'Щ': 'She',
    'Ъ': '',
    'Ы': 'y',
    'Ь': 'b',
    'Э': 'E',
    'Ю': 'Yu',
    'Я': 'Ya',
    ',': ',',
    '?': '?',
    ' ': ' ',
    '~': '~',
    '!': '!',
    '@': '@',
    '#': '#',
    '$': '$',
    '%': '%',
    '^': '^',
    '&': '&',
    '*': '*',
    '(': '(',
    ')': ')',
    '-': '-',
    '=': '=',
    '+': '+',
    ':': ':',
    ';': ';',
    '<': '<',
    '>': '>',
    '\'': '\'',
    '"': '"',
    '\\': '\\',
    '/': '/',
    '№': '#',
    '[': '[',
    ']': ']',
    '{': '{',
    '}': '}',
    '—': '-',
    '.': '.',
    '«': '«',
    '»': '»'
}

s=input()
ss=''
for k in s:
      ss += dictoflatters[k]
print(ss)