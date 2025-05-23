# 4. Custom Middleware (20 minutes)
# Task:
# Write a custom Django middleware to log request data into a file.
# Requirements:
# 1. Log the following details for each request:
# o URL
# o HTTP method
# o ExecuƟon Ɵme (in milliseconds)
# 2. Save the log in a file called request_logs.txt.


from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import time

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        start_time = time.time()
        request.start_time = start_time


    def process_response(self, request, response):
        end_time = time.time()
        execution_time = int((end_time - request.start_time) * 1000)
        log_entry = f"URL: {request.path}\nMethod: {request.method}\nExecution Time: {execution_time} ms\n"
        with open("request_logs.txt", "a") as f:
            f.write(log_entry)
        return response
    
    def process_exception(self, request, exception):
        log_entry = f"URL: {request.path}\nMethod: {request.method}\nError: {str(exception)}\n"
        with open("request_logs.txt", "a") as f:
            f.write(log_entry)
        return HttpResponse("Internal Server Error", status=500)
    




