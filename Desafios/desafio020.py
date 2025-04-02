from random import shuffle,randrange
nomes = ['Pedrinho', 'TremBala', 'Paulao', 'Shrek3']
ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
shuffle(nomes)
for nome, ordem in zip(nomes,ordem):
    print(f'{nome} vai apresentar em {ordem}')
"Sem interaçao"
