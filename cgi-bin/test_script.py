#!/opt/cgi-python/cgi_env/bin/python
import os
import sys

# Crucial: Output the required HTTP headers first
print("Content-Type: text/plain\r\n") 
# The extra \r\n (or two blank lines) separates headers from body.

print("CGI Script Test Status: OK")
print(f"User running the script: {os.environ.get('USER')}")
print(f"Interpreter path: {sys.executable}")