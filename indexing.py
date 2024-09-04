from haystack import Pipeline
from haystack.utils.auth import Secret
from haystack.components.converters import PyPDFToDocument
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentCleaner, DocumentSplitter
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from haystack_integrations.components.embedders.nvidia import NvidiaDocumentEmbedder

document_store = QdrantDocumentStore(embedding_dim=1024, host="qdrant")

converter = PyPDFToDocument()

cleaner = DocumentCleaner()

splitter = DocumentSplitter(split_by='word', split_length=100)

embedder = NvidiaDocumentEmbedder(model="snowflake/arctic-embed-l", 
                                  api_url="https://ai.api.nvidia.com/v1/retrieval/snowflake/arctic-embed-l",
                                  batch_size=1)

writer = DocumentWriter(document_store)

indexing = Pipeline()
indexing.add_component("converter", converter)
indexing.add_component("cleaner", cleaner)
indexing.add_component("splitter", splitter)
indexing.add_component("embedder", embedder)
indexing.add_component("writer", writer)

indexing.connect("converter", "cleaner")
indexing.connect("cleaner", "splitter")
indexing.connect("splitter", "embedder")
indexing.connect("embedder", "writer")

if __name__=="__main__":
    indexing.run({"converter": {"sources": ["/hayhooks/ChipNeMo.pdf"]}})