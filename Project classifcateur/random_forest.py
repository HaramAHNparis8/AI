import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

file_path = 'DATA.csv'
df = pd.read_csv(file_path)
noms = [
    "age", "gender", "graduated-high-school-type", "scholarship-type",
    "add-work", "artistic-sport-activity", "partner", "salary",
    "transportation", "accomodation", "mother-education", "father-education",
    "siblings", "parental-status", "mother-occupation", "father-occupation",
    "weekly-study-hours", "reading", "frequency-non-scientific",
    "ready-frequency-scientific", "attendance-seminars", "impact-projects",
    "attendance-class", "prep-midterm-1", "prep-midterm-2", "taking-note",
    "listening-class", "discussion", "flip-classroom",
    "average-grade-lastsemester", "expected-grade", "course-id", "output-grade"
]
df.columns = noms

X = df.drop(['age', 'output-grade'], axis=1)
y = df['output-grade']

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=42)

rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

feature_importances = rf_classifier.feature_importances_

importances_df = pd.DataFrame({
    'feature': X.columns,
    'importance': feature_importances
})
importances_df.sort_values(by='importance', ascending=False, inplace=True)

print(importances_df.head())

