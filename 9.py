from sklearn.linear_model import LinearRegression
import pandas as pd
data = pd.DataFrame({
 'Age': [45, 50, 60, 35, 40],
 'BP': [120, 130, 140, 110, 115],
 'Chol': [200, 220, 250, 180, 190],
 'Risk': [1, 1, 1, 0, 0]
})
X = data[['Age', 'BP', 'Chol']]
y = data['Risk']
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[55, 135, 230]])
print("Predicted Value:", prediction)
if prediction[0] >= 0.5:
 print("Prediction: Disease Present")
else:
 print("Prediction: No Disease")