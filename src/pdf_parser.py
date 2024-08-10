# Class for parsing PDF files
from unstructured.partition.pdf import partition_pdf

class PDFParser:
    def __init__(self, config):
        self.config = config

    def parse(self):
        return partition_pdf(
            filename=self.config.PDF_PATH,
            extract_images_in_pdf=True,
            infer_table_structure=True,
            chunking_strategy="by_title",
            max_characters=4000,
            new_after_n_chars=3800,
            combine_text_under_n_chars=2000,
            image_output_dir_path="."
        )
