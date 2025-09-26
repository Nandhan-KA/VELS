# STEP 1: Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# STEP 2: Create some random data (like student scores)
X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
print(X)
# STEP 3: Apply K-Means (we want 3 groups)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
print(kmeans)
# STEP 4: Get labels (which group each point belongs to)
labels = kmeans.labels_

# STEP 5: Plot
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            color='red', marker='X', s=200, label="Centers")
plt.title("K-Means Clustering")
plt.legend()
plt.show()
