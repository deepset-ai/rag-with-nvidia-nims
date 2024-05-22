# Build Air-Gapped RAG with Nvidia NIMs and Haystack

> Info: This repo is set up to use models hosted and accessible via https://build.nvidia.com/ 
> These models are already available and you can use them by creating yourself API keys through the platform.
> The project is set up so that you can change these models to NIM deployments by setting the `model` name and `api_url` in the `NvidiaGenerator`, `NvidiaDocumentEmbedder` and `NvidiaTextEmbedder` components.

## Run with Docker

1. `pip install -r requirements.txt`
2. Create a `.env` file and add `NVIDIA_API_KEY` (if you're using hosted models via https://build.nvidia.com/ then add an extra `NVIDIA_EMBEDDINGS_KEY` for embedding models)
3. `docker-compose up`
4. `pip install nvidia-haystack qdrant-haystack` in the hayhooks container
5. Run `python indexing.py` to preprocess and index `ChipNemo.pdf` into the Qdrant store made available in the `qdrant` container
6. `hayhooks deploy rag.yaml`

## File Structure

- indexing.py: This script preproecesses, embeds and writes ChipNemo.pdf into a Qdrant database
- rag.py: This scripts runs a RAG pipeline with a NIM LLM and retrieval model. 
- docker-compose.yml: This is the docker compose file we use to spin up a container for hayhooks (Haystack pipeline deployment) and Qdrant
- rag.yaml: This is the serialized RAG pipeline which is the same as `rag.py` in YAML. We use this to deploy our pipeline with hayhooks