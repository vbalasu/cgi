# cgi

Create simple CGI scripts using python or bash

You can create mini "serverless" endpoints that execute a script in response to a HTTP request

Here are a few examples:

1. env.sh - Print the environment variables. You can examine the QUERY_STRING being passed in
2. man.sh - Prints the man page for a command in plain text format
3. app.py - Basic python script that uses Bottle, calls an LLM (using Ollama) and returns the response

You can test the CGI scripts locally by running:
```
python -m http.server --cgi
```

And visiting your script by pointing your browser to `http://localhost:PORT/cgi-bin/YOUR_SCRIPT`
