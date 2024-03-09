import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np


file_path = 'DATA.csv'
df = pd.read_csv(file_path)


X = df.drop(['STUDENT ID', 'GRADE'], axis=1)
y = df['GRADE']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


rf_regressor = RandomForestRegressor(random_state=42)
rf_regressor.fit(X_train, y_train)


y_pred_rf_reg = rf_regressor.predict(X_test)
mse_rf = mean_squared_error(y_test, y_pred_rf_reg)
r2_rf = r2_score(y_test, y_pred_rf_reg)


svr_model = make_pipeline(StandardScaler(), SVR(kernel='linear'))
svr_model.fit(X_train, y_train)


y_pred_svr = svr_model.predict(X_test)
mse_svr = mean_squared_error(y_test, y_pred_svr)
r2_svr = r2_score(y_test, y_pred_svr)


kf = KFold(n_splits=5, shuffle=True, random_state=42)


rf_cv_scores = cross_val_score(rf_regressor, X, y, cv=kf, scoring='neg_mean_squared_error')
rf_cv_mse = -rf_cv_scores.mean()
rf_cv_r2 = cross_val_score(rf_regressor, X, y, cv=kf, scoring='r2').mean()


svr_cv_scores = cross_val_score(svr_model, X, y, cv=kf, scoring='neg_mean_squared_error')
svr_cv_mse = -svr_cv_scores.mean()
svr_cv_r2 = cross_val_score(svr_model, X, y, cv=kf, scoring='r2').mean()


print("Random Forest Regressor Performance:")
print("Mean Squared Error:", mse_rf)
print("R-squared:", r2_rf)
print("Cross-Validation MSE:", rf_cv_mse)
print("Cross-Validation R-squared:", rf_cv_r2)

print("\nSVR Performance:")
print("Mean Squared Error:", mse_svr)
print("R-squared:", r2_svr)
print("Cross-Validation MSE:", svr_cv_mse)
print("Cross-Validation R-squared:", svr_cv_r2)


models = ['Random Forest', 'SVR']
mse_values = [rf_cv_mse, svr_cv_mse]
r2_values = [rf_cv_r2, svr_cv_r2]

x = np.arange(len(models)) 
width = 0.35  

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mse_values, width, label='MSE')
rects2 = ax.bar(x + width/2, r2_values, width, label='R-Squared')

ax.set_ylabel('Scores')
ax.set_title('MSE and R-Squared Scores by Model')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()

