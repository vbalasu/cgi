#!/opt/cgi-python/cgi_env/bin/python
print("Content-Type: text/plain\r\n")
print("Asking gemma3...")
from langchain_ollama import ChatOllama
llm = ChatOllama(model='gemma3:12b')
output = llm.invoke('What tree fits in your hand?').content
print(output)
