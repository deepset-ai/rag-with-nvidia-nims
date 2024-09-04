# Build Air-Gapped RAG with Nvidia NIMs and Haystack

📚 This repository is accompanied by our article ["Building RAG Applications with NVIDIA NIM and Haystack on K8s"](https://haystack.deepset.ai/blog/haystack-nvidia-nim-rag-guide)

> Info: This repo is set up to use models hosted and accessible via https://build.nvidia.com/ 
>
> These models are already available and you can use them by creating yourself API keys through the platform.
> The project is set up so that you can change these models to NIM deployments by setting the `model` name and `api_url` in the `NvidiaGenerator`, `NvidiaDocumentEmbedder` and `NvidiaTextEmbedder` components.
> 
> 👩🏻‍🍳 We also provide a notebook on Haystack Cookbooks that provide the same code and setup, only expecting self-hosted NIMs
> 
> <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/rag-with-nims.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Run with Docker

1. `pip install -r requirements.txt`
2. Create a `.env` file and add `NVIDIA_API_KEY` (if you're using hosted models via https://build.nvidia.com/)
3. `docker-compose up`
6. `hayhooks deploy rag.yaml`
7. Go to `localhost:1416/docs` to interact with your RAG pipeline

## File Structure

- `indexing.py`: This script preproecesses, embeds and writes ChipNemo.pdf into a Qdrant database
- `rag.py`: This scripts runs a RAG pipeline with a NIM LLM and retrieval model. 
- `Dockerfile`: This is used by the docker-compose file to install dependencies
- `docker-compose.yml`: This is the docker compose file we use to spin up a container for hayhooks (Haystack pipeline deployment) and Qdrant
- `rag.yaml`: This is the serialized RAG pipeline which is the same as `rag.py` in YAML. We use this to deploy our pipeline with hayhooks
-  <a href="https://colab.research.google.com/github/deepset-ai/haystack-cookbook/blob/main/notebooks/rag-with-nims.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>: This notebook shows you how you can set up your components to use self-hosted NIMs.