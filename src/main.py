# Main application entry point

from src.pdf_parser import PDFParser
from src.data_processing import DataProcessor
from src.element_classifier import ElementClassifier
from src.summarizer import Summarizer
from src.retriever import ContentRetriever
from src.storage import StorageManager
from src.config import Configuration

def main():
    config = Configuration()
    parser = PDFParser(config)
    processor = DataProcessor(config)
    classifier = ElementClassifier(config)
    summarizer = Summarizer(config)
    retriever = ContentRetriever(config)
    storage = StorageManager(config)

    # Example workflow
    pdf_data = parser.parse("your_pdf_file.pdf")
    processed_data = processor.process(pdf_data)
    elements = classifier.classify(processed_data)
    summaries = summarizer.summarize(elements)
    retriever.retrieve(summaries)
    storage.save(summaries)

if __name__ == "__main__":
    main()
