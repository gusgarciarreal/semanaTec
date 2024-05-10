import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Cargar datos
archivo = pd.read_csv("twitter_dataset.csv")

# Convertir la columna 'Timestamp' al formato datetime
archivo["Timestamp"] = pd.to_datetime(archivo["Timestamp"])

# Estadísticas resumidas
print(archivo.head())

# Quitar columnas no numéricas
archivo = archivo.drop(columns=['Tweet_ID', 'Username', 'Text', 'Timestamp'])

# Determinar k utilizando el método del codo
inercia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=60)
    kmeans.fit(archivo[['Retweets', 'Likes']])
    inercia.append(kmeans.inertia_)

plt.plot(range(1, 11), inercia, marker='o')
plt.xlabel('Clusters')
plt.title('Valores de Inercia vs. Clusters')
plt.show()

# centros del algoritmo k-means con scikit-learn
kmeans = KMeans(n_clusters=3, random_state=42) # Usando k=3
kmeans.fit(archivo[['Retweets', 'Likes']])
centers = kmeans.cluster_centers_
print("Centros:")
print(centers)

X = archivo[['Retweets', 'Likes']]
archivo['Cluster'] = kmeans.labels_

# Visualización de los clusters
plt.figure(figsize=(10, 6))
plt.scatter(archivo['Retweets'], archivo['Likes'], c=archivo['Cluster'], cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200)
plt.xlabel('Retweets')
plt.ylabel('Likes')
plt.title('Clusters de Retweets y Likes')
plt.show()