import pandas as pd
data = pd.read_csv("CE_DS1.csv")
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
S = ['Ø'] * len(X[0])
G = ['?'] * len(X[0])
for i in range(len(X)):
 if y[i] == 'Yes': # Positive example
 for j in range(len(S)):
 if S[j] == 'Ø':
 S[j] = X[i][j]
 elif S[j] != X[i][j]:
 S[j] = '?'
 else: # Negative example
 for j in range(len(G)):
 if G[j] == '?' and S[j] != X[i][j]:
 G[j] = S[j]
print("Specific Boundary (S):", S)
print("General Boundary (G):", G)