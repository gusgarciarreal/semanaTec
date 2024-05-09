import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo = pd.read_csv("arteDeLaAnalitica\twitter_dataset.csv")

# Convertir la columna 'Timestamp' al formato datetime
archivo["Timestamp"] = pd.to_datetime(archivo["Timestamp"])

# Estadísticas resumidas
print(archivo.describe())

# Diagramas de caja y bigotes
plt.figure(figsize=(10, 6))
sns.boxplot(data=archivo, x="Retweets", y="Likes")
plt.title("Diagramas de Caja de Retweets y Likes")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=archivo, x="Likes", y="Retweets")
plt.title("Diagramas de Caja de Likes y Retweets")
plt.show()

# Histogramas
plt.figure(figsize=(10, 6))
sns.histplot(data=archivo, x="Retweets", bins=50, color="skyblue")
plt.title("Histograma de Retweets")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=archivo, x="Likes", bins=50, color="salmon")
plt.title("Histograma de Likes")
plt.show()

# Diagramas de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(data=archivo, x="Retweets", y="Likes", color="green")
plt.title("Diagrama de Dispersión de Retweets y Likes")
plt.show()

# Mapa de calor
plt.figure(figsize=(10, 6))
sns.heatmap(archivo[["Retweets", "Likes", "Timestamp"]].corr(), annot=True, cmap="Purples")
plt.title("Mapa de Calor de Correlaciones")
plt.show()