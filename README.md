# nvidia-haystack

1. `pip install -r requirements.txt`
2. Export `OPENAI_API_KEY` (skip this if you're not using OpenAI compoents if you want)
3. Export `NVIDIA_API_KEY`
4. Run `python rag-qa.py`

> Ignore `indexing.py` for now

To get an API key:
- go to build.nvidia.com
- pick a model
- generate an API key
- change the `NvidiaGenerator` accordingly