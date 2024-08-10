# Homepage of the documentation
# Project Documentation

Welcome to the documentation for the Advanced RAG on Semi-structured Data project.

## Overview

This project implements an advanced Retrieval-Augmented Generation (RAG) system to process semi-structured data from PDF documents. It utilizes state-of-the-art NLP techniques and integrates tools like `unstructured`, `LangChain`, and `Chromadb` to parse, classify, and retrieve content from documents effectively.

## Getting Started

To get started with this project, please follow the setup instructions in the README.md file at the root of this project repository.

## Components

The project is divided into several components:
- **PDF Parser**: Parses the PDF documents to extract text, tables, and images.
- **Data Processor**: Processes the raw data extracted from PDFs.
- **Element Classifier**: Classifies elements into text, tables, or images.
- **Summarizer**: Summarizes content using advanced NLP models.
- **Content Retriever**: Retrieves content based on queries using the multi-vector retrieval approach.
- **Storage Manager**: Manages the storage of processed data.
