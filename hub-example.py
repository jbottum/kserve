import os
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

HUGGINGFACEHUB_API_TOKEN = "put your HuggingFace Access Token here"

template = """Question: {question}
Answer: Let's think step by step."""

question = input("Enter your question: ")
prompt = template.format(question=question)
print(prompt)

# repo_id = "google/flan-t5-xl"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options
repo_id = "stabilityai/stablelm-tuned-alpha-3b"
llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature": 0, "max_length": 64}, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

try:
    result = llm_chain.run(question)
    print(result)
except Exception as e:
    print("Error occurred during execution:", str(e))

