import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import requests
from io import StringIO

def calculate_shannon_entropy(y):
    if len(y) == 0:
        return 0
    label_counts = np.bincount(y)
    probabilities = label_counts / len(y)
    entropy = -np.sum([p * np.log2(p) for p in probabilities if p > 0])
    return entropy

def best_split(X, y):
    best_entropy = float('inf')
    best_feature = None
    best_threshold = None

    for feature in X.columns:
        thresholds = X[feature].unique()
        for threshold in thresholds:
            left_mask = X[feature] == threshold
            right_mask = ~left_mask

            left_entropy = calculate_shannon_entropy(y[left_mask])
            right_entropy = calculate_shannon_entropy(y[right_mask])

            total_entropy = (len(y[left_mask]) / len(y)) * left_entropy + (len(y[right_mask]) / len(y)) * right_entropy

            if total_entropy < best_entropy:
                best_entropy = total_entropy
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold


data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer.data'
response = requests.get(data_url)
data_str = response.content.decode('utf-8')


columns = [
    'Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps',
    'deg-malig', 'breast', 'breast-quad', 'irradiat'
]


data = pd.read_csv(StringIO(data_str), names=columns)


le = LabelEncoder()
data['Class'] = le.fit_transform(data['Class'])


for column in data.columns:
    if data[column].dtype == 'object':
        data[column] = data[column].astype('category')
        data[column] = data[column].cat.codes


X = data.drop('Class', axis=1)
y = data['Class']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


best_feature, best_threshold = best_split(X_train, y_train)
print(f'Best Split: {best_feature}, Threshold: {best_threshold}')


X_test_split = X_test[best_feature] == best_threshold
y_pred = np.where(X_test_split, 1, 0)


accuracy = np.mean(y_pred == y_test)
print(f'acuremce: {accuracy}')
