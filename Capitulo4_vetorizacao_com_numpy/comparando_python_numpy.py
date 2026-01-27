#%%
import numpy as np
import math
import time

#OBJETIVO: comparar a velocidade de contas matemáticas em ndarrays do Numpy e listas no Python, para enteder a fundo a importância dessa biblioteca matemática

#%%
precos_np = np.random.rand(10_000_000)
type(precos_np)
#%%
precos_lista = list(precos_np)
type(precos_lista)
#%%

#Operações com Numpy
t0 = time.time()
desc = precos_np * 0.90
final = desc + 5
raiz = np.sqrt(precos_np)
print("Numpy: ",time.time() - t0," segundos")

#Operações com Python puro
t0 = time.time()
desc = [p * 0.90 for p in precos_lista]
final = [p + 5 for p in desc]
raiz = [math.sqrt(p) for p in final]
print("Python: ",time.time() - t0," segundos")
# %%


#Para 10 milhões de valores, o NumPy normalmente é muito mais rápido. Mas para poucos valores, o uso de loops com Python puro pode sair na frente porque o overhead do NumPy pesa mais que o ganho para poucos registros.

#✅ Resumindo:

#- Poucos elementos → Loops Python podem ser mais rápidos (overhead do NumPy é maior).

#- Muitos elementos → NumPy é muito mais rápido e escalável.
