from haystack import Pipeline
from haystack.utils.auth import Secret
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.embedders.nvidia import NvidiaTextEmbedder
from haystack_integrations.components.generators.nvidia import NvidiaGenerator
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore

document_store = QdrantDocumentStore(embedding_dim=1024, host="qdrant")

embedder = NvidiaTextEmbedder(model="snowflake/arctic-embed-l", 
                                  api_key=Secret.from_env_var("NVIDIA_EMBEDDINGS_KEY"), 
                                  api_url="https://ai.api.nvidia.com/v1/retrieval/snowflake/arctic-embed-l")

retriever = QdrantEmbeddingRetriever(document_store=document_store)

prompt = """Answer the question given the context.
Question: {{ query }}
Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}
Answer:"""
prompt_builder = PromptBuilder(template=prompt)

generator = NvidiaGenerator(
    model="meta/llama3-70b-instruct",
    api_url="https://integrate.api.nvidia.com/v1",
    model_arguments={
        "max_tokens": 1024
    }
)

rag = Pipeline()
rag.add_component("embedder", embedder)
rag.add_component("retriever", retriever)
rag.add_component("prompt", prompt_builder)
rag.add_component("generator", generator)

rag.connect("embedder.embedding", "retriever.query_embedding")
rag.connect("retriever.documents", "prompt.documents")
rag.connect("prompt", "generator")

with open("rag.yaml", "w") as f: 
    rag.dump(f)

while True:
    question = input("Ask a question:\n")
    result = rag.run(
        {
            "embedder": {"text": question},
            "prompt": {"query": question},
        }, include_outputs_from=["prompt"]
    )
    print(result["generator"]["replies"][0])
