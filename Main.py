import Account
import Request

def fulfill_request(request, other_requests, fulfilled_requests):
    for req in other_requests:
        if req.match(request):
            fulfilled_requests.append(request, req)
            other_requests.remove(req)
            return other_requests, fulfilled_requests


if __name__ == "__main__":
    #all_accounts = []
    pending_requests = []
    fulfilled_requests = []
    while pending_requests != []:
        pending_requests, fulfilled_requests = fulfill_request(pending_requests[0], pending_requests[1:], fulfilled_requests)
