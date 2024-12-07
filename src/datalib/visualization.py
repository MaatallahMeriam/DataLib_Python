import matplotlib.pyplot as plt

def plot_bar(data, labels, title):
    """Crée un graphique en barres."""
    plt.bar(labels, data)
    plt.title(title)
    plt.show()

def plot_histogram(data, bins, title):
    """Crée un histogramme."""
    plt.hist(data, bins=bins)
    plt.title(title)
    plt.show()

def plot_scatter(x, y, title):
    """Crée un nuage de points."""
    plt.scatter(x, y)
    plt.title(title)
    plt.show()
