from haystack import Pipeline
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack_integrations.document_stores.chroma import ChromaDocumentStore
from haystack.components.embedders import OpenAIDocumentEmbedder

document_store = ChromaDocumentStore()

fetcher = LinkContentFetcher()
converter = HTMLToDocument()
cleaner = DocumentCleaner()
splitter = DocumentSplitter()
embedder = OpenAIDocumentEmbedder()
writer = DocumentWriter(document_store)

indexing = Pipeline()
indexing.add_component("fetcher", fetcher)
indexing.add_component("converter", converter)
indexing.add_component("embedder", embedder)
indexing.add_component("writer", writer)

indexing.connect("fetcher", "converter")
indexing.connect("converter", "embedder")
indexing.connect("embedder", "writer")

while True:
    url = input("URL to index")
    result = indexing.run({"fetcher": {"urls": [url]}})
    print(result)