'''
Algoritmo em Python
Por Roseneide Santos
Data: 28/04/22
'''

vol_utilizados = []
contador = 0
soma_volumes = 0
vol_extra = ''
vol_resto = 0

vol_galao = float(input('Qual o volume do galão?: '))
qtd_garrafas = int(input('> Informe a quantidade de garrafas: '))

for i in range(qtd_garrafas):
  contador = contador + 1
  vol_garrafas = float(input(f'> Informe o volume da {contador}º garrafa: '))
  soma_volumes += vol_garrafas
  vol_utilizados.append(vol_garrafas)

if soma_volumes > vol_galao:
  vol_resto = soma_volumes - vol_galao
  vol_necessario = vol_garrafas - vol_resto
  soma_volumes = soma_volumes - vol_resto
  vol_utilizados.pop()
  vol_utilizados.append(vol_necessario)

print(f'\n RESULTADO: O enchimento do galão totalizou {soma_volumes:.0f}L utilizando os volumes: {vol_utilizados} e sobrou {vol_resto:.0f}L')