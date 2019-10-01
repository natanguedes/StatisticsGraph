
from pandas import DataFrame



data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'],
        'Ano': [2002, 2003, 2004, 2005, 2006],
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)
print(frame)
frame