# Author: Victor Hugo Lima Sanchez <limasanchezvictor@gmail.com>

import matplotlib.pyplot as plt
import numpy as np

font = {'family':'arial','color':'black','weight':'normal','size': 18}

#Foram feitos 10 testes e utilizado a média da acurácia

#Parte 2
algoritmo = ['L1 Logistic', 'L2(Multinomial)', 'L2(OvR)', 'Linear SVC', 'GPC']
acuracy1 = [83.12,82.7,79.3,82,82.7]
xs = [i + 0.5 for i, _ in enumerate(algoritmo)]
plt.bar(xs, acuracy1)

plt.xlabel('Algoritmos', fontdict=font)
plt.ylabel('Acuracia média', fontdict=font)

#Gerando graficos (Tutorial SckitLearn)
plt.title('PARTE 2 - 10 execuções', fontdict=font)
plt.xticks([i + 0.5 for i, _ in enumerate(algoritmo)], algoritmo)
plt.subplots_adjust(left=0.15)
plt.show()

#Gerando tabela - Parte 2
fig = plt.figure(dpi=130)
ax = fig.add_subplot(1,1,1)
table_data=[
    ["Execução", 1,2,3,4,5,6,7,8,9,10],
    ["L1 Logistic", 82.7,83.3,83.3,83.3,83.3,83.3,82.7,83.3,83.3,82.7],
    ["L2(Multinomial)", 82.7,82.7,82.7,82.7,82.7,82.7,82.7,82.7,82.7,82.7],
    ["L2(OvR)", 79.3,79.3,79.3,79.3,79.3,79.3,79.3,79.3,79.3,79.3],
    ["Linear SVC", 82,82,82,82,82,82,82,82,82,82],
    ["GPC", 82.7,82.7,82.7,82.7,82.7,82.7,82.7,82.7,82.7,82.7],
]
table = ax.table(cellText=table_data, loc='center')
table.set_fontsize(18)
table.scale(1,1)
plt.title('Parte 1 - 10 execuções\nAcurácia individual')
ax.axis('off')
plt.show()
