import numpy as np
dados_temp = np.random.normal(22, 4, 1000)
dados_co2 = np.random.normal(400, 50, 1000)

filtro = (dados_temp > 28) & (dados_co2 > 450)

temp_critico = dados_temp[filtro]
co2_critico = dados_co2[filtro]

quantidade = len(temp_critico)
percentagem = (quantidade/1000) * 100

print(quantidade)
print(percentagem)