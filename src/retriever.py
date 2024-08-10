# Class for retrieving document segments
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.embeddings import OpenAIEmbeddings
from langchain.storage import InMemoryStore
from langchain.vectorstores import Chroma

class ContentRetriever:
    def __init__(self, config):
        self.retriever = MultiVectorRetriever(
            vectorstore=Chroma(collection_name="summaries", embedding_function=OpenAIEmbeddings()),
            docstore=InMemoryStore(),
            id_key="doc_id"
        )

    def retrieve(self, query):
        return self.retriever.retrieve(query)
