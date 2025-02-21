napis = "Ala ma kota"

print(napis[::2])
print(napis[::-1])


print(dir(napis))
"""
 'capitalize', 'casefold', 'center', 'count', 'encode',
 'endswith', 'expandtabs', 'find', 'format', 'format_map',
  'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
  'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
  'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
  'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
  'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
  'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'
"""

help(napis.casefold)

print("ẞ".lower())
print("ẞ".casefold())
