import math
from collections import Counter
data = [
 ("Red", "Big", "Apple"),
 ("Red", "Small", "Apple"),
 ("Yellow", "Big", "Banana"),
 ("Yellow", "Small", "Banana"),
 ("Green", "Big", "Apple")
]
def entropy(data):
 labels = Counter(row[2] for row in data)
 total = len(data)
 return -sum((c/total) * math.log2(c/total) for c in labels.values())
def gini(data):
 labels = Counter(row[2] for row in data)
 total = len(data)
 return 1 - sum((c/total) ** 2 for c in labels.values())
def bayes_predict(test):
 classes = Counter(row[2] for row in data)
 probs = {}
 for c in classes:
 probs[c] = classes[c] / len(data)
 for i in range(len(test)):
 match = sum(1 for row in data if row[i] == test[i] and row[2] == c)
 probs[c] *= (match + 1) / (classes[c] + 2)
 return max(probs, key=probs.get)
test = ("Yellow", "Big")
print("Predicted Fruit:", bayes_predict(test))
print("Entropy:", entropy(data))
print("Gini Index:", gini(data))