FROM deepset/hayhooks:v0.0.15

EXPOSE 1416

RUN pip install pypdf qdrant-haystack nvidia-haystack

CMD ["hayhooks", "run", "--host", "0.0.0.0"]
