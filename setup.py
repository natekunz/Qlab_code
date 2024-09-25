import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="strat_evaluator",  # Replace with your desired package name
    version="0.1.0",  # Initial release version
    author="Your Name",
    author_email="your.email@example.com",
    description="A class for evaluating trading strategies based on asset price data and signals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/strat_evaluator",  # Replace with your repository URL
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy>=1.18.0",
        "pandas>=1.0.0",
        "matplotlib>=3.0.0",
        "seaborn>=0.10.0",
        "yfinance>=0.1.54",
        "statsmodels>=0.12.0",
    ],
    include_package_data=True,  # Includes files specified in MANIFEST.in
    zip_safe=False,
)