import numpy as np
import scipy.stats as stats

def calculate_mean(data):
    """Calcule la moyenne."""
    return np.mean(data)

def calculate_median(data):
    """Calcule la médiane."""
    return np.median(data)

def calculate_mode(data):
    """Calcule le mode."""
    mode_result = stats.mode(data)
    return mode_result.mode[0]

def calculate_std(data):
    """Calcule l'écart-type."""
    return np.std(data)

def calculate_correlation(x, y):
    """Calcule la corrélation entre deux séries."""
    return np.corrcoef(x, y)[0, 1]
