from setuptools import setup, find_packages

setup(
    name="datalib",
    version="0.1.0",
    author="Maatallah Meriam",
    author_email="mkdmeriam22@gmail.com",
    description="Une bibliothèque pour l'analyse et la manipulation de données",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MaatallahMeriam/DataLib",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "scipy"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
