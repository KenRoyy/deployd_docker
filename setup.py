from setuptools import setup, find_packages


setup(
    name="edu_pad",
    version="0.0.1",
    author="Andres Callejas",
    author_email="andres.callejas@iudigital.edu.co",
    description="ETL para análisis de datos del dólar",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
        "sqlite3-simple"
    ]
)