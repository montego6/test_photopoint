from django.http import JsonResponse
from core.helpers import is_interval_not_elapsed
from main.helpers import get_client_ip
from main.models import UserRequest
from . import consts


class IntervalBetweenRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_client_ip(request)
        last_user_request = (
            UserRequest.objects.filter(ip_address=ip).order_by("-timestamp").first()
        )
        if is_interval_not_elapsed(last_user_request.timestamp):
            return JsonResponse(
                {
                    "detail": f"interval between requests is {consts.INTERVAL_IN_SECS_BETWEEN_REQUESTS} seconds"
                }
            )

        response = self.get_response(request)
        return response
