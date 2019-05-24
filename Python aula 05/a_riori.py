# =============================================================================
# pacote apyori
# =============================================================================

from apyori import apriori
import pandas as pd


dados = pd.read_csv('mercado2.csv', header = None)

# =============================================================================
# Transformar em transação
# =============================================================================

transacoes = []

for i in range(len(dados)):
    transacoes.append([str(dados.values[i, j]) for j in range(len(dados.columns))])

regras = apriori(transacoes, min_support = 0.003,
                 min_confidence = 0.2, min_lift = 3,
                 min_length = 2)

resultado = list(regras)

print(len(resultado))

resultados2 = [list(x) for x in resultado]

print(resultados2)

resultado_formatado = []

for j in range(0,len(resultado)):
    resultado_formatado.append([list(x) for x in resultados2[j][2]])

for r in resultado_formatado:
    print(r)
    print('----------------')