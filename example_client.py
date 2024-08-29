import os
from openai import OpenAI

#import openlit
#openlit.init(otlp_endpoint="http://127.0.0.1:4318")


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
