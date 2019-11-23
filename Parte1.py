# Author: Victor Hugo Lima Sanchez <limasanchezvictor@gmail.com>

import matplotlib.pyplot as plt
from sklearn import datasets, metrics, svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Treino: %i' % label)
    
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

#Tutorial de introdução ao Scikit Learn
classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:n_samples//2], digits.target[:n_samples//2])
expected0 = digits.target[n_samples//2:]
predicted1 = classifier.predict(data[n_samples//2:])

#Algoritmo 1
clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)                                                     
#Dividindo as entradas e saídas (treino - 60% e teste - 40%)
train2, test2, train_labels2, test_labels2 = train_test_split(digits['data'], digits['target'], test_size=0.30, random_state=0)
clf.fit(train2, train_labels2)
predicted2 = clf.predict(test2)

#Algoritmo 2
knn = KNeighborsClassifier(n_neighbors = 1)
print(digits['target_names'])
#Dividindo as entradas e saídas (treino - 60% e teste - 40%)
train, test, train_labels, test_labels = train_test_split(digits['data'], digits['target'], test_size=0.30, random_state=0)
knn.fit(train, train_labels)
predicted3 = knn.predict(test)

#Dados da performance dos algoritmos (acuracia)
print("Dados do algoritmo SVC \n  %s:\n%s\n" % (classifier, metrics.classification_report(expected0, predicted1)))
print("Dados do algoritmo CLF \n  %s:\n%s\n" % (clf, metrics.classification_report(test_labels2, predicted2)))
print("Dados do algoritmo KNeighbors \n  %s:\n%s\n" % (knn, metrics.classification_report(test_labels, predicted3)))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted1))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Predição: %i' % prediction)

plt.show()
