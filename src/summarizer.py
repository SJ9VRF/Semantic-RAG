# Class for summarizing content
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

class Summarizer:
    def __init__(self, config):
        self.config = config
        self.model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    def summarize(self, elements):
        prompt_template = """
        Summarize this content concisely:
        {element}
        """
        prompt = ChatPromptTemplate.from_template(prompt_template)
        summaries = [prompt(element) | self.model | StrOutputParser() for element in elements]
        return summaries
