import numpy as np
import matplotlib.pyplot as plt
def lwr(X, y, xq, tau):
 m = X.shape[0]
 W = np.eye(m)
 for i in range(m):
 d = X[i] - xq
 W[i, i] = np.exp(-(d @ d) / (2 * tau**2))
 theta = np.linalg.pinv(X.T @ W @ X) @ X.T @ W @ y
 return xq @ theta
# Data
X = np.linspace(-3, 3, 100).reshape(-1, 1)
y = np.sin(X) + np.random.normal(0, 0.1, (100, 1))
X = np.c_[np.ones(100), X]
X_test = np.c_[np.ones(100), np.linspace(-3, 3, 100).reshape(-1, 1)]
# Prediction
tau = 0.3
y_pred = np.array([lwr(X, y, x, tau) for x in X_test]).ravel()
# Plot
plt.scatter(X[:, 1], y, color='red', label="Data")
plt.plot(X_test[:, 1], y_pred, color='blue', label="LWR Fit")
plt.legend()
plt.show()