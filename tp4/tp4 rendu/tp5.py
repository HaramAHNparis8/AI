import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


iris_learn_data = np.array([
    [5.1, 3.3, 1.7, 0.5],
    [6.4, 2.9, 4.3, 1.3],
    [5.4, 3.4, 1.5, 0.4],
    [7.7, 2.6, 6.9, 2.3],
    [4.9, 2.4, 3.3, 1.0],
    [7.9, 3.8, 6.4, 2.0],
    [6.7, 3.1, 4.4, 1.4],
    [5.2, 4.1, 1.5, 0.1],
    [6.0, 3.0, 4.8, 1.8],
    [5.8, 4.0, 1.2, 0.2],
    [7.7, 2.8, 6.7, 2.0],
    [5.1, 3.8, 1.5, 0.3],
    [4.7, 3.2, 1.6, 0.2],
    [7.4, 2.8, 6.1, 1.9],
    [5.0, 3.3, 1.4, 0.2],
    [6.3, 3.4, 5.6, 2.4],
    [5.7, 2.8, 4.1, 1.3],
    [5.8, 2.7, 3.9, 1.2],
    [5.7, 2.6, 3.5, 1.0],
    [6.4, 3.2, 5.3, 2.3],
    [6.7, 3.0, 5.2, 2.3],
    [6.3, 2.5, 4.9, 1.5],
    [6.7, 3.0, 5.0, 1.7],
    [5.0, 3.0, 1.6, 0.2],
    [5.5, 2.4, 3.7, 1.0],
    [6.7, 3.1, 5.6, 2.4],
    [5.8, 2.7, 5.1, 1.9],
    [5.1, 3.4, 1.5, 0.2],
    [6.6, 2.9, 4.6, 1.3],
])

iris_test_data = np.array([
    [5.6, 3.0, 4.1, 1.3],
    [5.9, 3.2, 4.8, 1.8],
    [6.3, 2.3, 4.4, 1.3],
    [5.5, 3.5, 1.3, 0.2],
    [5.1, 3.7, 1.5, 0.4],
    [4.9, 3.1, 1.5, 0.1],
    [6.3, 2.9, 5.6, 1.8],
    [5.8, 2.7, 4.1, 1.0],
    [7.7, 3.8, 6.7, 2.2],
    [4.6, 3.2, 1.4, 0.2],
])


iris_learn_label = np.array([
    2, 1, 0, 2, 0, 2, 0, 1, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 0, 0, 2, 1, 0, 0, 2, 0, 0, 1, 1, 0, 2, 1, 0, 2, 2, 1, 0, 1, 1, 1, 2, 0, 2, 0, 0, 1, 2, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 1, 0, 2, 1, 1, 1, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 2, 1, 0, 1, 2, 1, 0, 2, 2, 2, 2, 0, 0, 2, 2, 0, 2, 0, 2, 2, 0, 0, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 1, 1, 0, 0, 1, 0, 2, 1, 2, 1, 0, 2, 0, 2, 0, 0, 2, 0, 2, 1, 1, 1, 2, 2, 1, 1, 0, 1, 2, 2, 0, 1,
])

iris_test_label = np.array([
    1, 1, 1, 0, 0, 0, 2, 1, 2, 0,
])


k_values = list(range(2, 11))
best_accuracy = 0
best_k = 0

for k in k_values:
    knn_classifier = KNeighborsClassifier(n_neighbors=k)
    knn_classifier.fit(iris_learn_data, iris_learn_label)

    
    predictions = knn_classifier.predict(iris_test_data)
    accuracy = accuracy_score(iris_test_label, predictions)

    #

