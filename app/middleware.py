from flask import request

def before_request_middleware():
    print(f"Incoming request: {request.method} {request.url}")