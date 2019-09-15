from flask import Flask
from flask import request
from Request import Request

import json

app = Flask(__name__)
pending_requests = []

@app.route('/', methods=['POST'])

def fulfill_request(request, other_requests, fulfilled_requests):
    for req in other_requests:
        if req.match(request):
            fulfilled_requests.append((request, req))
            other_requests.remove(req)
            return other_requests, fulfilled_requests
    other_requests.append(request)
    return other_requests, fulfilled_requests

def index():
    info = json.loads(request.data)
    fulfilled_requests = []
    timesC = {
        "Monday": ["18"],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    kerb = info["kerb"]
    course = info["course"]

    pending_requests.append(Request(kerb, course, 5, timesC))
    pending_requests, fulfilled_requests = fulfill_request(pending_requests[0], pending_requests[1:], fulfilled_requests)

    req = fulfilled_requests[0][1]

    return_info = {
        "kerb": req.get_name(),
        "course": req.get_course(),
    }

    return json.dumps(return_info)
