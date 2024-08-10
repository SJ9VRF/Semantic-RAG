# Setup script for the package
from setuptools import setup, find_packages

setup(
    name='advanced_rag',
    version='0.1.0',
    description='Advanced RAG system for processing semi-structured data from PDF documents',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'unstructured[all-docs]',
        'langchain',
        'pydantic',
        'lxml',
        'openai',
        'chromadb',
        'tiktoken'
    ],
    entry_points={
        'console_scripts': [
            'advanced_rag=src.main:main',
        ],
    },
)
