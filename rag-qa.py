from haystack import Pipeline
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
from haystack.components.generators import OpenAIGenerator
from haystack.components.builders import PromptBuilder

fetcher = LinkContentFetcher()
converter = HTMLToDocument()
prompt = """Answer the question given the context.
Context:
{{ documents }}
Question: {{ query }}
Answer:"""
prompt_builder = PromptBuilder(template=prompt)
generator = OpenAIGenerator()

rag = Pipeline()
rag.add_component("fetcher", fetcher)
rag.add_component("converter", converter)
rag.add_component("prompt", prompt_builder)
rag.add_component("generator", generator)

rag.connect("fetcher.streams", "converter.sources")
rag.connect("converter.documents", "prompt.documents")
rag.connect("prompt", "generator")

while True:
    question = input("Ask a question:\n")
    result = rag.run({"fetcher": {"urls": ["https://haystack.deepset.ai/integrations/nvidia"]},
                      "prompt": {"query": question}})
    print(result["generator"]["replies"][0])