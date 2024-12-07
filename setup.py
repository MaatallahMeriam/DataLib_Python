from setuptools import setup, find_packages

setup(
    name="datalib",
    version="1.0.0",
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
    ],classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    keywords='data-analysis statistics machine-learning',
    python_requires=">=3.7",
    extras_require={
        'dev': ['pytest', 'sphinx']
    }
    
)
