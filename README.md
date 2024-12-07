# DataLib: Python Data Analysis Library

## Overview

DataLib is a comprehensive Python library designed to simplify data manipulation, statistical analysis, visualization, and machine learning tasks. It provides an intuitive and powerful set of tools for data scientists, researchers, and analysts.

## Features

### Data Manipulation
- CSV file loading and saving
- Data filtering
- Missing value handling
- Data normalization

### Statistical Analysis
- Descriptive statistics
- Correlation analysis
- T-tests
- Chi-square tests

### Data Visualization
- Bar plots
- Histograms
- Scatter plots
- Correlation heatmaps

### Advanced Analysis
- Linear and Polynomial Regression
- Classification Algorithms (KNN, Decision Trees)
- Clustering (K-means)
- Dimensionality Reduction (PCA)

## Installation

```bash
pip install datalib
```

## Quick Examples

### Data Manipulation
from datalib.data_processing import load_csv, normalize_column
from datalib.statistics import StatisticalAnalysis

# Charger un fichier CSV
df = load_csv("data.csv")

# Normaliser une colonne
normalized_df = normalize_column(df, "age")

# Analyser les statistiques descriptives
stats = StatisticalAnalysis(df)
print(stats.mean("age"))
