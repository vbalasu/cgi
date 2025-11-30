#!/opt/cgi-python/cgi_env/bin/python
print("Content-Type: text/plain\r\n")
import os
from urllib.parse import parse_qs
from langchain_ollama import ChatOllama

query_string = os.environ.get('QUERY_STRING', '')
params = parse_qs(query_string)
question = params.get('q', ['What tree fits in your hand?'])[0]

llm = ChatOllama(model='gemma3:12b')
output = llm.invoke(question).content
print(output)