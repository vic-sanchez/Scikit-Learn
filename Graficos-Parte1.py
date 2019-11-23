# Author: Victor Hugo Lima Sanchez <limasanchezvictor@gmail.com>

import matplotlib.pyplot as plt
import numpy as np

font = {'family':'arial','color':'black','weight':'normal','size': 18}

#Foram feitos 10 testes e utilizado a média da acurácia

#Parte 1
algoritmo = ['SVC', 'CLF', 'KNeighbors']
acuracy1 = [97,91,99]
xs = [i + 0.5 for i, _ in enumerate(algoritmo)]
plt.bar(xs, acuracy1)

plt.xlabel('Algoritmos', fontdict=font)
plt.ylabel('Acuracia média', fontdict=font)

#Gerando graficos (Tutorial SckitLearn) - Parte 1
plt.title('PARTE 1 - 10 execuções', fontdict=font)
plt.xticks([i + 0.5 for i, _ in enumerate(algoritmo)], algoritmo)
plt.subplots_adjust(left=0.15)
plt.show()

#Gerando tabela - Parte 1
fig = plt.figure(dpi=130)
ax = fig.add_subplot(1,1,1)
table_data=[
    ["Execução", 1,2,3,4,5,6,7,8,9,10],
    ["SVC", 97,97,97,97,97,97,97,97,97,97],
    ["CLF", 89,94,91,91,90,91,87,91,94,92],
    ["KNeighbors", 99,99,99,99,99,99,99,99,99,99],
]
table = ax.table(cellText=table_data, loc='center')
table.set_fontsize(18)
table.scale(1,1)
plt.title('Parte 1 - 10 execuções\nAcurácia individual')
ax.axis('off')
plt.show()
