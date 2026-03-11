import numpy as np

dados_int = np.random.randint(1, 101, 50)
dados_float = np.random.uniform(0, 10, 50)
print(f'dados_int: {dados_int}')
print(f'dados_float: {dados_float}')
print('')

x = np.sort(dados_int[dados_int % 2 == 0])
print(f'Números pares em dados_int: {x}')

y = np.sort(dados_int)
print(f'dados_int ordenado: {y}')

media = np.mean(dados_float)
mediana = np.median(dados_float)
desvio = np.std(dados_float)
max = np.max(dados_float)
min = np.min(dados_float)
print('')
print('Estatísticas de dados_float')
print(f'Média: {media}')
print(f'Mediana: {mediana}')
print(f'Desvio-padrão: {desvio}')
print(f'Máximo: {max}')
print(f'Mínimo: {min}')
print('')

soma_arrays = dados_int + dados_float
print(f'Soma dos dados: {soma_arrays}')
print(f'Média da soma dos dados: {np.mean(soma_arrays)}')
