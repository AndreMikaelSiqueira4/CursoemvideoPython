from random import choice
nomes = choice(['Carlos', 'Pedro', 'Junior', 'Shrek'])
print(f'Quem vai limpar o quadro vai ser o {nomes}')
"Sem Interaçao"



"Com Interaçao"
n1 = str(input('Primeiro aluno: ')) 
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto Aluno: '))

lista = [n1,n2,n3,n4]
escolhido = choice(lista)

print(f'O Escolhido foi {escolhido}')