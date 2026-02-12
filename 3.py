import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
data = pd.read_csv("DATA.csv")
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans_labels = kmeans.fit_predict(data)
em = GaussianMixture(n_components=2, random_state=0)
em_labels = em.fit_predict(data)
kmeans_score = silhouette_score(data, kmeans_labels)
em_score = silhouette_score(data, em_labels)
print("k-Means Silhouette Score:", kmeans_score)
print("EM Silhouette Score:", em_score)
if em_score > kmeans_score:
 print("EM algorithm produces better clustering.")
else:
 print("k-Means produces comparable clustering.")