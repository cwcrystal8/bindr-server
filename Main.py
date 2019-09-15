from Request import Request

def fulfill_request(request, other_requests, fulfilled_requests):
    for req in other_requests:
        if req.match(request):
            fulfilled_requests.append((request, req))
            other_requests.remove(req)
            return other_requests, fulfilled_requests
    other_requests.append(request)
    return other_requests, fulfilled_requests


if __name__ == "__main__":
    #all_accounts = []
    timesA = {
        "Monday": [7,8,9,18,19,20],
        "Tuesday": [7,8,9,18,19,21],
        "Wednesday": [7,8,9,16,19,21],
        "Thursday": [7,8,9,16,19,21],
        "Friday": [9,16,19,21],
        "Saturday": [7,8,9,15,19,21],
        "Sunday": [7,8,9,16,19,21],
    }
    timesB = {
        "Monday": [18,19,20],
        "Tuesday": [9,18,19,21],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [9,16,19,21],
        "Saturday": [],
        "Sunday": [16,19,21],
    }
    reqA = Request("Joseph Morales","6.009", 9, timesA)
    reqB = Request("Aryan Bhatt","6.009", 7, timesB)

    pending_requests = [reqA, reqB]
    fulfilled_requests = []
    while pending_requests != []:
        pending_requests, fulfilled_requests = fulfill_request(pending_requests[0], pending_requests[1:], fulfilled_requests)
    print(pending_requests)
    print(fulfilled_requests)
