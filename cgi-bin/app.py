#!/usr/bin/env python
from bottle import Bottle, run

app = Bottle()

@app.route('/')
def home():
    return {"message": get_response("What tree fits in your hand?")}

def get_response(query):
    from langchain_ollama import ChatOllama
    llm = ChatOllama(model="gemma3:12b")
    return llm.invoke(query).content

#run(app, host='localhost', port=8088)
run(app, server='cgi')
