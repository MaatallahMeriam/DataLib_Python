from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def linear_regression(X, y):
    """Applique une régression linéaire."""
    model = LinearRegression()
    model.fit(X, y)
    return model

def kmeans_clustering(X, n_clusters):
    """Applique le clustering k-means."""
    model = KMeans(n_clusters=n_clusters)
    model.fit(X)
    return model

def perform_pca(X, n_components):
    """Applique une Analyse en Composantes Principales (PCA)."""
    pca = PCA(n_components=n_components)
    return pca.fit_transform(X)
