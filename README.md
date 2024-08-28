# OPENAI REST API

This directory contains the source code to run and build docker images that run a FastAPI app
for serving inference from GPT4All models. The API matches the OpenAI API spec.

## Tutorial

The following tutorial assumes that you have checked out this repo and cd'd into it.

### Build the container

First change your working directory to `openai-api/api`.

Now you can build the FastAPI docker image. You only have to do this on initial build or when you add new dependencies to the requirements.txt file:
```bash
DOCKER_BUILDKIT=1 docker build -t openai_api --progress plain -f api/Dockerfile.buildkit .
```

### Setup the model you want served by the API

1. First copy the gguf version of the model you want served by the OpenAI-API server into api/models  (you can download one listed in app/models/models3.json)
1. Copy the env.example to .env and modify it to point to the model binary you just copied over to the api/models folder
1. Finally modify the example_client.py refer to the same binary model in the OpenAI chat completion

If you would like to convert any other Hugging face model into gguf, refer to this article here for more info: https://www.substratus.ai/blog/converting-hf-model-gguf-model/

### Start the API

Now that you have deployed the model binary and configured it, you can go ahead and start the backend with:

```bash
docker compose up --build
```

This will run both the API and locally hosted GPU inference server. If you want to run the API without the GPU inference server, you can run:

```bash
docker compose up --build openapi_api
```

To run the API with the GPU inference server, you will need to include environment variables (like the `MODEL_ID`). Edit the `.env` file and run
```bash
docker compose --env-file .env up --build
```

#### Spinning up your app
Run `docker compose up` to spin up the backend. Monitor the logs for errors in-case you forgot to set an environment variable above.


#### Running inference (tested on openai client version 1.41.0)
```python
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="not needed for a local LLM",
    base_url="http://localhost:4891/v1",

)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Who is Michael Jordan?",
        }
    ],
    #model="Meta-Llama-3-8B-Instruct.Q4_0",
    model="orca-mini-3b-gguf2-q4_0",
    #model="Phi-3-mini-4k-instruct.Q4_0",
    #model="lynx-8b-v1.1-2k",
    max_tokens=50,
    temperature=0.28,
    top_p=0.95,
    n=1,
    stream=False,
)

print(chat_completion)
```

#### Development
Run

```bash
docker compose up --build
```
and edit files in the `app` directory. The api will hot-reload on changes.

You can run the unit tests with

```bash
make test
```

#### Viewing API documentation

Once the FastAPI ap is started you can access its documentation and test the search endpoint by going to:
```
localhost:80/docs
```

This documentation should match the OpenAI OpenAPI spec located at https://github.com/openai/openai-openapi/blob/master/openapi.yaml
