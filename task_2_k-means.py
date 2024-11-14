import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('Data_set/Mall_Customers.csv')

# Select relevant features
features = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-means clustering
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(scaled_features)

# Add the cluster labels to the original dataset
data['cluster'] = cluster_labels

print(data)

# Get centroids and transform them back to the original scale
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

# Visualize the clusters 
plt.figure(figsize=(10, 6))
scatter = plt.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'], 
                      c=data['cluster'], cmap='viridis', alpha=0.6, label='Customers')

# Plot centroids
plt.scatter(centroids[:, 1], centroids[:, 2], c='red', marker='X', s=200, label='Centroids')

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Customer Segments')
plt.colorbar(scatter, label='Cluster')
plt.legend()
plt.show()

