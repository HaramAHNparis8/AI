import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'DATA.csv'
df_uploaded = pd.read_csv(file_path)


X = df_uploaded.drop(['STUDENT ID', 'GRADE'], axis=1)
y = df_uploaded['GRADE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train, y_train)


y_pred = svm_classifier.predict(X_test)

report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(report)
print(conf_matrix)


plt.figure(figsize=(20, 15))
for i, col in enumerate(X.columns):
    plt.subplot(7, 5, i + 1)
    sns.histplot(X[col], kde=True)
    plt.title(col)
    plt.tight_layout()
plt.show()


